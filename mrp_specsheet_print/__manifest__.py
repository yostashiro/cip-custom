# -*- coding: utf-8 -*-
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Specsheet Print",
    "summary": "",
    "version": "10.0.1.0.0",
    "category": "Reporting",
    "website": "https://www.quartile.co/",
    "author": "Quartile Limited",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "sale_order_line_mrp_remarks",
        "report_xlsx",
    ],
    "data": [
        "wizards/specsheet_report_wizard_view.xml",
        "reports.xml",
    ],
}
