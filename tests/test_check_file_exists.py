# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-function-docstring,too-few-public-methods
"""Tests for the hook.
"""
import typing

from tests import common as C


class TestCase(C.BaseTestCase):
    """Test cases for BaseTestCase.
    """
    filename = C.basename(__file__)

    def run_hook(self, filepaths: typing.Iterable[str],
                 expected_success: bool = True) -> None:
        res = C.subprocess.run(
            ('python3', self.hook_path, *list(filepaths)),
            stdout=C.subprocess.PIPE, check=False
        )
        if expected_success:
            self.assertEqual(res.returncode, 0, res.stdout.decode('utf-8'))
        else:
            self.assertNotEqual(res.returncode, 0,
                                res.stdout.decode('utf-8'))

    def test_exists(self):
        files = (str(f) for f in C.CURDIR.glob('*.py'))
        self.run_hook(files)

    def test_not_exists(self):
        files = ('file_not_exists_0.txt', 'file_not_exists_1.txt')
        self.run_hook(files, False)

# vim:sw=4:ts=4:et:
