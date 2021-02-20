# -*- coding: utf-8 -*-
# from odoo import http


# class VsiModule(http.Controller):
#     @http.route('/vsi_module/vsi_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vsi_module/vsi_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vsi_module.listing', {
#             'root': '/vsi_module/vsi_module',
#             'objects': http.request.env['vsi_module.vsi_module'].search([]),
#         })

#     @http.route('/vsi_module/vsi_module/objects/<model("vsi_module.vsi_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vsi_module.object', {
#             'object': obj
#         })
