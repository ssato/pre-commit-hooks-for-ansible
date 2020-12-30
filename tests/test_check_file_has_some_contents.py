# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
"""Tests for the hook.
"""
from tests import common as C


class TestCase(C.RunHookTestCase):
    """Hook test cases."""
    filename = C.basename(__file__)

# vim:sw=4:ts=4:et:
