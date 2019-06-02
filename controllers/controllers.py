# -*- coding: utf-8 -*-
from odoo import http

# class OnlineBookshop(http.Controller):
#     @http.route('/online_bookshop/online_bookshop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/online_bookshop/online_bookshop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('online_bookshop.listing', {
#             'root': '/online_bookshop/online_bookshop',
#             'objects': http.request.env['online_bookshop.online_bookshop'].search([]),
#         })

#     @http.route('/online_bookshop/online_bookshop/objects/<model("online_bookshop.online_bookshop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('online_bookshop.object', {
#             'object': obj
#         })