# coding: utf-8
import datetime
import os
import shutil

__author__ = 'chengchaojie'


def verify_key_value(json_obj, key_list, verify_value=True):

	if json_obj is None:
		return False

	if verify_value:
		for key in key_list:
			if key not in json_obj or json_obj.get(key) is None:
				return False

	else:
		for key in key_list:
			if key not in json_obj:
				return False

	return True


def acquire_session_value(request, session_field, attribute):

	return 9

	# session_obj = request.session[session_field]
	#
	# if session_obj is not None:
	# 	return getattr(object, attribute)
	# else:
	# 	return None


def check_store_path(store_path):
	now = datetime.datetime.now()

	month_day = "%s-%s/%s" % (now.year, now.month, now.day)
	today_dir = os.path.join(store_path, month_day)
	if not os.path.exists(today_dir):
		os.makedirs(today_dir)

	return today_dir


def copy_file_to_store(attachment):

	shutil.copyfile(attachment.get("src"), attachment.get("store_src"))
	shutil.copyfile(attachment.get("pdf"), attachment.get("store_pdf"))
	shutil.copyfile(attachment.get("profile"), attachment.get("store_profile"))
