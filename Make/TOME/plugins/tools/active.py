from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from unidecode import unidecode

from TOME import app
from TOME.misc import SUDOERS
from TOME.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


async def fetch_active_chats(chat_type: str):
    text = ""
    served_chats = await (get_active_chats() if chat_type == "voice" else get_active_video_chats())
    remover = remove_active_chat if chat_type == "voice" else remove_active_video_chat

    for i, chat_id in enumerate(served_chats, start=1):
        try:
            chat = await app.get_chat(chat_id)
            title = unidecode(chat.title).upper()
            link = f"<a href=https://t.me/{chat.username}>{title}</a>" if chat.username else title
            suffix = f" [<code>{chat_id}</code>]" if chat_type == "video" else ""
            text += f"<b>{i}.</b> {link}{suffix}\n"
        except Exception:
            await remover(chat_id)
    return text


@app.on_message(filters.command("vc") & SUDOERS)
async def active_voice_chats(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    text = await fetch_active_chats("voice")
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command("vvc") & SUDOERS)
async def active_video_chats(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
    text = await fetch_active_chats("video")
    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command("ac") & SUDOERS)
async def active_count(_, message: Message):
    try:
        voice_count = len(await get_active_chats())
    except Exception:
        voice_count = 0

    try:
        video_count = len(await get_active_video_chats())
    except Exception:
        video_count = 0

    total_count = voice_count + video_count

    await message.reply_text(
        f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\n"
        f"ᴠᴏɪᴄᴇ : {voice_count}\n"
        f"ᴠɪᴅᴇᴏ : {video_count}\n"
        f"ᴛᴏᴛᴀʟ : {total_count}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]]
        )
    )
