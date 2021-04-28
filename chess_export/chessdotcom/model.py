"""
Parse the Game response JSON object from lichess.org
"""

import json

from datetime import datetime, timezone
from typing import NamedTuple, Optional, Iterator

from ..common import Json


class ChessDotComUserRating(NamedTuple):
    rating: int
    result: str
    id_: str
    username: str

    @classmethod
    def from_api_response(cls, api_resp: Json) -> "ChessDotComUserRating":
        return cls(
            rating=api_resp["rating"],
            result=api_resp["result"],
            id_=api_resp["@id"],
            username=api_resp["username"],
        )


class ChessDotComGame(NamedTuple):
    url: str
    pgn: Optional[str]
    fen: str
    time_control: str
    end_time: datetime
    rated: bool
    time_class: str
    rules: str
    white: ChessDotComUserRating
    black: ChessDotComUserRating

    @classmethod
    def from_api_response(cls, api_resp: Json) -> "ChessDotComGame":
        # the pgn typically exists, but may not for some older games?, unsure why
        return cls(
            url=api_resp["url"],
            pgn=api_resp.get("pgn"),
            fen=api_resp["fen"],
            time_control=api_resp["time_control"],
            end_time=datetime.fromtimestamp(api_resp["end_time"], tz=timezone.utc),
            rated=api_resp["rated"],
            time_class=api_resp["time_class"],
            rules=api_resp["rules"],
            white=ChessDotComUserRating.from_api_response(api_resp["white"]),
            black=ChessDotComUserRating.from_api_response(api_resp["black"]),
        )


def from_export(filepath: str) -> Iterator[ChessDotComGame]:
    """
    Parse a chess.com exported file
    """
    with open(filepath) as f:
        for gobj in json.load(f):
            yield ChessDotComGame.from_api_response(gobj)
