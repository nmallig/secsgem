#####################################################################
# hosthandler.py
#
# (c) Copyright 2013-2021, Benjamin Parzella. All rights reserved.
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
"""Handler for GEM host."""

import collections

import secsgem.secs

from .handler import GemHandler


class GemHostHandler(GemHandler):
    """Baseclass for creating host models. Inherit from this class and override required functions."""

    def __init__(self, address, port, active, session_id, name, custom_connection_handler=None):
        """
        Initialize a gem host handler.

        :param address: IP address of remote host
        :type address: string
        :param port: TCP port of remote host
        :type port: integer
        :param active: Is the connection active (*True*) or passive (*False*)
        :type active: boolean
        :param session_id: session / device ID to use for connection
        :type session_id: integer
        :param name: Name of the underlying configuration
        :type name: string
        :param custom_connection_handler: object for connection handling (ie multi server)
        :type custom_connection_handler: :class:`secsgem.hsms.connections.HsmsMultiPassiveServer`
        """
        GemHandler.__init__(self, address, port, active, session_id, name, custom_connection_handler)

        self.isHost = True

        self.reportSubscriptions = {}
        self.ce_report_subscriptions = {}

    def clear_collection_events(self):
        """Clear all collection events."""
        self.logger.info("Clearing collection events")

        # clear subscribed reports
        self.reportSubscriptions = {}
        self.ce_report_subscriptions = {}

        # disable all ceids
        self.disable_ceids()

        # delete all reports
        self.disable_ceid_reports()

    def subscribe_collection_event(self, ceid, dvs, report_id=None):
        """
        Subscribe to a collection event.

        :param ceid: ID of the collection event
        :type ceid: integer
        :param dvs: DV IDs to add for collection event
        :type dvs: list of integers
        :param report_id: optional - ID for report, autonumbering if None
        :type report_id: integer
        """
        self.logger.info("Subscribing to collection event %s", ceid)

        if report_id is None:
            report_id = self.reportIDCounter
            self.reportIDCounter += 1

        # note subscribed reports
        self.reportSubscriptions[report_id] = dvs
        if ceid in self.ce_report_subscriptions:
            self.ce_report_subscriptions[ceid].add(report_id)
        else:
            self.ce_report_subscriptions[ceid] = set([report_id])

        # create report
        self.send_and_waitfor_response(self.stream_function(2, 33)(
            {"DATAID": 0, "DATA": [{"RPTID": report_id, "VID": dvs}]}))

        # link event report to collection event
        self.send_and_waitfor_response(self.stream_function(2, 35)(
            {"DATAID": 0, "DATA": [{"CEID": ceid, "RPTID": [report_id]}]}))

        # enable collection event
        self.send_and_waitfor_response(self.stream_function(2, 37)({"CEED": True, "CEID": [ceid]}))

    def list_events(self, ce_ids=[]):
        """
        List events.

        :param ce_ids: events to list details for
        :type ce_ids: array of int/str
        """
        if not isinstance(ce_ids,list):
            ce_ids = [ce_ids]

        self.logger.info("List events {}".format(ce_ids))

        packet = self.send_and_waitfor_response(self.stream_function(1, 23)(ce_ids))
        decoded = self.secs_decode(packet).get()

        return decoded

    def send_remote_command(self, rcmd, params):
        """
        Send a remote command.

        :param rcmd: Name of command
        :type rcmd: string
        :param params: DV IDs to add for collection event
        :type params: list of strings
        """
        self.logger.info("Send RCMD %s", rcmd)

        s2f41 = self.stream_function(2, 41)()
        s2f41.RCMD = rcmd
        if isinstance(params, list):
            for param in params:
                s2f41.PARAMS.append({"CPNAME": param[0], "CPVAL": param[1]})
        elif isinstance(params, collections.OrderedDict):
            for param in params:
                s2f41.PARAMS.append({"CPNAME": param, "CPVAL": params[param]})

        # send remote command
        return self.secs_decode(self.send_and_waitfor_response(s2f41))

    def delete_process_programs(self, ppids):
        """
        Delete a list of process program.

        :param ppids: Process programs to delete
        :type ppids: list of strings
        """
        self.logger.info("Delete process programs %s", ppids)

        # send remote command
        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(7, 17)(ppids))).get()

    def get_process_program_list(self):
        """Get process program list."""
        self.logger.info("Get process program list")

        # send remote command
        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(7, 19)())).get()

    def go_online(self):
        """Set control state to online."""
        self.logger.info("Go online")

        # send remote command
        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(1, 17)())).get()

    def go_offline(self):
        """Set control state to offline."""
        self.logger.info("Go offline")

        # send remote command
        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(1, 15)())).get()

    def enable_alarm(self, alid):
        """
        Enable alarm.

        :param alid: alarm id to enable, [] for all alarms
        :type alid: :class:`secsgem.secs.dataitems.ALID`
        """
        self.logger.info("Enable alarm %s", str(alid) if alid != [] else 'ALL')

        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(5, 3)(
            {"ALED": secsgem.secs.data_items.ALED.ENABLE, "ALID": alid}))).get()

    def disable_alarm(self, alid):
        """
        Disable alarm.

        :param alid: alarm id to disable, [] for all alarms
        :type alid: :class:`secsgem.secs.dataitems.ALID`
        """
        self.logger.info("Disable alarm %s", str(alid) if alid != [] else 'ALL')

        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(5, 3)(
            {"ALED": secsgem.secs.data_items.ALED.DISABLE, "ALID": alid}))).get()

    def list_alarms(self, alids=None):
        """
        List alarms.

        :param alids: alarms to list details for
        :type alids: array of int/str
        """
        if alids is None:
            alids = []
            self.logger.info("List all alarms")
        else:
            self.logger.info("List alarms %s", alids)

        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(5, 5)(alids))).get()

    def list_enabled_alarms(self):
        """List enabled alarms."""
        self.logger.info("List all enabled alarms")

        return self.secs_decode(self.send_and_waitfor_response(self.stream_function(5, 7)())).get()

    def _on_alarm_received(self, handler, ALID, ALCD, ALTX):
        del handler, ALID, ALCD, ALTX  # unused variables
        return secsgem.secs.data_items.ACKC5.ACCEPTED

    def _on_s05f01(self, handler, packet):
        """
        Handle Stream 5, Function 1, Alarm request.

        :param handler: handler the message was received on
        :type handler: :class:`secsgem.hsms.handler.HsmsHandler`
        :param packet: complete message received
        :type packet: :class:`secsgem.hsms.HsmsPacket`
        """
        s5f1 = self.secs_decode(packet)

        result = self._callback_handler.alarm_received(handler, s5f1.ALID, s5f1.ALCD, s5f1.ALTX)

        self.events.fire("alarm_received", {"code": s5f1.ALCD, "alid": s5f1.ALID, "text": s5f1.ALTX,
                                            "handler": self.connection, 'peer': self})

        return self.stream_function(5, 2)(result)


    def _on_s06f11(self, handler, packet):
        """
        Handle Stream 6, Function 11, Event Report Send.

        :param handler: handler the message was received on
        :type handler: :class:`secsgem.hsms.handler.HsmsHandler`
        :param packet: complete message received
        :type packet: :class:`secsgem.hsms.HsmsPacket`
        """
        del handler  # unused parameters

        message = self.secs_decode(packet)

        reports = self._preprocess_event_report(message)

        for data in reports:
            self.events.fire("collection_event_received", data)

        return self.stream_function(6, 12)(0)


    def _preprocess_event_report(self, message):
        """
        Common code for preprocessing the data received by S6,F11 and S6,F15/16

        :param message: decoded hsms packet (S6,F11 or S6,F16 message)
        """
        reports = []

        for report in message.RPT:
            report_values = report.V.get()
            report_dvs = self._get_report_dvs(report.RPTID.get(), 
                                                len(report_values))

            values = []

            for i, s in enumerate(report_dvs):
                values.append({"dvid": s, 
                               "value": report_values[i], 
                               "name": self.get_dvid_name(s)})

            data = {"dataid" : message.DATAID.get(),
                    "ceid": message.CEID.get(), 
                    "rptid": report.RPTID.get(), 
                    "values": values,
                    "name": self.get_ceid_name(message.CEID.get()), 
                    "handler": self.connection, 'peer': self}

            reports.append(data)

        return reports


    def _get_report_dvs(self, rptid, nvals):
        """
        Returns the data values for the given rptid 
        if the report is registered in self.reportSubscriptions,
        otherwise a list of None's of length 'nvals'.
        Can be overwritten in subclasses for improved support 
        of not registered reports.

        :param rptid: id of report
        :type report: int
        :param nval: number of None's in case of not registered 'rptid'
        :type nval: int
        """
        if rptid in self.reportSubscriptions:
            return self.reportSubscriptions[rptid]
        else:
            return [None,]*nvals


    def request_event_report(self, ceid):
        """
        Request event report(s) for given 'ceid' (using the S6,F15 message).

        :param ceid: id of collection event
        :type ceid: int
        """
        packet = self.send_and_waitfor_response(
                        self.stream_function(6, 15)(ceid))
        message = self.secs_decode(packet)

        return self._preprocess_event_report(message)


    def request_individual_report(self, rptid):
        """
        Request event report for given 'rptid' (using the S6,F19 message).

        :param rptid: id of report
        :type rptid: int
        """
        packet = self.send_and_waitfor_response(
                        self.stream_function(6, 19)(rptid))
        msg = self.secs_decode(packet)

        report_values = msg.get()
        report_dvs = self._get_report_dvs(rptid, len(report_values))

        values = []
        
        for i, s in enumerate(report_dvs):
            values.append({"dvid": s, 
                            "value": report_values[i], 
                            "name": self.get_dvid_name(s)})

        data = {"rptid": rptid, 
                "values": values,
                "handler": self.connection, 
                "peer": self}
        return data


    def clear_report(self, rptid):
        """
        Deletes report definition for given 'rptid' (using the S2,F33 message).

        :param rptid: id of report
        :type rptid: int
        """
        msg = self.stream_function(2, 33)(
                {"DATAID" : 0, 
                 "DATA" : [{"RPTID" : rptid, "VID" : []}]})
        packet = self.send_and_waitfor_response(msg)
        ack = self.secs_decode(packet).get()
        if not ack == secsgem.secs.data_items.DRACK.ACK:
            self.logger.error("Operation failed: error code={}".format(DRACK))
        else:
            self.reportSubscriptions.pop(rptid, None)
            for ce in self.ce_report_subscriptions.values():
                ce.discard(rptid)


    def clear_event_report(self, ceid):
        """
        Deletes all report definitions linked to given 'ceid' 
        (using the S2,F35 message).

        :param ceid: id of report
        :type ceid: int
        """
        msg = self.stream_function(2, 35)(
                {"DATAID" : 0, 
                 "DATA" : [{"CEID" : ceid, "RPTID" : []}]})
        packet = self.send_and_waitfor_response(msg)
        ack = self.secs_decode(packet).get()
        if not ack == secsgem.secs.data_items.LRACK.ACK:
            self.logger.error("Operation failed: error code={}".format(DRACK))
        else:
            rptids = self.ce_report_subscriptions.pop(ceid,[])
            for report_id in rptids:
                del self.reportSubscriptions[report_id]


    def _on_terminal_received(self, handler, TID, TEXT):
        del handler, TID, TEXT  # unused variables
        return secsgem.secs.data_items.ACKC10.ACCEPTED

    def _on_s10f01(self, handler, packet):
        """
        Handle Stream 10, Function 1, Terminal Request.

        :param handler: handler the message was received on
        :type handler: :class:`secsgem.hsms.handler.HsmsHandler`
        :param packet: complete message received
        :type packet: :class:`secsgem.hsms.HsmsPacket`
        """
        s10f1 = self.secs_decode(packet)

        result = self._callback_handler.terminal_received(handler, s10f1.TID, s10f1.TEXT)
        self.events.fire("terminal_received", {"text": s10f1.TEXT, "terminal": s10f1.TID, "handler": self.connection,
                                               'peer': self})

        return self.stream_function(10, 2)(result)

    def list_dvs(self, dvs=None):
        """Get list of available Data Variables.

        :returns: available data Variables
        :rtype: list
        """
        self.logger.info("Get list of data variables")

        if dvs is None:
            dvs = []

        if not isinstance(dvs, list):
            dvs = [dvs]

        packet = self.send_and_waitfor_response(self.stream_function(1, 21)(dvs))

        return self.secs_decode(packet)

