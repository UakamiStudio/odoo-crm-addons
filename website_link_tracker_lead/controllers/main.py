# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import werkzeug.utils

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home


class LinkTrackerLead(Home):

    @http.route('/ltl/<int:link_id>/<int:lead_id>', type='http', auth='public')
    def record_link_in_lead(self, link_id, lead_id, **kw):
        lead = request.env['crm.lead'].sudo().browse(lead_id)
        link = request.env['link.tracker'].sudo().browse(link_id)
        if link_id not in lead.mapped('link_tracker_ids.id'):
            lead.write({'link_tracker_ids': [(4, link_id)]})
        return werkzeug.utils.redirect(link.short_url)
