#####################################################################
# remote_command.py
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
"""Wrapper for GEM remote command."""

import secsgem.secs


class RemoteCommand:
    """Remote command definition."""

    def __init__(self, rcmd, name, params, ce_finished, **kwargs):
        """
        Initialize a remote command.

        You can manually set the secs-type of the id with the 'id_type' keyword argument.

        Custom parameters can be set with the keyword arguments,
        they will be passed to the GemEquipmentHandlers callback
        :func:`secsgem.gem.equipmenthandler.GemEquipmentHandler._on_rcmd_<remote_command>`.

        :param rcmd: ID of the status variable
        :type rcmd: various
        :param name: long name of the status variable
        :type name: string
        :param params: array of available parameter names
        :type params: list
        :param ce_finished: collection event to trigger when remote command was finished
        :type ce_finished: types supported by data item CEID
        """
        self.rcmd = rcmd
        self.name = name
        self.params = params
        self.ce_finished = ce_finished

        if isinstance(self.rcmd, int):
            self.id_type = secsgem.secs.variables.U4
        else:
            self.id_type = secsgem.secs.variables.String

        for key, value in kwargs.items():
            setattr(self, key, value)
