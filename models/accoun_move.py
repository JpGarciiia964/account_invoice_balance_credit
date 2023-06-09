from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    abono_proxima_factura = fields.Monetary(string='Abono Próximo Mes', compute='_compute_abono_proxima_factura')

    @api.depends('partner_id')
    def _compute_abono_proxima_factura(self):
        for move in self:
            if move.move_type in ['out_invoice', 'out_refund'] and move.partner_id:
                lines = self.env['account.move.line'].search([
                    ('partner_id', '=', move.partner_id.id),
                    ('reconciled', '=', False)
                ])
                credit_total = sum(lines.mapped('credit'))
                total_parcial = move.amount_total - credit_total
                total_parcial_n = move.amount_total + total_parcial
                move.abono_proxima_factura = abs(total_parcial_n)
            else:
                move.abono_proxima_factura = 0
