import telebot
import schedule
import time
from license_check import jira_license_info, conf_license_info

tb = telebot.TeleBot('{{ BOT_TOKEN }}')
chat_id = '{{ CHAT_ID }}'


def jira_license_check():
    text_jira = "There are %d Jira licenses left" % jira_license_info()
    return tb.send_message(chat_id, text_jira)


def conf_license_check():
    text_conf = "There are %d Confluence licenses left" % conf_license_info()
    return tb.send_message(chat_id, text_conf)


def try_jira():
    try:
        jira_license_check()
    except TypeError:
        pass


def try_conf():
    try:
        conf_license_check()
    except TypeError:
        pass


schedule.every(12).hours.do(try_jira)
schedule.every(12).hours.do(try_conf)

while True:
    schedule.run_pending()
    time.sleep(1)
