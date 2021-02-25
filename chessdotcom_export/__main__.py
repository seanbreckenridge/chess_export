import sys
import json

import click

from .export import get_player_games


@click.command()
@click.option(
    "--username", "-u", type=str, required=True, help="Display debug messages"
)
def main(username: str) -> None:
    """
    Export your chess.com games using the public API
    """
    click.echo(json.dumps(list(get_player_games(username))))

if __name__ == "__main__":
    main(prog_name="chessdotcom_export")
