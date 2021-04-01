import json
from typing import List

import click

from .common import Json
from .export import get_player_games
from .model import Game, from_export


@click.group()
def main() -> None:
    """
    Export your chess.com games using the public API
    """
    pass


@main.command()
@click.argument("username", type=str)
def export(username: str) -> None:
    """
    Export your chess games
    """
    games: List[Json] = list(get_player_games(username))
    click.echo(json.dumps(games, sort_keys=True))


@main.command()
@click.argument(
    "FROM_FILE",
    type=click.Path(exists=True),
    required=True,
)
def inspect(from_file: str) -> None:
    """
    Parse an exported JSON file and interact with it
    """
    games: List[Game] = list(from_export(from_file))
    click.secho("Use the 'games' variable to interact", fg="green")
    import IPython  # type: ignore[import]

    IPython.embed()


if __name__ == "__main__":
    main(prog_name="chessdotcom_export")
