{
    'name': 'Product File Preview',
    'version': '16.0.0.0',
    'summary': 'This module allow to add a file on product and preview it on website',
    'description': 'This module use pdfjs to preview pdf file on website',
    'category': 'Website',
    'author': 'RAHARIJAONA Brice Ainarivony',
    'website': '',
    'license': '',
    'depends': ['base', 'website_sale'],
    'data': [
        'views/product_template_views.xml',
        'views/template_client.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'product_file_preview/static/src/js/product_form.js'
        ]
    },
    'installable': True,
    'auto_install': False,
}