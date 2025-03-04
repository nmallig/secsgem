#####################################################################
# s09f13.py
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
"""Class for stream 09 function 13."""

from secsgem.secs.functions.base import SecsStreamFunction
from secsgem.secs.data_items import MEXP, EDID


class SecsS09F13(SecsStreamFunction):
    """
    conversation timeout.

    **Data Items**

    - :class:`MEXP <secsgem.secs.data_items.MEXP>`
    - :class:`EDID <secsgem.secs.data_items.EDID>`

    **Structure**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS09F13
        {
            MEXP: A[6]
            EDID: U1/U2/U4/U8/I1/I2/I4/I8/A/B
        }

    **Example**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS09F13({"MEXP": "S01E01", "EDID": "data"})
        S9F13
          <L [2]
            <A "S01E01">
            <A "data">
          > .

    :param value: parameters for this function (see example)
    :type value: dict
    """

    _stream = 9
    _function = 13

    _data_format = [
        MEXP,
        EDID
    ]

    _to_host = True
    _to_equipment = False

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = False
