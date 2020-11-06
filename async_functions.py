import asyncio
import aiohttp

urls = ['https://github.com/igortereshchenko/threading/blob/master/thread.py',
        'https://docs.sqlalchemy.org/en/13/orm/cascades.html',
        'https://www.kaggle.com/stackoverflow/stackoverflow?select=tags'
        ]

async def get_info(ulr):
    async with aiohttp.ClientSession() as session:
        async with session.get(ulr) as response:

            print(ulr, "is parsing")

            data = await response.text()

            print(len(data) , "is loaded")


containers = [get_info(ulr) for ulr in urls]

loop = asyncio.get_event_loop()
loop.run_until_complete( asyncio.wait(containers) )
print('Finish')

# SIMPLE EXAMPLE

# async def any_function():
#     pass
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete( any_function() )
# loop.close()