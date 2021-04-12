import asyncio

async def make_americano():
    print("Americano Start")
    await asyncio.sleep(3)
    print("Americano End")

async def make_latte():
    print("Latte Start")
    await asyncio.sleep(5)
    print("Latte End")

async def main():
    coro1 = make_americano() #비동기
    coro2 = make_latte() #비동기
    await asyncio.gather(
        coro1,
        coro2
    )

print("Main Start") # 동기
asyncio.run(main()) # 안에 내용 비동기
print("Main End") # 동기