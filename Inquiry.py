import DingTalkBot
import BOCFX
import os
from dotenv import load_dotenv

load_dotenv()

DINGTALKTOKEN = os.environ.get("DINGTALKTOKEN")

TIMERANGE = 6

bot = DingTalkBot.Bot(DINGTALKTOKEN, "中行SGD")
fx = BOCFX.FX(TIMERANGE)

s1 = ""
for i in f"{fx.datemean()}".split("\n")[1:-1]:
    t,p = i.split()
    s1 += t + "    " + p + "\n"

s_div = "----------------------------------\n"
s2 = f"{TIMERANGE+1}日均价: {fx.allmean()}"

bot.send_msg(s1+s_div+s2)
