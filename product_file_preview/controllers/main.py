
from odoo import http
from odoo.http import request
import json


class Main(http.Controller):

    @http.route('/get-product-attachment', website=True, type='json', auth='public')
    def get_attachment(self, **kw):
        product_id = kw.get('product_id')
        if product_id:
            attachment = request.env['product.template'].sudo().search_read([('id', '=', product_id)], fields=['attachment'], limit=1)
            return {
                'attachment': attachment[0]['attachment']
            }
        else:
            return {

            }
