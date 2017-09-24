# -*- coding: utf-8 -*-
# Copyright 2016-2017 Pledra
# Copyright 2017 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'Product Configurator Manufacturing Extended',
    'version': '10.0.1.0.0',
    'category': 'Manufacturing',
    'summary': '',
    'author': 'Pledra, Quartile Limited',
    'license': 'LGPL-3',
    'website': 'https://www.odoo-asia.com',
    'depends': [
        'product_configurator_adj',
        'product_configurator_mrp',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/product_attribute_value_set_views.xml',
        'views/product_config_step_line_views.xml',
    ],
    'installable': True,
}
