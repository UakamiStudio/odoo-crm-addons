# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Link Leads with Links Tracked',
    'version': '11.0.1.0.1',
    'category': 'Marketing',
    'author': 'Uakami',
    'website': "https://uakami.com/",
    'license': 'AGPL-3',
    'depends': [
        'link_tracker',
        'crm',
        'website',
    ],
    'data': [
        'views/link_tracker_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
