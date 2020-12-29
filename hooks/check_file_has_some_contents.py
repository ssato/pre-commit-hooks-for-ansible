# Copyright (C) 2020 Red Hat, Inc.
#
# SPDX-License-Identifier: MIT
#
"""
Check if given file has some contents.
"""
import pathlib
import sys
import typing
import yaml


def check(filepaths: typing.Sequence[str]) -> typing.Iterator[int]:
    """Check if given file has some content.
    """
    for filepath in filepaths:
        fpath = pathlib.Path(filepath)

        if fpath.stat().st_size == 0:
            print(f'{filepath}: Looks empty')
            yield 1

        if fpath.suffix in ('.yml', '.yaml'):
            try:
                if not bool(yaml.safe_load(fpath.open())):
                    print(f'{filepath}: Looks a YAML file but has empty data')
                    yield 1
            except (OSError, IOError):
                pass


def main(argv: typing.Optional[typing.Sequence[str]] = None) -> int:
    """entry point.
    """
    if argv:
        return sum(check(argv[1:]))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
