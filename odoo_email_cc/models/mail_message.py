
from odoo import api, fields, models


class MailMessage(models.Model):
    _inherit = 'mail.message'

    email_cc = fields.Char(string="Email cc")

    @api.model
    def create(self, vals):
        message = super(MailMessage, self).create(vals)
        if self.env.context.get('email_cc'):
            message.email_cc = self.env.context.get('email_cc')
        return message
