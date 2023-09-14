from whatsapp_api_client_python import API
from googletrans import Translator
from httpcore import SyncHTTPProxy

greenAPI = API.GreenApi(
    "7103853426", "f9ff74d19efe47ce9943cda4e5f16dd816bff01f995140f48f"
)
proxy = SyncHTTPProxy((b'http', b'127.0.0.1', 7890, b''))
translator = Translator(proxies={'all': proxy})

def main():
    # qr = greenAPI.account.qr()
    # print(qr)
    msg = "我在测试微信直接用母语与你沟通的应用程序。"
    esMsg = translator.translate(text=msg, src='zh-cn',dest='es')
    response = greenAPI.sending.sendMessage("8616619710908@c.us", esMsg.text)
    print(response.data)
    

if __name__ == '__main__':
    main()