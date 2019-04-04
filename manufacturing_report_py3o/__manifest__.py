# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Manufacturing Report Py3o',
    'version': '10.0.1.0.0',
    'category': 'Manufacturing',
    'license': 'AGPL-3',
    'summary': 'Sample py3o manufacturing report',
    'description': """
Manufacturing Report Py3o
===================

This module adds a sample py3o manufacturing report.

    """,
    'author': 'Akretion, Quartile Limited',
    'depends': [
        'report_py3o',
        'mrp',
        ],
    'data': ['report.xml'],
    'installable': True,
}
