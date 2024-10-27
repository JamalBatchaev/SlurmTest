import asyncio
import time
from aiohttp import ClientSession, ClientResponseError
 
 
async def fetch_url_data(session, url):
   try:
       async with session.get(url, timeout=60) as response:
           resp = await response.read()
   except Exception as e:
       print(e)
   else:
       return resp
   return
 
 
async def fetch_async(loop, r):
   url = "https://www.yandex.ru"
   tasks = []
   async with ClientSession() as session:
       for i in range(r):
           task = asyncio.ensure_future(fetch_url_data(session, url))
           tasks.append(task)
       responses = await asyncio.gather(*tasks)
   return responses
 
 
if __name__ == '__main__':
   for ntimes in [1, 10, 50, 100, 500]:
       start_time = time.time()
       loop = asyncio.get_event_loop()
       future = asyncio.ensure_future(fetch_async(loop, ntimes))
       # будет выполняться до тех пор, пока не завершится или не возникнет ошибка
       loop.run_until_complete(future)
       responses = future.result()
       print(f'Получено {ntimes} результатов запроса за {time.time() - start_time} секунд')