
import asyncio
from const import *

# 序列化
import json

# 解决文件导入问题
import os
import sys
current_path = os.path.abspath(__file__)  # 得到当前文件的绝对路径
top_path = '\\'.join( current_path.split('\\')[:-2] )  # 分割再拼接得到当前文件的根目录
sys.path.append(top_path)  # 将根目录加到系统路径里

from share.const import *
import game
g = game.Game()

async def handle_client(reader, writer):  # 服务器启动之后，客户端链接服务器之后会执行这个函数
    data = await reader.read(MAX_BYTES)  # 接收客户端传来的消息
 
    # 在客户端的asyncClient中使用了encode进行了编码，所以在这要用decode进行解码
    # 在客户端的asyncClient中使用了json.dumps将信息转换为字符流，在这用json.loads还原
    msg = json.loads( data.decode() )  

    # 打印客户端传来的消息
    print(msg) 

    # 定义一个下行消息
    s2cmsg= {}

    # 如果上行消息的type是C2S_ADD_SUNFLOWER，就让下行消息s2cmsg等于服务端的checkAddPlant返回的mgs
    if msg['type'] == C2S_ADD_SUNFLOWER:  
        s2cmsg = g.checkAddPlant( msg['pos'] )

    # 然后执行的操作与客户端的asyncclient.py中的上行消息一样
    # 先用json的dumps函数将数据s2cmsg打包成字符流，再进行编码
    writer.write(json.dumps(s2cmsg).encode()) 
    await writer.drain()


async def main():  # async 表示这个函数要异步等待
    # 系统提供的启动回调的函数，括号里需要提供一个回调函数、一个I、一个端口
    # 先启动一个服务器
    server = await asyncio.start_server(handle_client, '127.0.0.1', SERVER_PORT) 
    print("Server start!Listen on port", SERVER_PORT) 
    
    # 让服务器一直运行
    async with server:
        await server.serve_forever()

asyncio.run( main() )