# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountAbstractPayment(models.AbstractModel):
    _inherit = "account.abstract.payment"

    @api.model
    def default_get(self, fields_list):
        res = super(AccountAbstractPayment, self).default_get(fields_list)
        if "journal_id" in fields_list:
            invoice_id = self.env["account.invoice"].browse(self._context.get("active_id"))
            if invoice_id:
                res[
                    "journal_id"] = invoice_id.eg_account_journal_id and invoice_id.eg_account_journal_id.odoo_account_journal_id.id or None

        return res
