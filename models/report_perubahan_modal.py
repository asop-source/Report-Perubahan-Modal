
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



class ReportPerubahanModal(models.Model):
	_name = "report.perubahan.modal"
	
	
	date_start = fields.Date( string="Date start",  help="" ,
								required=True, default=lambda self: time.strftime("%Y-%m-%d"), 
	)
	date_end = fields.Date( string="Date end",  help="",
								required=True, 
								default=lambda self: time.strftime("%Y-%m-%d"),  )
	name = fields.Char( required=True, string="Name",  help="",
	)
	name_report = fields.Selection(
		string='Report Name',
		selection=[('Report Perubahan Modal', 'Report Perubahan Modal')], 
		required=True,
		
	)
	company_id = fields.Many2one(comodel_name="res.company",  string="Company",  help="" , 
	)

	report_ids = fields.One2many('report.perubahan.modal.line','report_id', string="Data Report")



	def cari_nilai1(self):
		# name = self.env['account.move.line'].search([('account_id','=','3120000'),
		# 												  ('date','<=',self.date_start)							
		# 												  ])
		
		sql = """
				select sum(debit - credit) as hasil 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3120000'
				and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil']


	def cari_nilai2(self):

		sql = """
				select sum(debit - credit) as hasil2 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3120000'
				and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil2']


	def cari_nilai3(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3120000'
							and aml.date <= %s
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3120000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 +hasil2

			return total



	def cari_nilai4(self):
		# name = self.env['account.move.line'].search([('account_id','=','3120000'),
		# 												  ('date','<=',self.date_start)							
		# 												  ])
		
		sql = """
				select sum(debit - credit) as hasil4 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3110000'
				and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil4']


	def cari_nilai5(self):

		sql = """
				select sum(debit - credit) as hasil5 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3110000'
				and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil5']


	def cari_nilai6(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3110000'
							and aml.date <= %s
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3110000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 + hasil2

			return total



	def cari_nilai7(self):
		sql = """
				select sum(debit - credit) as hasil7 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3130000'
				and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil7']


	def cari_nilai8(self):

		sql = """
				select sum(debit - credit) as hasil8 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3130000'
				and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil8']


	def cari_nilai9(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3130000'
							and aml.date <= %s
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3130000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 + hasil2

			return total


	def cari_nilai10(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date >= %s and aml.date <= %s
							
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date >= %s and aml.date <= %s
			"""
		cr = self.env.cr
		cr.execute(sql, [self.date_start,  self.date_end,
						 self.date_start,  self.date_end])
		result = cr.dictfetchall()
		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 + hasil2 
			return total


	def cari_nilai11(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date <= %s
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start])
		result = cr.dictfetchall()
		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 + hasil2

			return total


	def cari_nilai12(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date <= %s
				) as hasil2,
				(
				select sum(debit - credit) as hasil3
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date <= %s
				) as hasil3,
				(
				select sum(debit - credit) as hasil4
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date >= %s and aml.date <= %s
				) as hasil4
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil3']) if res['hasil3'] != None else 0
			hasil4 = float(res['hasil4']) if res['hasil4'] != None else 0

			total = hasil1 + hasil2 + hasil3 + hasil4

			return total

	def cari_nilai13(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date >= %s and aml.date <= %s
							
				) as hasil2,
				(
				select sum(debit - credit) as hasil3 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date >= %s and aml.date <= %s
							
				) as hasil3
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date >= %s and aml.date <= %s
			"""
		cr = self.env.cr
		cr.execute(sql, [self.date_start,  self.date_end,
						 self.date_start,  self.date_end,
						 self.date_start,  self.date_end])
		result = cr.dictfetchall()
		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil3']) if res['hasil3'] != None else 0

			total = hasil1 + hasil2 + hasil3
			return total


	def cari_nilai14(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date <= %s
				) as hasil2,
				(
				select sum(debit - credit) as hasil3 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date <= %s
				) as hasil3
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, self.date_start])
		result = cr.dictfetchall()
		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 + hasil2 + hasil3

			return total


	def cari_nilai15(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date <= %s
				) as hasil2,
				(
				select sum(debit - credit) as hasil3
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date <= %s
				) as hasil3,
				(
				select sum(debit - credit) as hasil4
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date <= %s
				) as hasil4,
				(
				select sum(debit - credit) as hasil5
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date >= %s and aml.date <= %s
				) as hasil5,
				(
				select sum(debit - credit) as hasil6
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date >= %s and aml.date <= %s
				) as hasil6
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, 
						 self.date_start,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil3']) if res['hasil3'] != None else 0
			hasil4 = float(res['hasil4']) if res['hasil4'] != None else 0
			hasil5 = float(res['hasil5']) if res['hasil5'] != None else 0
			hasil6 = float(res['hasil6']) if res['hasil6'] != None else 0

			total = hasil1 + hasil2 + hasil3 + hasil4 + hasil5 + hasil6

			return total



	def cari_nilai16(self):
		sql = """
				select sum(debit - credit) as hasil 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3214000'
				and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil']


	def cari_nilai17(self):

		sql = """
				select sum(debit - credit) as hasil2 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3214000'
				and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil2']


	def cari_nilai18(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3214000'
							and aml.date <= %s
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3214000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 +hasil2

			return total



	def cari_nilai19(self):
		sql = """
				select sum(debit - credit) as hasil 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3410000'
				and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil']


	def cari_nilai20(self):

		sql = """
				select sum(debit - credit) as hasil2 
				from account_move_line aml 
				join account_account aa on aml.account_id = aa.id
				where aa.code = '3410000'
				and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start])
		result = cr.dictfetchall()

		for res in result:
			return res['hasil2']


	def cari_nilai21(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3410000'
							and aml.date <= %s
				) as hasil2
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3410000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_start, self.date_end,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0

			total = hasil1 +hasil2

			return total


	def cari_nilai22(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3120000'
							and aml.date >= %s and aml.date <= %s
				) as hasil2,
				(
				select sum(debit - credit) as hasil3 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3110000'
							and aml.date >= %s and aml.date <= %s
				) as hasil3,
				(
				select sum(debit - credit) as hasil4 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3130000'
							and aml.date >= %s and aml.date <= %s
				) as hasil4,
				(
				select sum(debit - credit) as hasil5 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date >= %s and aml.date <= %s
				) as hasil5,
				(
				select sum(debit - credit) as hasil6 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date >= %s and aml.date <= %s
				) as hasil6,
				(
				select sum(debit - credit) as hasil7 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date >= %s and aml.date <= %s
				) as hasil7,
				(
				select sum(debit - credit) as hasil8 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date >= %s and aml.date <= %s
				) as hasil8,
				(
				select sum(debit - credit) as hasil9
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date >= %s and aml.date <= %s
				) as hasil9,
				(
				select sum(debit - credit) as hasil10
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3214000'
							and aml.date >= %s and aml.date <= %s
				) as hasil10
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3410000'
							and aml.date >= %s and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil3']) if res['hasil3'] != None else 0
			hasil4 = float(res['hasil4']) if res['hasil4'] != None else 0
			hasil5 = float(res['hasil5']) if res['hasil5'] != None else 0
			hasil6 = float(res['hasil6']) if res['hasil6'] != None else 0
			hasil7 = float(res['hasil7']) if res['hasil7'] != None else 0
			hasil8 = float(res['hasil8']) if res['hasil8'] != None else 0
			hasil9 = float(res['hasil9']) if res['hasil9'] != None else 0
			hasil10 = float(res['hasil10']) if res['hasil10'] != None else 0

			total = hasil1 + hasil2 + hasil3 + hasil4 + hasil5 + hasil6 + hasil7 +hasil8 + hasil9 + hasil10

			return total


	def cari_nilai24(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3120000'
							and aml.date >= %s and aml.date <= %s
				) as hasil2,
				(
				select sum(debit - credit) as hasil3 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3110000'
							and aml.date >= %s and aml.date <= %s
				) as hasil3,
				(
				select sum(debit - credit) as hasil4 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3130000'
							and aml.date >= %s and aml.date <= %s
				) as hasil4,
				(
				select sum(debit - credit) as hasil5 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date >= %s and aml.date <= %s
				) as hasil5,
				(
				select sum(debit - credit) as hasil6 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date >= %s and aml.date <= %s
				) as hasil6,
				(
				select sum(debit - credit) as hasil7 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date >= %s and aml.date <= %s
				) as hasil7,
				(
				select sum(debit - credit) as hasil8 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date >= %s and aml.date <= %s
				) as hasil8,
				(
				select sum(debit - credit) as hasil9
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date >= %s and aml.date <= %s
				) as hasil9,
				(
				select sum(debit - credit) as hasil10
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3214000'
							and aml.date >= %s and aml.date <= %s
				) as hasil10,
				(
				select sum(debit - credit) as hasil11
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3410000'
							and aml.date >= %s and aml.date <= %s
				) as hasil11,
				(
				select sum(debit - credit) as hasil12 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3120000'
							and aml.date <= %s
				) as hasil12,
				(
				select sum(debit - credit) as hasil13 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3110000'
							and aml.date <= %s
				) as hasil13,
				(
				select sum(debit - credit) as hasil14 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3130000'
							and aml.date <= %s
				) as hasil14,
				(
				select sum(debit - credit) as hasil15 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date <= %s
				) as hasil15,
				(
				select sum(debit - credit) as hasil16 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date <= %s
				) as hasil16,
				(
				select sum(debit - credit) as hasil17 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date <= %s
				) as hasil17,
				(
				select sum(debit - credit) as hasil18 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date <= %s
				) as hasil18,
				(
				select sum(debit - credit) as hasil19
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date <= %s
				) as hasil19,
				(
				select sum(debit - credit) as hasil20
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3214000'
							and aml.date <= %s
				) as hasil20
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3410000'
							and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start, self.date_end,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start,])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil3']) if res['hasil3'] != None else 0
			hasil4 = float(res['hasil4']) if res['hasil4'] != None else 0
			hasil5 = float(res['hasil5']) if res['hasil5'] != None else 0
			hasil6 = float(res['hasil6']) if res['hasil6'] != None else 0
			hasil7 = float(res['hasil7']) if res['hasil7'] != None else 0
			hasil8 = float(res['hasil8']) if res['hasil8'] != None else 0
			hasil9 = float(res['hasil9']) if res['hasil9'] != None else 0
			hasil10 = float(res['hasil10']) if res['hasil10'] != None else 0
			hasil11 = float(res['hasil11']) if res['hasil11'] != None else 0
			hasil12 = float(res['hasil12']) if res['hasil12'] != None else 0
			hasil13 = float(res['hasil13']) if res['hasil13'] != None else 0
			hasil14 = float(res['hasil14']) if res['hasil14'] != None else 0
			hasil15 = float(res['hasil15']) if res['hasil15'] != None else 0
			hasil16 = float(res['hasil16']) if res['hasil16'] != None else 0
			hasil17 = float(res['hasil17']) if res['hasil17'] != None else 0
			hasil18 = float(res['hasil18']) if res['hasil18'] != None else 0
			hasil19 = float(res['hasil19']) if res['hasil19'] != None else 0
			hasil20 = float(res['hasil20']) if res['hasil20'] != None else 0

			total1 = hasil1 + hasil2 + hasil3 + hasil4 + hasil5 + hasil6 + hasil7 +hasil8 + hasil9 + hasil10
			total2 = hasil11 + hasil12 + hasil13 + hasil14 + hasil15 + hasil16 + hasil17 +hasil18 + hasil19 + hasil20
			total_nilai = total2 + total1
			
			return total_nilai


	def cari_nilai23(self):
		sql = """
				select sum(debit - credit) as hasil, 
				(
				select sum(debit - credit) as hasil2 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3120000'
							and aml.date <= %s
				) as hasil2,
				(
				select sum(debit - credit) as hasil3 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3110000'
							and aml.date <= %s
				) as hasil3,
				(
				select sum(debit - credit) as hasil4 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3130000'
							and aml.date <= %s
				) as hasil4,
				(
				select sum(debit - credit) as hasil5 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3310000'
							and aml.date <= %s
				) as hasil5,
				(
				select sum(debit - credit) as hasil6 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3320000'
							and aml.date <= %s
				) as hasil6,
				(
				select sum(debit - credit) as hasil7 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3211000'
							and aml.date <= %s
				) as hasil7,
				(
				select sum(debit - credit) as hasil8 
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3212000'
							and aml.date <= %s
				) as hasil8,
				(
				select sum(debit - credit) as hasil9
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3213000'
							and aml.date <= %s
				) as hasil9,
				(
				select sum(debit - credit) as hasil10
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3214000'
							and aml.date <= %s
				) as hasil10
							from account_move_line aml 
							join account_account aa on aml.account_id = aa.id
							where aa.code = '3410000'
							and aml.date <= %s
			"""

		cr = self.env.cr
		cr.execute(sql, [self.date_start, 
						 self.date_start, 
						 self.date_start, 
						 self.date_start, 
						 self.date_start, 
						 self.date_start, 
						 self.date_start,
						 self.date_start,
						 self.date_start,
						 self.date_start])
		result = cr.dictfetchall()

		for res in result:

			hasil1 = float(res['hasil']) if res['hasil'] != None else 0
			hasil2 = float(res['hasil2']) if res['hasil2'] != None else 0
			hasil3 = float(res['hasil3']) if res['hasil3'] != None else 0
			hasil4 = float(res['hasil4']) if res['hasil4'] != None else 0
			hasil5 = float(res['hasil5']) if res['hasil5'] != None else 0
			hasil6 = float(res['hasil6']) if res['hasil6'] != None else 0
			hasil7 = float(res['hasil7']) if res['hasil7'] != None else 0
			hasil8 = float(res['hasil8']) if res['hasil8'] != None else 0
			hasil9 = float(res['hasil9']) if res['hasil9'] != None else 0
			hasil10 = float(res['hasil10']) if res['hasil10'] != None else 0

			total = hasil1 + hasil2 + hasil3 + hasil4 + hasil5 + hasil6 + hasil7 +hasil8 + hasil9 + hasil10

			return total



	@api.multi
	def generate_master(self):
		if self.name_report == 'Report Perubahan Modal' :
			return self.generate_report()


	@api.multi
	def generate_report(self):

		#delete Doble ID
		sql = "delete from report_perubahan_modal_line where report_id=%s"
		cr = self.env.cr
		cr.execute(sql, (self.id,) )
		compulsory_nilai = []
		master = self.env['report.perubahan.modal.master'].search([])
		for m in master :
			if m.name == "Additional members savings" :
				compulsory_nilai = self.cari_nilai1()
				principal_nilai = self.cari_nilai4()
				voluntary_nilai = self.cari_nilai7()
				donation_nilai = self.cari_nilai10()
				general_nilai = self.cari_nilai13()
				working_nilai = self.cari_nilai16()
				earning_nilai = self.cari_nilai19()
				total_nilai = self.cari_nilai22()
			elif m.name == "Balance as of December 31 2017" :
				compulsory_nilai = self.cari_nilai2()
				principal_nilai = self.cari_nilai5()
				voluntary_nilai = self.cari_nilai8()
				donation_nilai = self.cari_nilai11()
				general_nilai = self.cari_nilai14()
				working_nilai = self.cari_nilai17()
				earning_nilai = self.cari_nilai20()
				total_nilai = self.cari_nilai23()
			elif m.name == "Balance as of Jan 31 2018" :
				compulsory_nilai = self.cari_nilai3()
				principal_nilai = self.cari_nilai6()
				voluntary_nilai = self.cari_nilai9()
				donation_nilai = self.cari_nilai12()
				general_nilai = self.cari_nilai15()
				working_nilai = self.cari_nilai18()
				earning_nilai = self.cari_nilai21()
				total_nilai = self.cari_nilai24()
			else :
				compulsory_nilai = 0
				principal_nilai = 0
				voluntary_nilai = 0
				donation_nilai = 0
				general_nilai = 0
				working_nilai = 0
				earning_nilai = 0
				total_nilai = 0


		#search name
			report_id = {
						'name' : m.name,
						'compulsory': compulsory_nilai,
						'principal' : principal_nilai,
						'voluntary' : voluntary_nilai,
						'donation'	: donation_nilai,
						'general'	: general_nilai,
						'working'	: working_nilai,
						'earning'	: earning_nilai,
						'total'		: total_nilai
						}
		# report_id = [(0,0,
		# 				{
		# 				'name' : x.name,
		# 				'compulsory' : c
		# 				# list comperation
		# 				}) for x in self.env['report.perubahan.modal.master'].search([])
		# 			]
			self.report_ids = [(0,0,report_id)]


	def cell_format(self, workbook):
		cell_format = {}
		cell_format['title'] = workbook.add_format({
			'bold': True,
			'align': 'center',
			'valign': 'vcenter',
			'font_size': 20,
			'font_name': 'Arial',
		})
		cell_format['header'] = workbook.add_format({
			'bold': True,
			'align': 'center',
			'border': True,
			'font_name': 'Arial',
		})
		cell_format['content'] = workbook.add_format({
			'font_size': 11,
			'border': False,
			'font_name': 'Arial',
		})
		cell_format['content_float'] = workbook.add_format({
			'font_size': 11,
			'border': True,
			'num_format': '#,##0.00',
			'font_name': 'Arial',
		})
		cell_format['total'] = workbook.add_format({
			'bold': True,
			'num_format': '#,##0.00',
			'border': True,
			'font_name': 'Arial',
		})
		return cell_format, workbook



