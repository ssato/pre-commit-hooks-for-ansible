# Copyright (C) 2020 Red Hat, Inc.
#
# SPDX-License-Identifier: MIT
#
"""
Check if given file has some contents.
"""
import argparse
import pathlib
import sys
import typing


def check(filepaths: typing.Sequence[str]) -> typing.Iterator[int]:
    """Check if given file has some content.
    """
    for filepath in filepaths:
        if not pathlib.Path(filepath).exists():
            print(f'Not exist: {filepath}')
            yield 1


def main(argv: typing.Optional[typing.Sequence[str]] = None) -> int:
    """entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'files', nargs='*', metavar='FILE',
        help='Specify file path to check if it exists'
    )
    args = parser.parse_args(argv)
    return sum(check(args.files))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
