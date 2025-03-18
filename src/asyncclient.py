
import asyncio
import json
from const import *
from share.const import *

class AsyncClient(object):
    def __init__(self, game, ip, port):
        self.game= game  # 把游戏逻辑也传进
        self.ip = ip
        self.port = port

    # 客户端向服务端发送消息c2s()
    async def c2s(self, message): 
        # 连接服务器
        # await表示协程，只要没有连接完成就不会往下执行其他代码
        reader,writer = await asyncio.open_connection(self.ip, self.port)  

        # 先用json的dumps函数将数据message打包成字符流，再进行编码
        data = json.dumps(message).encode()  # encode执行编码

        # 写进缓冲区
        writer.write(data)
        await writer.drain()

        # 等待服务端返回消息给message
        message = await reader.read(MAX_BYTES)

        # 解码再解包
        msg = json.loads(message.decode())
        print( msg )
        if msg['type'] == S2C_ADD_SUNFLOWER:
            self.game.checkAddPlant(msg['pos'], SUNFLOWER_ID)

