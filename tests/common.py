# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name,missing-function-docstring
"""Common utility test routines and classes.
"""
import pathlib
import subprocess
import typing
import unittest


CURDIR = pathlib.Path(__file__).resolve().parent
HOOKS_DIR = CURDIR.parent / 'hooks'


def list_res_files(name: str, pattern: str) -> typing.Iterable[str]:
    """List resource data files for `name`.
    """
    files = sorted(str(p) for p in (CURDIR / 'res' / name).glob(pattern))
    if not files:
        raise RuntimeError('No resource data files were found for '
                           '{}, pattern = {}'.format(name, pattern))

    return files


def make_pattern(expected_success: bool = True,
                 pattern: typing.Optional[str] = None) -> str:
    """Make up a pattern string.
    """
    if pattern is None or not pattern:
        return '*{}*.*'.format('ok' if expected_success else 'ng')

    return pattern


def basename(fname):
    """Get base filename from filepath.
    """
    return pathlib.Path(fname).name


class BaseTestCase(unittest.TestCase):
    """Base class to test ansible-lint rules.
    """
    filename = basename(__file__)

    def setUp(self) -> None:
        if 'test_' not in self.filename:
            self.name = self.hook = self.hook_path = None
        else:
            self.hook = self.filename.replace('test_', '')
            self.name = self.hook.replace('.py', '')
            self.hook_path = str(HOOKS_DIR / self.hook)


class RunHookTestCase(BaseTestCase):
    """Base class to test ansible-lint rules.
    """
    def run_hook(self, expected_success: bool = True,
                 pattern: typing.Optional[str] = None):
        """Run hook script to targets matches given file path pattern.
        """
        if self.hook is None or not self.hook:
            return

        pattern = make_pattern(expected_success, pattern)

        for filepath in list_res_files(self.name, pattern):
            res = subprocess.run(
                ('python3', self.hook_path, filepath),
                stdout=subprocess.PIPE, check=False,
            )
            if expected_success:
                self.assertEqual(res.returncode, 0, res.stdout.decode('utf-8'))
            else:
                self.assertNotEqual(res.returncode, 0,
                                    res.stdout.decode('utf-8'))

    def test_10_ok_cases(self):
        self.run_hook()

    def test_20_ng_cases(self):
        self.run_hook(False)

# vim:sw=4:ts=4:et:
