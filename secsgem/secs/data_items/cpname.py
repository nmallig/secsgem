#####################################################################
# cpname.py
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
"""CPNAME data item."""
from .. import variables
from .base import DataItemBase


class CPNAME(DataItemBase):
    """
    Command parameter name.

    :Types:
       - :class:`String <secsgem.secs.variables.String>`
       - :class:`I8 <secsgem.secs.variables.I8>`
       - :class:`I1 <secsgem.secs.variables.I1>`
       - :class:`I2 <secsgem.secs.variables.I2>`
       - :class:`I4 <secsgem.secs.variables.I4>`
       - :class:`U8 <secsgem.secs.variables.U8>`
       - :class:`U1 <secsgem.secs.variables.U1>`
       - :class:`U2 <secsgem.secs.variables.U2>`
       - :class:`U4 <secsgem.secs.variables.U4>`

    **Used In Function**
        - :class:`SecsS02F41 <secsgem.secs.functions.SecsS02F41>`
        - :class:`SecsS02F42 <secsgem.secs.functions.SecsS02F42>`
        - :class:`SecsS02F49 <secsgem.secs.functions.SecsS02F49>`
        - :class:`SecsS02F50 <secsgem.secs.functions.SecsS02F50>`
        - :class:`SecsS04F21 <secsgem.secs.functions.SecsS04F21>`
        - :class:`SecsS04F29 <secsgem.secs.functions.SecsS04F29>`
        - :class:`SecsS16F05 <secsgem.secs.functions.SecsS16F05>`
        - :class:`SecsS16F27 <secsgem.secs.functions.SecsS16F27>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.U1,
        variables.U2,
        variables.U4,
        variables.U8,
        variables.I1,
        variables.I2,
        variables.I4,
        variables.I8,
        variables.String
    ]
