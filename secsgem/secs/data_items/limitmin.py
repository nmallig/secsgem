#####################################################################
# limitmin.py
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
"""LIMITMIN data item."""
from .. import variables
from .base import DataItemBase


class LIMITMIN(DataItemBase):
    """The maximum value allowed for the upper dead band limit 

    :Types:
       - :class:`secsgem.secs.variables.F4 <secsgem.secs.variables.F4>`

    **Used In Function**
        - :class:`SecsS02F48 <secsgem.secs.functions.SecsS02F48>`
    """

    __type__ = variables.F4
