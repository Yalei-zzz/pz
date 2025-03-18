
import asyncio
import const

async def handle_client(reader, weiter):  # 服务器启动之后，客户端链接服务器之后会执行这个函数
    data = await reader.read(const.MAX_BYTES)
    print(data)

async def main():  # async 表示这个函数要异步等待
    # 系统提供的启动回调的函数，括号里需要提供一个回调函数、一个I、一个端口
    # 先启动一个服务器
    server = await asyncio.start_server(handle_client, '127.0.0.1', const.LISTEN_PORT) 
    print("Server start!Listen on port", const.LISTEN_PORT) 
    
    # 让服务器一直运行
    async with server:
        await server.serve_forever()

asyncio.run( main() )