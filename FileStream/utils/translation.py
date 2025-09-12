from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Sᴀʟᴜᴛ, </b>{}\n 
<b>Jᴇ sᴜɪs ᴜɴ ʙᴏᴛ ᴅᴇ sᴛʀᴇᴀᴍɪɴɢ ᴅᴇ ғɪᴄʜɪᴇʀs ᴛᴇʟᴇɢʀᴀᴍ ᴇᴛ ɢᴇ́ɴᴇ́ʀᴀᴛᴇᴜʀ ᴅᴇ ʟɪᴇɴs ᴅɪʀᴇᴄᴛs</b>\n
<b>Fᴏɴᴄᴛɪᴏɴɴᴇ sᴜʀ ʟᴇs ᴄʜᴀɪ̂ɴᴇs ᴇᴛ ʟᴇs ᴅɪsᴄᴜssɪᴏɴs ᴘʀɪᴠᴇ́ᴇs</b>\n
<b>💕 @{}</b>\n"""

    HELP_TEXT = """
<b>- ᴀᴊᴏᴜᴛᴇᴢ-ᴍᴏɪ ᴄᴏᴍᴍᴇ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴇᴜʀ sᴜʀ ʟᴀ ᴄʜᴀɪ̂ɴᴇ</b>
<b>- ᴇɴᴠᴏʏᴇᴢ-ᴍᴏɪ ɴ'ɪᴍᴘᴏʀᴛᴇ ǫᴜᴇʟ ᴅᴏᴄᴜᴍᴇɴᴛ ᴏᴜ ᴍᴇ́ᴅɪᴀ</b>
<b>- ᴊᴇ ғᴏᴜʀɴɪʀᴀɪ ᴜɴ ʟɪᴇɴ ᴅᴇ sᴛʀᴇᴀᴍɪɴɢ</b>\n
<b>🔞 ᴄᴏɴᴛᴇɴᴜ ᴀᴅᴜʟᴛᴇ sᴛʀɪᴄᴛᴇᴍᴇɴᴛ ɪɴᴛᴇʀᴅɪᴛ.</b>\n
<i><b>ʀᴇᴘᴏʀᴛᴇʀ ʟᴇs ʙᴜɢs ᴀ̀ <a href='https://telegram.me/Hyoshdesign'>ʟᴇ ᴅᴇ́ᴠᴇʟᴏᴘᴘᴇᴜʀ</a></b></i>"""

    ABOUT_TEXT = """
<b>⚜ ᴍᴏɴ ɴᴏᴍ : {}</b>\n
<b>✦ ᴠᴇʀsɪᴏɴ : {}</b>
<b>✦ ᴍɪs ᴀ̀ ᴊᴏᴜʀ ʟᴇ : 12-septembre-2025</b>
<b>✦ ᴅᴇ́ᴠᴇʟᴏᴘᴘᴇᴜʀ : <a href='https://telegram.me/Hyoshdesign'>Hyosh coder</a></b>\n
"""

    STREAM_TEXT = """
<i><u>Vᴏᴛʀᴇ ʟɪᴇɴ ᴇsᴛ ɢᴇ́ɴᴇ́ʀᴇ́ !</u></i>\n
<b>📂 ɴᴏᴍ ᴅᴜ ғɪᴄʜɪᴇʀ :</b> <b>{}</b>\n
<b>📦 ᴛᴀɪʟʟᴇ ᴅᴜ ғɪᴄʜɪᴇʀ :</b> <code>{}</code>\n
<b>📥 ᴛᴇ́ʟᴇ́ᴄʜᴀʀɢᴇᴍᴇɴᴛ :</b> <code>{}</code>\n
<b>🖥 ʀᴇɢᴀʀᴅᴇʀ :</b> <code>{}</code>\n
<b>🔗 ᴘᴀʀᴛᴀɢᴇʀ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>Vᴏᴛʀᴇ ʟɪᴇɴ ᴇsᴛ ɢᴇ́ɴᴇ́ʀᴇ́ !</u></i>\n
<b>📂 ɴᴏᴍ ᴅᴜ ғɪᴄʜɪᴇʀ :</b> <b>{}</b>\n
<b>📦 ᴛᴀɪʟʟᴇ ᴅᴜ ғɪᴄʜɪᴇʀ :</b> <code>{}</code>\n
<b>📥 ᴛᴇ́ʟᴇ́ᴄʜᴀʀɢᴇᴍᴇɴᴛ :</b> <code>{}</code>\n
<b>🔗 ᴘᴀʀᴛᴀɢᴇʀ :</b> <code>{}</code>\n"""

    BAN_TEXT = "__Dᴇ́sᴏʟᴇ́ Mᴏɴsɪᴇᴜʀ, Vᴏᴜs ᴇ̂ᴛᴇs ʙᴀɴɴɪ ᴅ'ᴜᴛɪʟɪsᴇʀ ᴄᴇ ʙᴏᴛ.__\n\n**[Cᴏɴᴛᴀᴄᴛᴇᴢ ʟᴇ ᴅᴇ́ᴠᴇʟᴏᴘᴘᴇᴜʀ](tg://user?id={}) ɪʟ ᴠᴏᴜs ᴀɪᴅᴇʀᴀ**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ᴀɪᴅᴇ', callback_data='help'),
            InlineKeyboardButton('ᴀ̀ ᴘʀᴏᴘᴏs', callback_data='about'),
            InlineKeyboardButton('ғᴇʀᴍᴇʀ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 ᴄʜᴀɪ̂ɴᴇ ᴅᴇ ᴍɪsᴇs ᴀ̀ ᴊᴏᴜʀ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ᴀᴄᴄᴜᴇɪʟ', callback_data='home'),
            InlineKeyboardButton('ᴀ̀ ᴘʀᴏᴘᴏs', callback_data='about'),
            InlineKeyboardButton('ғᴇʀᴍᴇʀ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴄʜᴀɪ̂ɴᴇ ᴅᴇ ᴍɪsᴇs ᴀ̀ ᴊᴏᴜʀ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ᴀᴄᴄᴜᴇɪʟ', callback_data='home'),
            InlineKeyboardButton('ᴀɪᴅᴇ', callback_data='help'),
            InlineKeyboardButton('ғᴇʀᴍᴇʀ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴄʜᴀɪ̂ɴᴇ ᴅᴇ ᴍɪsᴇs ᴀ̀ ᴊᴏᴜʀ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )