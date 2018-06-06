# -*- coding: utf-8 -*-
# Copyright 2018 Grant Thornton Spain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MukDmsConfigSettings(models.TransientModel):
    _name = 'muk.dms.config.settings'
    _inherit = 'res.config.settings'

    company_id = fields.Many2one(
        'res.company', string='Company', required=True,
        default=lambda self: self.env.user.company_id)
