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


def is_utf8_file_without_bom(filepath: str) -> bool:
    """Check if given file is encoded with utf-8 without BOM.
    """
    try:
        with open(filepath, encoding='utf-8') as fileobj:
            return not fileobj.read(10).startswith("\ufeff")
    except UnicodeDecodeError:  # Not in 'utf-8'.
        pass

    return False


def has_non_unix_newline(filepath: str) -> bool:
    """Check if lines in given file end with unix style line breaks.
    """
    with open(filepath, newline='') as fio:
        for line in fio:
            # Only try checking the first line to avoid the whole lines.
            return re.search(NON_UNIX_NEWLINE, line) is not None

    return False  # It's empty.


def check(filepaths: typing.Sequence[str]) -> typing.Iterator[int]:
    """Check new lines in files in given paths.
    """
    for fpath in filepaths:
        if is_utf8_file_without_bom(fpath):
            if has_non_unix_newline(fpath):
                print(f'{fpath}: Has non-unix style new lines')
                yield 1
        else:
            print(f'{fpath}: Not UTF-8 or UTF-8 but with BOM')
            yield 1


def main(argv: typing.Optional[typing.Sequence[str]] = None) -> int:
    """entry point.
    """
    if argv:
        return sum(check(argv[1:]))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
