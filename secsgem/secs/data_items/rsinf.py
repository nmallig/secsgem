#####################################################################
# rsinf.py
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
"""RSINF data item."""
from .. import variables
from .base import DataItemBase


class RSINF(DataItemBase):
    """
    Starting location.

    :Types:
       - :class:`I8 <secsgem.secs.variables.I8>`
       - :class:`I1 <secsgem.secs.variables.I1>`
       - :class:`I2 <secsgem.secs.variables.I2>`
       - :class:`I4 <secsgem.secs.variables.I4>`

    **Used In Function**
        - :class:`SecsS12F07 <secsgem.secs.functions.SecsS12F07>`
        - :class:`SecsS12F14 <secsgem.secs.functions.SecsS12F14>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.I1,
        variables.I2,
        variables.I4,
        variables.I8
    ]
    __count__ = 3
