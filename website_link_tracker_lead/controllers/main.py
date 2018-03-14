# -*- coding: utf-8 -*-
# Copyright 2018 Uakami - Manuel Marquez <buzondemam@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import werkzeug.utils

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import Home


class LinkTrackerLead(Home):

    @http.route(
        '/ltl/<model("link.tracker"):link>/<model("crm.lead"):lead>',
        type='http',
        auth='public')
    def record_link_in_lead(self, link, lead, **kw):
        if link.id not in lead.mapped('link_tracker_ids.id'):
            lead.write({'link_tracker_ids': [(4, link.id)]})
        return werkzeug.utils.redirect(link.short_url)
