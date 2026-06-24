import asyncio

async def task_a():
    print("Task A 시작")
    await asyncio.sleep(5) # 이 순간에 이벤트 루프가 Task B를 실행
    print("Task A 종료")

async def task_b():
    print("Task B 시작")
    await asyncio.sleep(1) # 이 순간에 이벤트 루프가 다른 task를 실행
    print("Task B 종료")

async def main():
    await asyncio.gather(task_a(), task_b())


if __name__ == "__main__":
    asyncio.run(main())