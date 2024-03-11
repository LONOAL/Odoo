
from odoo import models, fields, api

class opentop(models.Model):
    _name = 'opentop'
    _description = 'openacademy.openacademy'

    name = fields.Char(string="Nome", required=True)
    description = fields.Text(string="Factous")
    elo = fields.Integer(string="Tercero del mundooo")
