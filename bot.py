# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(lineno)d - %(module)s - %(levelname)s - %(message)s"
)
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# ❌ REMOVE uvloop (it breaks Pyrogram sync mode on Python 3.11)
# import uvloop
# uvloop.install()

import asyncio
from pyrogram import Client, idle
from config import Config


class ChannelForward(Client, Config):
    def __init__(self):
        super().__init__(
            name="CHANNELFORWARD",
            bot_token=self.BOT_TOKEN,
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            workers=20,
            plugins={"root": "Plugins"}
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"New session started for {me.first_name} (@{me.username})")

    async def stop(self):
        await super().stop()
        print("Session stopped. Bye!!")


async def main():
    app = ChannelForward()
    await app.start()
    await idle()      # keeps bot running
    await app.stop()


if __name__ == "__main__":
    asyncio.run(main())
