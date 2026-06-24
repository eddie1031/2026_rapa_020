import asyncio

async def worker(name, delay):
    print(f'{name}: 작업 시작')
    await asyncio.sleep(delay)
    print(f'{name}: 작업 종료')
    return f'worker_{name}의 결과물'

async def main():
    # await worker('작업자1', 2)
    # await worker('작업자2', 1)

    task1 = asyncio.create_task(worker('작업자1', 2))
    task2 = asyncio.create_task(worker('작업자2', 1))

    print(type(task1))

    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())
