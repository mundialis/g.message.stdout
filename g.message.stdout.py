#!/usr/bin/env python3

############################################################################
#
# MODULE:       g.message.stdout
# AUTHOR(S):    Anika Weinmann
# PURPOSE:      This module writes a message to stdout
#
# COPYRIGHT:    (C) 2021-2022 by mundialis GmbH & Co. KG and the GRASS Development Team
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

# %module
# % label: Prints a message to stdout
# % description: This module writes a message to stdout.
# % keyword: general
# % keyword: support
# % keyword: scripts
# %end

# %option
# % key: message
# % type: string
# % required: yes
# % multiple: no
# % key_desc: string
# % label: Text of the message to be printed
# % description: Message is printed on GRASS_VERBOSE>=2
# %end


import sys
import grass.script as grass


def main():
    print(options["message"])


if __name__ == "__main__":
    options, flags = grass.parser()
    sys.exit(main())
