from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MembersGroup(models.Model):
    _name = 'members.group'

    name = fields.Char(string="Nom")

    date = fields.Date(string="Date")
    member_ids = fields.Many2many('members', relation='members_group_member_rel', column1='member_group_id', column2='member_id', string="Members")

    def write(self, vals):
        res = super(MembersGroup, self).write(vals)

        for member_group in self:
            # Remove all groups with this many2many field
            self.env['members'].search([('member_group_id', '=', member_group.id)]).write({'member_group_id': None})
            # Update all group of member
            for member in member_group.member_ids:
                self.env['members'].browse(member.id).write({'member_group_id': member_group.id})
        return res
