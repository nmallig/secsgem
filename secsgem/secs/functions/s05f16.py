#####################################################################
# s05f16.py
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
"""Class for stream 05 function 16."""

from secsgem.secs.functions.base import SecsStreamFunction


class SecsS05F16(SecsStreamFunction):
    """
    exception recover complete - confirm.

    **Structure**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS05F16
        Header only

    **Example**::

        >>> import secsgem.secs
        >>> secsgem.secs.functions.SecsS05F16()
        S5F16 .

    :param value: function has no parameters
    :type value: None
    """

    _stream = 5
    _function = 16

    _data_format = None

    _to_host = False
    _to_equipment = True

    _has_reply = False
    _is_reply_required = False

    _is_multi_block = False
