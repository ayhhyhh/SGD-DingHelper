import requests


class Bot():
    def __init__(self, token, keyword):
        assert token, "DingTalkToken not provided"
        self.token = token
        self.keyword = keyword
        self.url = f"https://oapi.dingtalk.com/robot/send?access_token={self.token}"

    def make_json(self, msg):
        post_json = {
            "msgtype": 'text',
            "text": {
                "content": f"{self.keyword}\n{msg}",
            },
        }
        return post_json

    def send_msg(self, msg):
        res = requests.post(
            url=self.url, json=self.make_json(msg))
        if res.status_code == 200:
            print("DingTalk Message Sending Success!")
        else:
            print("Message Sending Failure")
