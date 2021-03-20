from odoo import api, fields, models
from datetime import datetime

class ScheduledReminders(model.Model):
    _name = "Scheduled Reminders"
    _description = "Scheduled Reminders Model"

    Descreption = fields.Char('Mô tả', required=True)
    name = fields.Char('Tên')
    address = fields.Char('địa chỉ')
    owner_id = fields.Many2one('res.partner', string='Owner')
    age = fields.Integer('Age', default=1)


    @api.model
    def send_email_maintain_reminder(self):
        datetime_now = datetime.datetime.utcnow()
        exist_record = self.env['remind.maintain'].search(
            ['&', '|', ('time_reminder', '>=', datetime_now.strftime('%Y-%m-%d %H:%M:%S')),
             ('time_reminder', '<=', (datetime_now + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')),
             ('flag_send', '=', False)])
        for record in exist_record:
