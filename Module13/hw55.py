import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    participants = [
        ('Pasha', 3),
        ('Denis', 4),
        ('Appolon', 5)
    ]
    tasks = [start_strongman(name, power) for name, power in participants]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(start_tournament())
