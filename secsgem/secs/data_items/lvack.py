#####################################################################
# lvack.py
#
# (c) Copyright 2021, Benjamin Parzella. All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#####################################################################
"""LVACK data item."""
from .. import variables
from .base import DataItemBase


class LVACK(DataItemBase):
    """variable limit error code 
    
       :Types: :class:`secsgem.secs.variables.Binary <secsgem.secs.variables.Binary>`
       :Length: 1

    **Values**
        +-------+-------------------+------------------------------------------------+
        | Value | Description       | Constant                                       |
        +=======+===================+================================================+
        | 0     | Ok          | :const:`secsgem.secs.dataitems.VLAACK.Ok` |
        +-------+-------------------+------------------------------------------------+
        | 1     | limit attribute definition error   | :const:`secsgem.secs.dataitems.VLAACK.ERROR`    |
        +-------+-------------------+------------------------------------------------+

    **Used In Function**
        - :class:`SecsS02F46 <secsgem.secs.functions.SecsS02F46>`

    """

    __type__ = variables.Binary
    __count__ = 1

    NO_VID = 1
    LIMIT_UNSUPPORTED_VID = 2
    VARIABLE_REPEATED = 3
    LIMIT_VALUE_ERROR = 4
