"""
Parse and Serialize the Game response from chess.com
"""

import json

from datetime import datetime, timezone
from typing import NamedTuple, List, Optional

from .common import Json


class UserRating(NamedTuple):
    rating: int
    result: str
    id_: str
    username: str

    @classmethod
    def from_api_response(cls, api_resp: Json) -> "UserRating":
        return cls(
            rating=api_resp["rating"],
            result=api_resp["result"],
            id_=api_resp["@id"],
            username=api_resp["username"],
        )

    def to_dict(self) -> Json:
        return {
            "rating": self.rating,
            "result": self.result,
            "@id": self.id_,
            "username": self.username,
        }


class Game(NamedTuple):
    url: str
    pgn: Optional[str]
    fen: str
    time_control: str
    end_time: datetime
    rated: bool
    time_class: str
    rules: str
    white: UserRating
    black: UserRating

    @classmethod
    def from_api_response(cls, api_resp: Json) -> "Game":
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
            white=UserRating.from_api_response(api_resp["white"]),
            black=UserRating.from_api_response(api_resp["black"]),
        )

    def to_dict(self) -> Json:
        return {
            "url": self.url,
            "pgn": self.pgn,
            "time_control": self.time_control,
            "end_time": int(self.end_time.timestamp()),
            "rated": self.rated,
            "fen": self.fen,
            "time_class": self.time_class,
            "rules": self.rules,
            "white": self.white.to_dict(),
            "black": self.black.to_dict(),
        }


def from_export(filepath: str) -> List[Game]:
    """
    Parse a chessdotcom_export file
    """
    games: List[Game] = []
    with open(filepath) as f:
        obj: Json = json.load(f)
        for gobj in obj:
            games.append(Game.from_api_response(gobj))
    return games
