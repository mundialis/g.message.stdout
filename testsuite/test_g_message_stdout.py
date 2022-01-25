#!/usr/bin/env python3

############################################################################
#
# MODULE:       g.message.stdout
# AUTHOR(S):    Anika Weinmann
# PURPOSE:      Tests g.message.stdout GRASS module
#
# COPYRIGHT:    (C) 2021-2022 mundialis GmbH & Co. KG and the GRASS Development Team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#############################################################################

from grass.gunittest.case import TestCase
from grass.gunittest.main import test
from grass.gunittest.gmodules import SimpleModule


class TestGMessageStdout(TestCase):
    msg = "Hello World"

    def test_message(self):
        """Test if message is written to stdout"""
        g_message_stdout = SimpleModule("g.message.stdout", message=self.msg)
        self.assertModule(g_message_stdout)
        stdout = g_message_stdout.outputs.stdout
        stderr = g_message_stdout.outputs.stderr
        self.assertTrue(stdout)
        self.assertEqual(self.msg, stdout.strip())
        self.assertEqual("", stderr)


if __name__ == "__main__":
    test()
