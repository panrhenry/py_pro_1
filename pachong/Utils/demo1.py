import asyncio, graia.scheduler
from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication, Session
from graia.application.friend import Friend
from graia.application.message.chain import MessageChain
from graia.application.message.elements.internal import Plain

loop = asyncio.get_event_loop()
bcc = Broadcast(loop = loop)
app = GraiaMiraiApplication(broadcast = bcc,
                            connect_info = Session(host = 'http://localhost:60', # 填入httpapi服务运行的地址
                                                authKey = '123123123', # 填入authKey
                                                account = 1292687393, #你的机器人的qq号
                                                #Graia已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
                                                websocket = True
                                                )
                            )
#处理群消息
@bcc.receiver("FriendMessage")
async def friend_message_listener(app: GraiaMiraiApplication,
                                friend: Friend,):
    await app.sendFriendMessage(friend, MessageChain.create([Plain('hello world!')]))

app.launch_blocking()
