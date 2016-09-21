# coding: utf-8

import os
import xlwt
from lemon.ras_type import *

__author__ = 'chengchaojie'


class SimpleXlwt:
	def __init__(self, value_filter=None, file_path=None):
		self.file_path = file_path

		self.value_filter = value_filter

		self.sheet_list = {}

		self.work_book = xlwt.Workbook()
		self.current_sheet = None
		self.current_sheet_name = None
		self.current_row = 0

	def set_data_filter(self, value_filter):
			self.value_filter = value_filter

	def add_sheet(self, sheet_name, overwrite=True):
		if isinstance(sheet_name, str) or isinstance(sheet_name, unicode):
			self.current_sheet_name = sheet_name
			self.current_sheet = self.work_book.add_sheet(sheet_name, overwrite)
			self.current_row = 0
			self.sheet_list[sheet_name] = {"fp": self.current_sheet, "row": 0}

			return self.current_sheet

		return None

	def get_sheet(self, sheet_name=None):
		if isinstance(sheet_name, str):
			sheet = self.sheet_list.get(sheet_name)
			if sheet is not None:
				self.current_sheet = sheet["fp"]
				self.current_sheet_name = sheet_name
				self.current_row = sheet["row"]

		return self.current_sheet

	def add_row_count(self, sheet_name, length):
		self.sheet_list[sheet_name]["row"] += length
		self.current_row += length

	def write_header(self, header, row=0, fp=None):
		fp = self.get_sheet(fp)
		for colx, value in enumerate(header):
			fp.write(row, colx, value)

		self.add_row_count(self.current_sheet_name, 1)

	def write_date(self, date, boolean_field=None, fp=None):
		# if not isinstance(date, list) or not isinstance(date, tuple):
		# 	return None

		fp = self.get_sheet(fp)
		for row in date:
			for colx, value in enumerate(row):
				if self.value_filter is not None:
					value = self.value_filter.exchange(colx, value)

				fp.write(self.current_row, colx, value)
			self.current_row += 1

		self.sheet_list[self.current_sheet_name]["row"] = self.current_row

	def write_column_date(self, date, rn=1, cn=0, fp=None):
		# if not isinstance(date, list) or not isinstance(date, tuple):
		# 	return None

		fp = self.get_sheet(fp)
		for value in date:
			fp.write(rn, cn, value)
			rn += 1

	def save_xls(self, file_path):
		if file_path is None and self.file_path is None and not isinstance(file_path, None):
			return False

		self.file_path = file_path
		self.work_book.save(self.file_path)



