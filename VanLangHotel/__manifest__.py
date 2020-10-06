{
    'name': 'Văn Lang Hotel',
    'version': '2.3',
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
        'security/VLH_group_user.xml',
        'security/ir.model.access.csv',
        'data/booking_sequence.xml',
        'views/picture.xml',
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
        'wizard/report_booking.xml',
        'report/create_paper_bill.xml',
        'report/return_booking_order.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
