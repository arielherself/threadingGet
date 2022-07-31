import asyncio, aiohttp, datetime, os

TEST_URL = 'https://www.naixisubs.com'
THREADS = 20
TIMEOUT = 20

successCount = 0
errorCount = 0

async def waiter():
    global successCount, errorCount
    while True:
        await asyncio.sleep(3)
        print(f'[{datetime.datetime.now().isoformat()}] Checking progress...')
        if successCount != 0:
            print(f'[{datetime.datetime.now().isoformat()}] {successCount} success(es), {errorCount} error(s).')
            os._exit(0)
    

async def get(taskId: int):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(TEST_URL, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'}) as response:
                responseContent = await response.content.read()
        with open(f'response_{taskId}.out', 'wb') as fil:
            fil.write(responseContent)
    except:
        global errorCount
        errorCount += 1
    else:
        global successCount
        successCount += 1
    return

async def main():
    taskCount = 0
    index = 0
    pool = []
    while True:
        print(f'[{datetime.datetime.now().isoformat()}] Adding threads #{index+1}-{index+THREADS}')
        taskCount += THREADS
        pool.extend([asyncio.create_task(get(i+1)) for i in range(index, index+THREADS)])
        await asyncio.wait(pool+[asyncio.create_task(waiter())])
        await asyncio.sleep(TIMEOUT)
        index += THREADS

asyncio.run(main())
