from pyrogram import filters
from pyrogram.types import Message

from StringGen import Alone
from StringGen.utils import add_served_user, keyboard


@Alone.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Alone.mention},\nAɴ ꜱᴀʙᴍɪʟᴋᴇ ᴀᴡᴀᴊᴇɴɴɪᴋᴀʟᴏ ꜱᴛʀɪɴɢ ᴋᴇ ʟɪʏᴇ ᴍᴇʀɪ ᴊᴀɴᴀ.",
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
