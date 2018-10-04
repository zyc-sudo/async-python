import asyncio


async def msg(text):
    await asyncio.sleep(0.1)
    print(text)
    return text


async def long_operation(i):
    print(i + ' long_operation started')
    await asyncio.sleep(3)
    print(i +'long_operation finished')
    return i

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = []
    t1 = loop.create_task(msg('first'))
    t2 = loop.create_task(long_operation('1'))
    loop.run_until_complete(msg('second'))
    print("finished second")
    #loop.run_until_complete(msg('third'))
    #print("finished all")
    for task in asyncio.Task.all_tasks():
        print(task)
        print(task.done())
        print(task.cancelled())
        if not task.done() and not task.cancelled():
            print("cancelling" )
            task.cancel()
    for task in asyncio.Task.all_tasks():
        print(task)
    #loop.run_until_complete(long_operation('2'))
    print(t1.result())
    print(t2.result())
    #task.append(t)
    #loop.run_until_complete(asyncio.wait(task))
