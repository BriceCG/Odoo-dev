
from odoo import api, fields, models


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def _message_route_process(self, message, message_dict, routes):
        """ Inherit this function to get email_cc from incoming email """
        if message_dict.get('cc'):
            email_cc = message_dict.get('cc')
            # Normalize email_cc
            mail_thread_cc = self.env['mail.thread.cc'].sudo()
            email_cc_normalized = ", ".join(mail_thread_cc._mail_cc_sanitized_raw_dict(email_cc).values())
            if email_cc_normalized:
                # Update context
                context = dict(self.env.context or {})
                context.update({'email_cc': email_cc_normalized})
                self.env.context = context
        thread_id = super(MailThread, self)._message_route_process(message, message_dict, routes)

        return thread_id
