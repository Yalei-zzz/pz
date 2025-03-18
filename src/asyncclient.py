
import asyncio
import json
from const import *

class AsyncClient(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    # 客户端向服务端发送消息c2s()
    async def c2s(self, message): 
        # 连接服务器
        # await表示协程，只要没有连接完成就不会往下执行其他代码
        reader,writer = await asyncio.open_connection(self.ip, self.port)  

        # 先用json的dumps函数将数据message打包成字符流，再转换为编码
        data = json.dumps(message).encode()  

        # 写进缓冲区
        writer.write(data)
        await writer.drain()
