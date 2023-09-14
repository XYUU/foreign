from whatsapp_chatbot_python import GreenAPIBot, Notification
from googletrans import Translator
from httpcore import SyncHTTPProxy

bot = GreenAPIBot(
    "7103853426", "f9ff74d19efe47ce9943cda4e5f16dd816bff01f995140f48f"
)
proxy = SyncHTTPProxy((b'http', b'127.0.0.1', 7890, b''))
translator = Translator(proxies={'all': proxy})

@bot.router.message()
def message_handler(notification: Notification) -> None:
    print(notification.message_text)
    str = translator.translate(notification.message_text,src='es', dest='zh-cn')
    print(str.text)
    # notification.answer("Hello")

bot.run_forever()