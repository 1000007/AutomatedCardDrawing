# from receive import rev_msg
from send_message.send_message import send_message
from massage_flide import msg_talker
import websocket, time, json, logging

talker = msg_talker()
print("欢迎您，自助扭蛋机的管理者。")

ws_url = "ws://127.0.0.1:6700/ws"
logging.basicConfig(level=logging.DEBUG, format='[void] %(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def recv_msg(_, message):
    try:
        rev = json.loads(message)
        if rev == None:
            return False
        else:
            if rev["post_type"] == "message":
                # print(rev) #需要功能自己DIY
                if rev["message_type"] == "private":  #私聊
                    talker.private_msg(rev, ws)
                elif rev["message_type"] == "group":  #群聊
                    talker.group_msg(rev, ws)
                else:
                    pass
            elif rev["post_type"] == "notice":
                    pass
            else:
                pass
    except Exception as e:
        print(e)
        return False
    


if __name__ == '__main__':

    ws = websocket.WebSocketApp(
        ws_url,
        on_message=recv_msg,
        on_open=lambda _: logger.debug('连接成功......'),
        on_close=lambda _: logger.debug('重连中......'),
    )
    while True:
        ws.run_forever()
        time.sleep(5)