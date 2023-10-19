{
    'name': 'Create account bank statement',
    'version': '16.0.1.0.0',
    'license': 'OPL-1',
    'category': 'Extra Addons',

    'summary': """
        An extension module that allows create new lines in account.bank.statement form view
    """,
    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'depends': [
        'account'
    ],

    'data': [
        'views/allow_create_statement_views.xml',
        'views/account_bank_statement_views.xml',
        'views/allow_create_statement_line_views.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],

    'installable': True,
    'price': 0,
    'currency': 'EUR',
}