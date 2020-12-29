# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-function-docstring,too-few-public-methods
"""Tests for the hook.
"""
import typing

import hooks.check_utf8_with_unix_style_new_lines as TT

from tests import common as C


class Base(C.BaseTestCase):
    """Base class."""
    filename = C.basename(__file__)


class FunctionTestCase(Base, C.BaseTestCase):
    """Function test cases."""
    def _assert(self, fun: typing.Callable, pattern: str = '*ok*',
                assert_meth: typing.Optional[typing.Callable] = None) -> None:
        if assert_meth is None:
            assert_meth = self.assertTrue

        for fpath in C.list_res_files(self.name, pattern):
            assert_meth(fun(fpath), fpath)

    def test_is_utf8_file_without_bom(self):
        self._assert(TT.is_utf8_file_without_bom)
        self._assert(TT.is_utf8_file_without_bom, '*ng_encoding*',
                     self.assertFalse)

    def test_has_non_unix_newline(self):
        self._assert(TT.has_non_unix_newline, '*_ok_utf-8*', self.assertFalse)
        self._assert(TT.has_non_unix_newline, '*_ng_utf-8*', self.assertTrue)


class TestCase(Base, C.RunHookTestCase):
    """Hook test cases."""

# vim:sw=4:ts=4:et:
