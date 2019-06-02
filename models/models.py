# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OnlineBookshop(models.Model):
     _name = 'online.bookshop'

     book_name = fields.Char(string = "Book Name")
     book_image = fields.Binary(string = "Book Image")

     book_id = fields.Char(string="Book No.", readonly=True, required=True, copy=False, default='New')

     @api.model
     def create(self, vals):
          if vals.get('book_id', 'New') == 'New':
               vals['book_id'] = self.env['ir.sequence'].next_by_code('online.bookshop') or 'New'
          result = super(OnlineBookshop, self).create(vals)
          return result

     # #application_no = fields.Char(string='Application  No', required=True, copy=False, readonly=True,
     #  #                            index=True, default=lambda self: _('New'))
     #
     # @api.model
     # def create(self, vals):
     #    """Overriding the create method and assigning the the sequence for the record"""
     #    if vals.get('book_id', _('New')) == _('New'):
     #        vals['book_id'] = self.env['ir.sequence'].next_by_code('online.bookshop') or _('New')
     #    res = super(OnlineBookshop, self).create(vals)
     #    return res