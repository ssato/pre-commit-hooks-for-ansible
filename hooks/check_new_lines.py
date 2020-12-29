# Copyright (C) 2020 Red Hat, Inc.
#
# SPDX-License-Identifier: MIT
#
"""Check if newline code in file is LF.
"""
import re
import sys
import typing

NON_UNIX_NEWLINE = r'\r\n?$'


def has_non_unix_newline(path: str) -> bool:
    """
    :param path: A path to the file
    """
    with open(path, newline='') as strm:
        if any([line for line in strm if re.search(NON_UNIX_NEWLINE, line)]):
            return True
    return False


def check(filepaths: typing.Sequence[str]) -> typing.Iterator[int]:
    """Check new lines in files in given paths.
    """
    for fpath in filepaths:
        yield 1 if has_non_unix_newline(fpath) else 0


def main(argv: typing.Optional[typing.Sequence[str]] = None) -> int:
    """entry point.
    """
    if argv:
        return sum(check(argv[1:]))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
