
from odoo import api, fields, models


class Members(models.Model):
    _name = 'members'

    name = fields.Char(string="Nom")
    status = fields.Selection([
        ('none', 'Aucun'),
        ('alive', 'En vie'),
        ('dead', 'Mort')
    ], default='none', string="Status")
    gender = fields.Selection([
        ('male', 'Homme'),
        ('female', 'Femme')
    ], default='female', string="Genre")
    has_photo = fields.Selection([
        ('with', 'Avec Photo'),
        ('without', 'Sans Photo')
    ], default='without', string="Avec / Sans Photo")
    years = fields.Integer(string="Ancienneté", default=0)
    member_group_id = fields.Many2one('members.group', string="Group")
    group_date = fields.Date(string="Date group", related='member_group_id.date')
    _sql_constraints = [
        ('uniq_name_last_name', 'UNIQUE(name)', 'Le nom est déja enregistré')
    ]


