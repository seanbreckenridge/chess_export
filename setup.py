from pathlib import Path
from setuptools import setup, find_namespace_packages

reqs = Path("requirements.txt").read_text().strip().splitlines()
long_description = Path("README.md").read_text()

pkg = "chess_export"
setup(
    name=pkg,
    version="0.1.0",
    url="https://github.com/seanbreckenridge/chess_export",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description="""Export your chess.com/lichess.org games""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=reqs,
    keywords="chess data",
    entry_points={"console_scripts": ["chess_export = chess_export.__main__:main"]},
    package_data={pkg: ["py.typed"]},
    extras_require={"testing": ["mypy"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
