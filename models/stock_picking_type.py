# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    display_product_name_history = fields.Boolean(
        string='Display products name changes history', default=False,
        help="If this case is checked,the system will display the history of changes of the product name in moves.")

