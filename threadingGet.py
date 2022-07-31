import requests, time
from threading import Thread

TEST_URL = 'https://www.baidu.com'
THREADS = 20
TIMEOUT = 20

errorCount = 0
successCount = 0

class getTask:
    def run(self):
        try:
            response = requests.get(TEST_URL).content
            responses.append(response)
        except (requests.exceptions.ConnectionError, ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionResetError):
            global errorCount
            errorCount += 1
        else:
            global successCount
            successCount += 1
        return

if __name__ == '__main__':
    responses = []
    # count = 0
    rounds = 0
    while True:
        rounds += 1
        # count += THREADS
        tasks = []
        pool = []
        for i in range(THREADS):
            tasks.append(getTask())
            pool.append(Thread(target=tasks[i].run))
        for each in pool:
            each.start()
        time.sleep(TIMEOUT)
        if responses:
            break
        else:
            print('Timeout exceeded. Restarting threads...')
    print(f'Success.\n{successCount} success(es), {errorCount} error(s), {rounds} round(s).\n----------')
    for i, each in enumerate(responses):
        with open(f'response_{i+1}.out', 'wb') as fil:
            fil.write(each)
    print('Finished writing files.\nYou can wait for redundant threads to stop or force-terminate by pressing Ctrl+C...\n----------')

