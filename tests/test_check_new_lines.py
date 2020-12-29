# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-function-docstring,too-few-public-methods
"""Tests for the hook.
"""
import hooks.check_new_lines as TT

from tests import common as C


class Base(C.BaseTestCase):
    """Base class."""
    filename = C.basename(__file__)


class FunctionTestCase(Base, C.BaseTestCase):
    """Function test cases."""
    def test_has_non_unix_newline(self):
        for fpath in C.list_res_files(self.name, "*ok*"):
            self.assertFalse(TT.has_non_unix_newline(fpath), fpath)

        for fpath in C.list_res_files(self.name, "*ng*"):
            self.assertTrue(TT.has_non_unix_newline(fpath), fpath)


class TestCase(Base, C.RunHookTestCase):
    """Hook test cases."""

# vim:sw=4:ts=4:et:
