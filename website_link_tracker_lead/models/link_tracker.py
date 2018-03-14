# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from werkzeug import urls, utils

from odoo import api, fields, models


class LinkTracker(models.Model):
    _inherit = 'link.tracker'

    lead_ids = fields.Many2many(
        'crm.lead',
        relation='link_tracker_lead',
        column1='link_id',
        column2='lead_id',
        string='Leads that clicked the link',
        copy=False
    )
    leads_count = fields.Integer('Leads Counter', compute='_get_leads_count')
    url_tracking_lead = fields.Char(
        'Url Tracking Lead', compute='_get_url_tracking_lead')

    @api.depends('lead_ids')
    def _get_leads_count(self):

        self.leads_count = len(self.lead_ids)

    def _get_url_tracking_lead(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        self.url_tracking_lead = urls.url_join(
            base_url, '/ltl/%(link_id)s/${object.id}' % {'link_id': self.id})

    @api.model
    def convert_links(self, html, vals, blacklist=None):

        if isinstance(blacklist, list):
            blacklist.append('/ltl')
        else:
            blacklist = ['/ltl']

        return super(LinkTracker, self).convert_links(html, vals, blacklist)

    @api.multi
    def action_view_leads(self):
        leads = self.mapped('lead_ids')
        action = self.env.ref(
            'website_link_tracker_lead.crm_link_tracker_lead_action').read()[0]

        if len(leads) > 1:
            action['domain'] = [('id', 'in', leads.ids)]
        elif len(leads) == 1:
            action['views'] = [
                (self.env.ref('crm.crm_case_form_view_oppor').id, 'form')]
            action['res_id'] = leads.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
