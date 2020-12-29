# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-function-docstring,too-few-public-methods
"""Tests for the hook.
"""
from tests import common as C


class FunctionsTestCase(C.BaseTestCase):
    """Test cases for functions.
    """

    def test_list_res_files(self):
        self.assertTrue(
            C.list_res_files('check_utf8_with_unix_style_new_lines', '*ok*')
        )
        with self.assertRaises(RuntimeError):
            C.list_res_files('dir_not_exist', '*ng*')

    def test_make_pattern(self):
        self.assertEqual(C.make_pattern(), '*ok*.*')
        self.assertEqual(C.make_pattern(False), '*ng*.*')
        self.assertEqual(C.make_pattern(pattern='a/b/c'), 'a/b/c')

    def test_basename(self):
        self.assertEqual(C.basename('a/b/c/d.txt'), 'd.txt')


class BaseTestCase(C.BaseTestCase):
    """Test cases for BaseTestCase.
    """
    filename = C.basename(__file__)

    def test_filename_name_hook(self):
        self.assertEqual(self.filename, 'test_common.py')
        self.assertEqual(self.name, 'common')
        self.assertEqual(self.hook, 'common.py')


# vim:sw=4:ts=4:et:
