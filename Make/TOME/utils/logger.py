from config import LOG, LOGGER_ID
from TOME import app
from TOME.utils.database import is_on_off
import random
from pyrogram.enums import ParseMode, ChatType
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




Play_photos = [
    "https://telegra.ph/file/81009f2e52c8a5f9c624f.jpg",
    "https://telegra.ph/file/6e1c51c0a9e6a8dd4b7d6.jpg",
    "https://telegra.ph/file/8906c2983ccccec87b94b.jpg",
    "https://telegra.ph/file/ff3f64662a7d2d963ad3a.jpg",
    "https://telegra.ph/file/f749c5ca043b065dcd155.jpg",
    "https://telegra.ph/file/2f92401e55df540e9a08a.jpg",
    "https://telegra.ph/file/23b2b067f655268c7175b.jpg",
    "https://telegra.ph/file/a9f3e132bd53e317facaf.jpg",
    "https://telegra.ph/file/41cc878a1f8e319564c14.jpg",
    "https://telegra.ph/file/706b4f1cc6fc0e6106d9d.jpg",
    "https://telegra.ph/file/bcc44687940963fa56e42.jpg",
    "https://telegra.ph/file/e6107f7f0cd82074351ed.jpg",
    "https://telegra.ph/file/01c3a968643c48431b354.jpg",
    "https://telegra.ph/file/9edc8ba62307c0e50fbd5.jpg",
    "https://telegra.ph/file/8336041b769dbc8e47932.jpg",
    "https://telegra.ph/file/685f02c8bcdf36f388293.jpg",
    "https://telegra.ph/file/1cf6bc0938fbf364f7a2c.jpg",
    "https://telegra.ph/file/79d5ee5a60995079ddc99.jpg",
    "https://telegra.ph/file/52aa7fae33e0e3b08d439.jpg",
    "https://graph.org/file/50037e072302b4eff55ba.jpg",
    "https://telegra.ph/file/9fb6b0b102b7ff81f8e7a.jpg",
    "https://telegra.ph/file/6bf43423eda4becdc945d.jpg",
    "https://telegra.ph/file/3ede26cb75f796ba46df6.jpg",
    "https://telegra.ph/file/5cc70669688b185c62cee.jpg",
    "https://telegra.ph/file/375fdfb226e00479ebd40.jpg",
    "https://telegra.ph/file/c10d3f6e3ba7a20d357be.jpg",
    "https://telegra.ph/file/2c4b942e7602112beeec6.jpg",
]

async def play_logs(message, streamtype):
    if await is_on_off(2):
        chatusername = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        
        if message.chat.type == ChatType.CHANNEL:
            logger_text = f"""┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈
<blockquote><b>╭⚉<b>{app.mention}
<b>╰⚆ᴘʟᴧʏ ⸢ᴄʜᴧɴɴᴇʟ⸥ ᴠᴇɢᴧ♪</b>

<b>╭⬤ ᴄʜᴧɴɴᴇʟ ɴᴧᴍᴇ :</b> {message.chat.title}
<b>┃᚜◉ ᴄʜᴧɴɴᴇʟ ᴜsᴇꝛ :</b> @{message.chat.username}
<b>╰⬢ ᴄʜᴧɴɴᴇʟ. ɪᴅ :</b>{message.chat.id}

<b>╭⬢ ǫᴜᴇꝛʏ :</b> {message.text.split(None, 1)[1]}
<b>╰⬤ sᴛꝛᴇᴧᴍᴛʏᴘᴇ :</b> {streamtype}
</blockquote>━ılıılıılıılıılıılııılıᴄʜᴧɴɴᴇʟılıılıılıılıılıılııllıılı━"""
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            message.chat.title, url=f"https://t.me/{message.chat.username}")
                    ],
                ]
            )
        else:
            logger_text = f"""┈┅┅━━━⊷⊰🍁⊱⊶━━━┅┅┈
<blockquote><b>╭❖<b>{app.mention}
<b>╰❖ ᴘʟᴧʏ ⸢ɢꝛᴏᴜᴘ⸥ ᴍᴜsɪᴄ♪</b></blockquote>
<blockquote>
<b>╭❖ ᴄʜᴧᴛ ɴᴧᴍᴇ :</b> {message.chat.title}
<b>┃᚜◉ᴄʜᴧᴛ ᴜsᴇꝛ :</b> @{message.chat.username}
<b>┃᚜◉ɴᴧᴍᴇ :</b> {message.from_user.mention if message.from_user else "Unknown User"}
<b>╰❖ ᴜsᴇꝛɴᴧᴍᴇ :</b> @{message.from_user.username if message.from_user and message.from_user.username else "Unknown User"}</blockquote>
<blockquote>
<b>╭❖ ǫᴜᴇꝛʏ :</b> {message.text.split(None, 1)[1]}
<b>╰❖ sᴛꝛᴇᴧᴍᴛʏᴘᴇ :</b> {streamtype}
</blockquote>┈┅┅━━━⊷⊰🌀⊱⊶━━━┅┅┈"""
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            message.chat.title, url=f"https://t.me/{message.chat.username}")
                    ],
                ]
            )
        
        photo_url = random.choice(Play_photos)
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_photo(
                    chat_id=LOGGER_ID,
                    photo=photo_url,
                    caption=logger_text,
                    reply_markup=reply_markup,
                    parse_mode=ParseMode.HTML
                )
            except Exception as e:
                print(f"Error sending photo: {e}")
        return
 
