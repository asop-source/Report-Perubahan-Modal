# -*- coding: utf-8 -*-
{
    'name': "Vit Report Perubahan Modal",

    'summary': """
        
        Laporan Perubahan Modal


        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "asopkarawang@gmail.com",
    'website': "http://www.vitraining.com",
    "images": ["static/Picture/icon.png"],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Report',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','om_account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/report_perubahan_modal.xml',
        'data/report.perubahan.modal.csv',
        'data/report.perubahan.modal.master.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}