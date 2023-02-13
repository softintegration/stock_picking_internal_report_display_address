# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    report_display_address = fields.Boolean(
        string='Report display address', default=False,
        help="If this case is checked,the system will display the source and destination address in report.")

