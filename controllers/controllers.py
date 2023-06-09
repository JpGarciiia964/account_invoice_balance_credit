# -*- coding: utf-8 -*-
# from odoo import http


# class AccountInvoiceBalanceCredit(http.Controller):
#     @http.route('/account_invoice_balance_credit/account_invoice_balance_credit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_invoice_balance_credit/account_invoice_balance_credit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_invoice_balance_credit.listing', {
#             'root': '/account_invoice_balance_credit/account_invoice_balance_credit',
#             'objects': http.request.env['account_invoice_balance_credit.account_invoice_balance_credit'].search([]),
#         })

#     @http.route('/account_invoice_balance_credit/account_invoice_balance_credit/objects/<model("account_invoice_balance_credit.account_invoice_balance_credit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_invoice_balance_credit.object', {
#             'object': obj
#         })
