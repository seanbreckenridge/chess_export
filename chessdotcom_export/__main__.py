import json
from typing import List, Any

import click
import IPython  # type: ignore[import]

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
    games: List[Any] = []
    for game in get_player_games(username):
        games.append(game)
    click.echo(json.dumps(games, sort_keys=True))


@main.command()
@click.option(
    "--from-file",
    "-f",
    "from_",
    type=click.Path(exists=True),
    required=True,
    help="Exported file to read from",
)
def inspect(from_: str) -> None:
    """
    Parse an exported JSON file and interact with it
    """
    games: List[Game] = from_export(from_)
    click.echo("Use the 'games' variable to interact")
    IPython.embed()


if __name__ == "__main__":
    main(prog_name="chessdotcom_export")
