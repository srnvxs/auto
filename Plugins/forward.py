

import logging
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import channelforward
from config import Config

@channelforward.on_message(filters.channel)
async def forward(client, message):

    try:
        for id in Config.CHANNEL:
            from_channel, to_channel = id.split(":")

            if message.chat.id == int(from_channel):

                if Config.AS_COPY:
                    await message.copy(int(to_channel))
                else:
                    await message.forward(int(to_channel))

                logger.info(f"Forwarded message from {from_channel} to {to_channel}")
                await asyncio.sleep(1)

    except Exception as e:
        logger.exception(e)
