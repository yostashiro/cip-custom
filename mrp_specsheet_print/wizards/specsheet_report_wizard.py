# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api


class SpecsheetReportWizard(models.TransientModel):
    _name = "specsheet.report.wizard"
    _description = 'Spec Sheet Print Wizard'

    # threshold_date = fields.Date(
    #     string='Threshold Date',
    #     default=fields.Date.context_today,
    #     required=True,
    # )
    limit_locs = fields.Boolean(
        string='Limit Locations',
        default=True,
        help="Only consider stock in locations that are meant to be available "
             "for customers. If unselected, consider all the internal "
             "locations",
    )
    website_published = fields.Boolean(
        string='Only Show Products Published on Website',
        default=True,
        help="Enable option to filter out the products that are unpublished "
             "on website. Otherwise, both published and unpublished product "
             "will be exported to the report",
    )
    categ_id = fields.Many2one(
        comodel_name='product.category',
        string='Product Category',
    )

    @api.multi
    def action_export_xlsx(self):
        self.ensure_one()
        report = self.env['specsheet.report'].create(self._prepare_report())
        self._create_report_lines(report)
        return report.print_report()

    def _prepare_report(self):
        self.ensure_one()
        return {
            'order_id': self.env.context.get('active_id'),
            'limit_locs': self.limit_locs,
            'website_published': self.website_published,
            'categ_id': self.categ_id.id or False,
            'categ_name': self.categ_id.display_name or False
        }

    def _create_report_lines(self, report):
        self.ensure_one()
        for ln in report.order_id.move_raw_ids:
            line_data = {
                'report_id': report.id,
                'product_id': ln.product_id.id,
                'product_name': ln.product_id.display_name,
                'categ_id': ln.product_id.categ_id.id,
                'categ_name': ln.product_id.categ_id.display_name,
                'quantity': ln.product_uom_qty,
            }
            self.env['specsheet.report.line'].create(line_data)
