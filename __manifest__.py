# -*- coding: utf-8 -*-
{
    'name': "Abono a proxima factura",

    'summary': """
        Este modulo agrega un campo en la vista de la factura y en el documento impreso""",

    'description': """
        Este modulo agrega un campo en la vista de la factura y en el documento impreso
        que contiene el credito disponible del cliente como abono a proximo mes
    """,

    'author': "Juan Garcia | Root Systemte Technology ",
    'website': "http://www.rootsystemtechnology.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',
    'license': 'GPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_invoice.xml',
        'views/account_invoice_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
