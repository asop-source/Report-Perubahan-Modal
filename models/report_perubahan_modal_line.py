
from odoo import api, fields, models
import time
import datetime
from io import BytesIO
import xlsxwriter
import base64
from datetime import datetime
from odoo.exceptions import Warning
import logging
_logger = logging.getLogger(__name__)

class ReportModal(models.Model):
	_name = 'report.perubahan.modal.line'


	name = fields.Char(string="Description")
	compulsory = fields.Float(string="Compulsory Savings")
	principal = fields.Float(string= "Principal Savings")
	voluntary = fields.Float(string= "Voluntary Saving")
	donation = fields.Float(sring= "Donation")
	general = fields.Float(string= "General Reserve")
	working = fields.Float(string= "Working Capital Reserve")
	earning = fields.Float(string= "Earnings (SHU)")
	total = fields.Float(string= "Total Equity")

	report_id = fields.Many2one('report.perubahan.modal')