#######################################################################################################################################################
###########        ######   #####  #####       #####        ######   #################  ##      #####     ##          ##           ##       ###########
###########  #############   ##   ######  ##########  ############   #################  ##  ##   ###  ##  ##  ######  ##  #######  ##  ####  ##########
###########        #########     #######  ##########        ######   #################  ##  ###   #  ###  ##          ##  #######  ##     #############
###########  ##############  ###  ######  ##########  ############   #################  ##  ####    ####  ##  ##########  #######  ##   #   ###########
###########        ######   #####   ####       #####        ######          ##########  ##  ############  ##  ##########           ##   ###   #########
#######################################################################################################################################################
	

	data = fields.Binary('File')

	@api.multi
	def export_excel(self):
		headers = [
					"No",
					"Description",
					"Compulsory Savings",
					"Principal Savings",
					"Voluntary Saving",
					"Donation",
					"General Reserve",
					"Working Capital Reserve",
					"Earnings (SHU)",
					"Total Equity",
					]

		fp = BytesIO()
		workbook = xlsxwriter.Workbook(fp)
		cell_format, workbook = self.cell_format(workbook)

		if not self.report_ids:
			raise Warning("Data tidak ditemukan. Mohon Generate Report terlebih dahulu")

		worksheet = workbook.add_worksheet()
		worksheet.set_column('A:ZZ', 30)
		column_length = len(headers)

		########## parameters
		worksheet.write(0, 4, "REPORT PERUBAHAN MODAL", cell_format['title'])
		worksheet.write(1, 0, "Tanggal", cell_format['content'])
		worksheet.write(1, 1, self.date_start.strftime("%d-%b-%Y") + ' sampai ' + self.date_end.strftime("%d-%b-%Y"), cell_format['content'])
		worksheet.write(2, 0, "Company", cell_format['content'])
		worksheet.write(2, 1, self.company_id.name , cell_format['content'])

		########### header
		column = 0
		row = 4
		for col in headers:
			worksheet.write(row, column, col, cell_format['header'])
			column += 1

		########### contents
		row = 5
		final_data=[]
		no=1
		for data in self.report_ids :
			final_data.append([
				no,
				data.name,
				data.compulsory,
				data.principal,
				data.voluntary,
				data.donation,
				data.general,
				data.working,
				data.earning,
				data.total,
			])
			no += 1

		for data in final_data:
			column = 0
			for col in data:
				worksheet.write(row, column, col, cell_format['content'] if column<2 else  cell_format['content_float'])
				column += 1
			row += 1

		workbook.close()
		result = base64.encodestring(fp.getvalue())
		filename = self.name_report + '-' + self.company_id.name + '%2Exlsx'
		self.write({'data':result})
		url = "web/content/?model="+self._name+"&id="+str(self.id)+"&field=data&download=true&filename="+filename
		return {
			'type': 'ir.actions.act_url',
			'url': url,
			'target': 'new',
		}
