
import asyncio
from FileStream.bot import FileStream, multi_clients
from FileStream.utils.bot_utils import is_user_banned, is_user_exist, is_user_joined, gen_link, is_channel_banned, is_channel_exist, is_user_authorized
from FileStream.utils.database import Database
from FileStream.utils.file_properties import get_file_ids, get_file_info
from FileStream.config import Telegram
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums.parse_mode import ParseMode
db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

@FileStream.on_message(
    filters.private
    & (
            filters.document
            | filters.video
            | filters.video_note
            | filters.audio
            | filters.voice
            | filters.animation
            | filters.photo
    ),
    group=4,
)
async def private_receive_handler(bot: Client, message: Message):
    if not await is_user_authorized(message):
        return
    if await is_user_banned(message):
        return

    await is_user_exist(bot, message)
    if Telegram.FORCE_SUB:
        if not await is_user_joined(bot, message):
            return
    try:
        inserted_id = await db.add_file(get_file_info(message))
        await get_file_ids(False, inserted_id, multi_clients, message)
        reply_markup, stream_text = await gen_link(_id=inserted_id)
        await message.reply_text(
            text=stream_text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
    except FloodWait as e:
        print(f"En pause pendant {str(e.value)}s")
        await asyncio.sleep(e.value)
        await bot.send_message(chat_id=Telegram.ULOG_CHANNEL,
                               text=f"A ᴇᴜ FʟᴏᴏᴅWᴀɪᴛ ᴅᴇ {str(e.value)}s ᴅᴇ [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\n**ɪᴅ ᴜᴛɪʟɪsᴀᴛᴇᴜʀ :** `{str(message.from_user.id)}`",
                               disable_web_page_preview=True, parse_mode=ParseMode.MARKDOWN)


@FileStream.on_message(
    filters.channel
    & ~filters.forwarded
    & ~filters.media_group
    & (
            filters.document
            | filters.video
            | filters.video_note
            | filters.audio
            | filters.voice
            | filters.photo
    )
)
async def channel_receive_handler(bot: Client, message: Message):
    if await is_channel_banned(bot, message):
        return
    await is_channel_exist(bot, message)

    try:
        inserted_id = await db.add_file(get_file_info(message))
        await get_file_ids(False, inserted_id, multi_clients, message)
        reply_markup, stream_link = await gen_link(_id=inserted_id)
        await bot.edit_message_reply_markup(
            chat_id=message.chat.id,
            message_id=message.id,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ʟɪᴇɴ ᴅᴇ ᴛᴇ́ʟᴇ́ᴄʜᴀʀɢᴇᴍᴇɴᴛ 📥",
                                       url=f"https://t.me/{FileStream.username}?start=stream_{str(inserted_id)}")]])
        )

    except FloodWait as w:
        print(f"En pause pendant {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Telegram.ULOG_CHANNEL,
                               text=f"ᴀ ᴇᴜ ғʟᴏᴏᴅᴡᴀɪᴛ ᴅᴇ {str(w.x)}s ᴅᴇ {message.chat.title}\n\n**ɪᴅ ᴅᴇ ʟᴀ ᴄʜᴀɪ̂ɴᴇ :** `{str(message.chat.id)}`",
                               disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Telegram.ULOG_CHANNEL, text=f"**#SᴜɪᴠɪDᴇʀʀᴇᴜʀ:** `{e}`",
                               disable_web_page_preview=True)
        print(f"Jᴇ ɴᴇ ᴘᴇᴜx ᴘᴀs ᴍᴏᴅɪғɪᴇʀ ʟᴇ ᴍᴇssᴀɢᴇ ᴅᴇ ᴅɪғғᴜsɪᴏɴ !\nEʀʀᴇᴜʀ :  **Dᴏɴɴᴇᴢ-ᴍᴏɪ ʟᴇ ᴅʀᴏɪᴛ ᴅᴇ ᴍᴏᴅɪғɪᴄᴀᴛɪᴏɴ ᴅᴀɴs ʟᴇs ᴄʜᴀɪ̂ɴᴇs ᴅᴇ ᴍɪsᴇs à ᴊᴏᴜʀ ᴇᴛ ʟᴀ ᴄʜᴀɪ̂ɴᴇ ᴅᴇ ᴄᴏʀʙᴇɪʟʟᴇ !{e}**")