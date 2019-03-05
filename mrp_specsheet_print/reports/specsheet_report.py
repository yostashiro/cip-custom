# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SpecsheetReport(models.TransientModel):
    _name = 'specsheet.report'

    order_id = fields.Many2one(
        'mrp.production',
    )
    limit_locs = fields.Boolean()
    website_published = fields.Boolean()
    categ_name = fields.Char()

    # Data fields, used to browse report data
    categ_id = fields.Many2one(
        comodel_name='product.category',
    )
    line_ids = fields.One2many(
        comodel_name='specsheet.report.line',
        inverse_name='report_id'
    )
