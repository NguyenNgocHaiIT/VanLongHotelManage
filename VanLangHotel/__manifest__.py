{
    'name': 'Văn Lang Hotel',
    'version': '1.1',
    'category': 'Manager',
    'sequence': 1,
    'summary': "This module provides tasks related to hotel management",
    'description': "This module provides tasks related to hotel management",
    'author': "Nguyen Ngoc Hai, Nguyen Viet Tu, Duong Trung Hieu",
    'website': '',
    'depends': [
        'base',

    ],
    'data': [
        'views/menu_action.xml',
        'views/promotion.xml',
        'views/employee_view.xml',
        'views/customer_view.xml',
        'views/room_view.xml',
        'views/booking.xml',
        'views/service.xml',
        'data/promotion_data_default.xml',
        'data/service_data_default.xml',
        'data/employee_data_default.xml',
        'data/customer_data_default.xml',
        'data/room_data_default.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
