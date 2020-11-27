from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings


def send(message, at_mobiles=[]):
    webhook = settings.DING_WEB_HOOK

    ding = DingtalkChatbot(webhook=webhook)

    ding.send_text(msg=('面试通知：%s' % message), at_mobiles=at_mobiles)
