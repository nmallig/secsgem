#####################################################################
# mlcl.py
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
"""MLCL data item."""
from .. import variables
from .base import DataItemBase


class MLCL(DataItemBase):
    """
    Message length.

    :Types:
       - :class:`U8 <secsgem.secs.variables.U8>`
       - :class:`U1 <secsgem.secs.variables.U1>`
       - :class:`U2 <secsgem.secs.variables.U2>`
       - :class:`U4 <secsgem.secs.variables.U4>`

    **Used In Function**
        - :class:`SecsS12F04 <secsgem.secs.functions.SecsS12F04>`
        - :class:`SecsS12F05 <secsgem.secs.functions.SecsS12F05>`

    """

    __type__ = variables.Dynamic
    __allowedtypes__ = [
        variables.U1,
        variables.U2,
        variables.U4,
        variables.U8
    ]
