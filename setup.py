import io
from setuptools import setup, find_packages

requirements = ["click>=7.0", "requests", "IPython"]

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fo:
    long_description = fo.read()

pkg = "chessdotcom_export"
setup(
    name=pkg,
    version="0.1.1",
    url="https://github.com/seanbreckenridge/chessdotcom_export",
    author="Sean Breckenridge",
    author_email="seanbrecke@gmail.com",
    description=("""Export your chess.com games using the public API"""),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(include=["chessdotcom_export"]),
    install_requires=requirements,
    keywords="chess data",
    entry_points={
        "console_scripts": ["chessdotcom_export = chessdotcom_export.__main__:main"]
    },
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
