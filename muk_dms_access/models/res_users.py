# -*- coding: utf-8 -*-
# Copyright 2017 Grant Thornton Spain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        res = super(ResUsers, self).create(vals)
        access_group_pool = self.env['muk_dms_access.groups']
        default_group = access_group_pool.search([
            ('default_group_for_users', '=', True)
        ])
        if default_group:
            default_group.update({
                'additional_users': (4, res.id),
                'users': (4, res.id)
            })
        return res
