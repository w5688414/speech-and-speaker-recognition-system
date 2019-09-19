# -*-coding:utf-8 -*-

from aip import AipSpeech

'''
调用百度语音识别API实现
Author: Hang Hang Li
date: 2019/5/6
'''

def baiduAPI():
	""" 你的 APPID AK SK """
	APP_ID = '9370767'
	API_KEY = '6oOkwS7OOOPIvYxOc0evUUjA'
	SECRET_KEY = 'ec0b95d99a90efb2bdb049bb21763715'

	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

	# 读取文件
	filePath = "latestSpeech/output.wav"
	def get_file_content(filePath):
		with open(filePath, 'rb') as fp:
			return fp.read()

	# 识别本地文件  dev_pid: 1537-普通话(纯中文识别)\	1536-普通话(支持简单的英文识别)\  1936-普通话远场
	result_str = client.asr(get_file_content(filePath), 'wav', 16000, {
	    'dev_pid': 1537,
	})
	print(result_str)
	code = result_str["err_no"]
	if code == 3301:
		return "音频质量过差,请重新录制清晰的音频！"
	elif code == 3308:
	    return "音频过长,音频时长不超过60s!"
	elif code == 0:
		text = result_str["result"][0]
		print("文本：" + text)
		return text
	else:
		return "无法识别，请重新录音！"
