# chessdotcom_export

[![PyPi version](https://img.shields.io/pypi/v/chessdotcom_export.svg)](https://pypi.python.org/pypi/chessdotcom_export) [![Python 3.7|3.8|3.9](https://img.shields.io/pypi/pyversions/chessdotcom_export.svg)](https://pypi.python.org/pypi/chessdotcom_export) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Export your chess.com games using the public API. [Published-Data API Docs](https://www.chess.com/news/view/published-data-api)

## Installation

Requires `python3.6+`

To install with pip, run:

    pip install chessdotcom-export

---

### Usage

#### export

```
chessdotcom_export export --help
Usage: chessdotcom_export export [OPTIONS] USERNAME

  Export your chess games

Options:
  --help  Show this message and exit.
```

The only required argument is your username, the API serves public data and has no serial rate limit.

#### inspect

```
Usage: chessdotcom_export inspect [OPTIONS]

  Parse an exported JSON file and interact with it

Options:
  -f, --from-file PATH  Exported file to read from  [required]
  --help                Show this message and exit.
```

### Example

The games are described in [`PGN`](https://en.wikipedia.org/wiki/Portable_Game_Notation) (which can be parsed using the [`chess`](https://python-chess.readthedocs.io/en/latest/pgn.html) package), with the final board state in [`FEN`](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation), also parseable using [`chess.Board`](https://python-chess.readthedocs.io/en/latest/core.html#chess.Board)

```
$ chessdotcom_export export seanbreckenridge >data.json
Requesting https://api.chess.com/pub/player/seanbreckenridge/games/archives
Requesting https://api.chess.com/pub/player/seanbreckenridge/games/2021/01
Requesting https://api.chess.com/pub/player/seanbreckenridge/games/2021/02
$ chessdotcom_export inspect -f data.json

In [1]: import io, chess.pgn

In [2]: game = chess.pgn.read_game(io.StringIO(games[0].pgn))

In [3]: for move in game.mainline_moves():
   ...:     print(move)
   ...:
e2e4
e7e6
b1c3
d8f6
d2d3
f8c5
d3d4
c5d4
f2f3
```

### Library Usage

You can also run the commands from python:

```
In [1]: import chessdotcom_export

In [2]: games = list(map(lambda j: chessdotcom_export.Game.from_api_response(j), chessdotcom_export.get_player_games("seanbreckenridge")))
Requesting https://api.chess.com/pub/player/seanbreckenridge/games/archives
Requesting https://api.chess.com/pub/player/seanbreckenridge/games/2021/01
Requesting https://api.chess.com/pub/player/seanbreckenridge/games/2021/02

In [3]: games[0].fen
Out[3]: 'r3k2r/5ppp/1Qp5/p3p2q/K3P3/4BP1N/1PP3PP/R4B1R b kq -'

In [4]: export = chessdotcom_export.from_export("data.json")

In [5]: export[0].fen
Out[5]: 'r3k2r/5ppp/1Qp5/p3p2q/K3P3/4BP1N/1PP3PP/R4B1R b kq -'
```

### Tests

```bash
git clone 'https://github.com/seanbreckenridge/chessdotcom_export'
cd ./chessdotcom_export
pip install '.[testing]'
mypy ./chessdotcom_export
