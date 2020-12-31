# Copyright (C) 2020 Red Hat, Inc.
# SPDX-License-Identifier: MIT
#
# pylint: disable=invalid-name,missing-function-docstring
"""Integration tests.
"""
import subprocess
import typing

import tests.common as C


class IntegrationTestCase(C.BaseTestCase):
    """
    Run pre-commit try-repo.

    .. seealso:: https://pre-commit.com/#developing-hooks-interactively
    """
    def run_pre_commit(self, expected_success: bool = True,
                       pattern: typing.Optional[str] = None) -> None:
        """Run pre-commit try-repo.
        """
        if pattern is None or not pattern:
            pattern = 'res/**/*ok*'

        files = ' '.join(sorted(str(p) for p in C.CURDIR.glob(pattern)))
        res = subprocess.run(
            f'pre-commit try-repo . --verbose --files {files}'.split(),
            stdout=subprocess.PIPE, check=False,
            cwd=str((C.CURDIR / '..').resolve())
        )
        _assert = self.assertEqual if expected_success else self.assertNotEqual
        _assert(res.returncode, 0, res.stdout.decode('utf-8'))

    def test_10_ok_cases(self):
        self.run_pre_commit()

    @C.unittest.skip('Not implemented yet')
    def test_20_ng_cases(self):
        self.run_pre_commit(False, 'res/**/*ng*')

# vim:sw=4:ts=4:et:
