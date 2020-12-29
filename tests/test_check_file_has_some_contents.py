# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-function-docstring,too-few-public-methods
"""Tests for the hook.
"""
from tests import common as C


class Base(C.BaseTestCase):
    """Base class."""
    filename = C.basename(__file__)


class TestCase(Base, C.RunHookTestCase):
    """Hook test cases."""

# vim:sw=4:ts=4:et:
