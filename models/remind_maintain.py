
class RemindMaintain(models.Model):
    _name = 'remind.maintain'
    _rec_name = 'name'
    _order = 'time_reminder desc, create_date desc'

    recipient_ids = fields.Many2many('res.partner', string='Recipient')
    parner_id = fields.Many2one('res.partner' string='Khách Hàng')
    partner_phone = fields.Char(String='số điện thoại')
    time_reminder = fields.Datetime(string='Thời gian nhắc lịch', required=True)
    flag_send = fields.Boolean(default=False)
