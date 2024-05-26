
from odoo import api, fields, models


class OdooEmployee(models.Model):
    _name = 'odoo.employee'
    _inherit = ['portal.mixin']

    name = fields.Char(string="Name")
    date_of_birth = fields.Date(string="Date")
    email = fields.Char(string="Email")
    image = fields.Binary(string="Image")
    token = fields.Char(string="Token")
    link = fields.Char(compute='_compute_link')

    def _compute_link(self):
        """ Get link for employee to download pdf report"""
        for employee in self:
            employee.link = employee.generate_link()

    @api.model
    def get_employee_data(self, data):
        """ Get list of employee using JSON RPC """
        if data.get('employee_id'):
            id = int(data.get("employee_id"))
            employee_id = self.search_read([('id', '=', id)], fields=['id', 'email', 'date_of_birth', 'link', 'access_token'])
            return {
                'employee_id': employee_id
            }
        else:
            employee_ids = self.search_read([],
                                           fields=['id', 'email', 'date_of_birth', 'link', 'access_token'])
            return {
                'employee_ids': employee_ids
            }

    def generate_link(self):
        """This function allow to generate link from portal for employee """
        # Generate access token if it is not set
        access_token = self._portal_ensure_token()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return base_url+'/odoo_employee/print?access_token=%s' % (access_token)
