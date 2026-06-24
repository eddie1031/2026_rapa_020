import asyncio

async def say_after(delay, message):
    await asyncio.sleep(delay)
    print(message)

async def main():
    await asyncio.gather(
        say_after(1, "1초 뒤 출력"),
        say_after(2, "2초 뒤 출력"),
        say_after(3, "3초 뒤 출력"),
    )

if __name__ == '__main__':
    asyncio.run(main())
