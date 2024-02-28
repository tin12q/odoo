from odoo import models, fields, api

class Hospital(models.Model):
    _name = 'hospital.client'
    _description = 'Hospital Client'
    name = fields.Char(string='Name', required=True)
    region = fields.Char(string='Region', required=True)
    address = fields.Text(string='Address', required=True)
    representative_name = fields.Char(string='Representative', required=True)
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email', required=True)

