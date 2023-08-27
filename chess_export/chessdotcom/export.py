"""
Request/Export your games from chess.com
"""

from typing import Iterator, List

from ..common import Json, safe_request_json

BASE_URL = "https://api.chess.com/pub/"


def get_player_game_archives(username: str) -> List[str]:
    """Returns a list of monthly archive URLs for the user"""
    url = BASE_URL + "/".join(("player", username, "games", "archives"))
    mresp = safe_request_json(url)
    return list(mresp["archives"])


def get_player_games(username: str) -> Iterator[Json]:
    """Returns all accessible games, using the monthly archive as the source"""
    for archive_url in get_player_game_archives(username):
        yield from safe_request_json(archive_url)["games"]
