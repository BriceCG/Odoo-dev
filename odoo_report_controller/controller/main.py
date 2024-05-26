
from odoo import http
from odoo.http import request


class OdooController(http.Controller):

    @http.route('/odoo_employee/print', auth='none', type='http', csrf=False)
    def export_pdf(self, access_token=None):
        """ This function allows to download pdf version of report """
        if not access_token:
            return request.redirect('/')
        employee = request.env['odoo.employee'].sudo().search_read([('access_token', '=', access_token)], limit=1)
        if employee:
            employee = employee[0]
            pdf = request.env['ir.actions.report'].sudo()._render_qweb_pdf('odoo_report_controller.odoo_employee_report', [employee['id']])[0]
            pdfhttpheaders = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf)),
            ]
            return request.make_response(pdf, headers=pdfhttpheaders)
        else:
            return request.redirect('/')