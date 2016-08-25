from setuptools import setup

setup(
    name="github-release",
    version="0.0.2",
    description="A helper tool for creating GitHub releases",
    author="Joachim Viide <jviide@iki.fi>",
    url="https://github.com/abusesa/github-release",
    license="MIT",
    scripts=[
        "scripts/github-release"
    ],
    install_requires=[
        "requests >= 2.8.1",
        "argparse >= 1.4.0"
    ]
)
