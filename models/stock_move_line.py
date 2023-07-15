# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _get_aggregated_product_quantities(self, **kwargs):
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for key,aggr_move_line in aggregated_move_lines.items():
            product_id = key.split("_")[0]
            move_line = self.filtered(lambda ml:ml.product_id.id == int(product_id))
            aggr_move_line.update({'display_product_name_history':move_line[0].picking_type_id.display_product_name_history,
                                   })
        return aggregated_move_lines
