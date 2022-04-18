from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    eg_account_journal_id = fields.Many2one(comodel_name="eg.account.journal", string="Payment Gateway")
