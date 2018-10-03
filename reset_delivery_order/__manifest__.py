# -*- coding: utf-8 -*-
# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Reset Delivery Order",
    'summary': """
        You can reset the delivery order.""",
    'description': """
        You can only reset the delivery order from
        sales which have not been cancelled.
    """,
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'license': 'AGPL-3',
    'category': 'Sale',
    'version': '10.0.1.0.0',
    'data': [
        'views/stock_picking_view.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'depends': ['sale', 'stock']
}
