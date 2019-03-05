# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from collections import Counter

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class SpecsheetReportCompute(models.TransientModel):
    # only methods are defined here
    _inherit = 'specsheet.report'

    @api.multi
    def print_report(self):
        self.ensure_one()
        order = self.order_id
        if order.procurement_group_id:
            sale_order = self.env['sale.order'].search([
                ('procurement_group_id', '=', order.procurement_group_id.id)])
            if sale_order:
                self.write({'sale_order_id': sale_order.id})
        report_name = 'mrp_specsheet_print.specsheet_report'
        return self.env['report'].get_action(self, report_name)
