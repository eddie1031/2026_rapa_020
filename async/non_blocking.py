import asyncio

async def cook_ramen():
    print('라면 물 끓이기 시작')

    await asyncio.sleep(3)

    print('보글보글')

async def main():
    print('요리 시작')

    task = asyncio.create_task(cook_ramen())

    print('다른작업 수행!')

    await task

    print('모든작업이 종료되었습니다.')

if __name__ == '__main__':
    asyncio.run(main())
