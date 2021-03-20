# -*- coding: utf-8 -*-
{
    'name': "Scheduled_reminders",
    'summary': """Scheduled reminders model""",
    'description': """Managing car information""",
    'author': "nguyennha",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/scheduled_reminders_views.xml',
        'views/cron_remind.xml',
        'views/template_mail_noti.xml',
        'data/cron_remind.xml',
        'data/template_mail_noti.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}