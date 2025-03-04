#####################################################################
# acka.py
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
"""ACKA data item."""
from .. import variables
from .base import DataItemBase


class ACKA(DataItemBase):
    """
    Request success.

       :Types: :class:`Boolean <secsgem.secs.variables.Boolean>`
       :Length: 1

    **Values**
        +-------+---------+
        | Value |         |
        +=======+=========+
        | True  | Success |
        +-------+---------+
        | False | Failed  |
        +-------+---------+

    **Used In Function**
        - :class:`SecsS05F14 <secsgem.secs.functions.SecsS05F14>`
        - :class:`SecsS05F15 <secsgem.secs.functions.SecsS05F15>`
        - :class:`SecsS05F18 <secsgem.secs.functions.SecsS05F18>`
        - :class:`SecsS16F02 <secsgem.secs.functions.SecsS16F02>`
        - :class:`SecsS16F04 <secsgem.secs.functions.SecsS16F04>`
        - :class:`SecsS16F06 <secsgem.secs.functions.SecsS16F06>`
        - :class:`SecsS16F12 <secsgem.secs.functions.SecsS16F12>`
        - :class:`SecsS16F14 <secsgem.secs.functions.SecsS16F14>`
        - :class:`SecsS16F16 <secsgem.secs.functions.SecsS16F16>`
        - :class:`SecsS16F18 <secsgem.secs.functions.SecsS16F18>`
        - :class:`SecsS16F24 <secsgem.secs.functions.SecsS16F24>`
        - :class:`SecsS16F26 <secsgem.secs.functions.SecsS16F26>`
        - :class:`SecsS16F28 <secsgem.secs.functions.SecsS16F28>`
        - :class:`SecsS16F30 <secsgem.secs.functions.SecsS16F30>`
        - :class:`SecsS17F04 <secsgem.secs.functions.SecsS17F04>`
        - :class:`SecsS17F08 <secsgem.secs.functions.SecsS17F08>`
        - :class:`SecsS17F14 <secsgem.secs.functions.SecsS17F14>`

    """

    __type__ = variables.Boolean
    __count__ = 1
