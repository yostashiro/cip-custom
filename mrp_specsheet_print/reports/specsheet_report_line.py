# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SpecsheetReportLine(models.TransientModel):
    _name = 'specsheet.report.line'

    report_id = fields.Many2one(
        comodel_name='specsheet.report',
        ondelete='cascade',
        index=True,
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        index=True,
    )
    categ_id = fields.Many2one(
        comodel_name='product.category',
    )
    product_name = fields.Char()
    categ_name = fields.Char()
    quantity = fields.Float()
