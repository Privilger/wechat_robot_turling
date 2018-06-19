#人工智障以完成~~~

from ShowapiRequest import ShowapiRequest
import json
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

    r = ShowapiRequest("http://route.showapi.com/60-27",
                       "67709", "f75a882b857f468f9076ddc9c53e326e")
    r.addBodyPara("info", msg.text)
    r.addBodyPara("userid", "userid")

    res = r.post()
    j = json.loads(res.text)
    print(j['showapi_res_body']['text'])  # 返回信息
    return j['showapi_res_body']['text']

itchat.auto_login()
itchat.run()
