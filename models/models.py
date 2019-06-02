# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OnlineBookshop(models.Model):
     _name = 'online.bookshop'
     #_inherit = ['product.template']

     book_name = fields.Char(string = "Book Name")
     book_name_b = fields.Char(string = "Book Name in Bangla")
     book_image = fields.Binary(string = "Book Image")

     book_id = fields.Char(string="Book No.", readonly=True, required=True, copy=False, default='New')

     @api.model
     def create(self, vals):
          if vals.get('book_id', 'New') == 'New':
               vals['book_id'] = self.env['ir.sequence'].next_by_code('online.bookshop') or 'New'
          result = super(OnlineBookshop, self).create(vals)
          return result

