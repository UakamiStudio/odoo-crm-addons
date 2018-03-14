# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    link_tracker_ids = fields.Many2many(
        'link.tracker',
        relation='link_tracker_lead',
        column1='lead_id',
        column2='link_id',
        string='Clicked Tracking Links',
        copy=False)
