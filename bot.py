import asyncio

from app import tg


async def main():

    await tg.initialize()

    await tg.start()

    await tg.updater.start_polling()

    print("✅ BOT ONLINE")

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
