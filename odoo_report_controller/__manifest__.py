{
    'name': 'Odoo Report Controller',
    'version': '1.0.0.0',
    'summary': 'Create a new report and allow to download it from website',
    'description': """This module allows to :
                - Define new model call odoo_employee
                - Add a new route on websit to allows download
                """,
    'category': '',
    'author': '',
    'website': '',
    'license': '',
    'depends': ['base', 'portal', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'report/odoo_employee_report.xml',
        'views/odoo_employee_views.xml'
    ],
    'installable': True,
    'auto_install': False,
}