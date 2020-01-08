# -*- coding: utf-8 -*-
from odoo import http

# class VitCoaBudgetary(http.Controller):
#     @http.route('/vit_coa_budgetary/vit_coa_budgetary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_coa_budgetary/vit_coa_budgetary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_coa_budgetary.listing', {
#             'root': '/vit_coa_budgetary/vit_coa_budgetary',
#             'objects': http.request.env['vit_coa_budgetary.vit_coa_budgetary'].search([]),
#         })

#     @http.route('/vit_coa_budgetary/vit_coa_budgetary/objects/<model("vit_coa_budgetary.vit_coa_budgetary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_coa_budgetary.object', {
#             'object': obj
#         })