{
    'name': 'Odoo email cc',
    'version': '16.0.0.0',
    'summary': 'This module allows to get email_cc from mail',
    'description': '',
    'category': 'Mail',
    'author': 'Raharijaona Brice Ainarivony',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['mail'],
    'data': [],
    'installable': True,
    'auto_install': False,
    'assets':{
        'web.assets_backend': [
            'odoo_email_cc/static/src/js/message.js',
            'odoo_email_cc/static/src/xml/message.xml'
        ]
    }
}