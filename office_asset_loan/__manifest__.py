{
    'name': 'Office Asset Loan',
    'version': '19.0.1.0.0',
    'summary': 'Catat inventaris kantor dan peminjamannya',
    'category': 'Tools',
    'author': 'Nama Lengkap Anda',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/office_asset_loan_sequence.xml',
        'views/office_asset_views.xml',
        'views/office_asset_loan_views.xml',
        'views/office_asset_menus.xml',
    ],
    'application': True,
    'installable': True,
}
