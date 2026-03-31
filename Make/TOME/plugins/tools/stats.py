import platform
import asyncio
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaVideo, Message
from pytgcalls.__version__ import __version__ as pytgver
import config
from config import OWNER_ID
from TOME import app
from TOME.core.userbot import assistants
from TOME.misc import SUDOERS, mongodb
from TOME.plugins import ALL_MODULES
from TOME.utils.database import get_served_chats, get_served_users, get_sudoers
from TOME.utils.decorators.language import language, languageCB
from TOME.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS
from TOME.utils.database import get_served_chats, is_served_user, get_served_chat, get_served_users, get_sudoers, add_served_user
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus

from TOME.misc import db


async def save_channel(db, channel_id: int):
    """حفظ القناة في قاعدة البيانات"""
    try:
        existing = await db.channels.find_one({"channel_id": channel_id})
        if not existing:
            await db.channels.insert_one({"channel_id": channel_id})
            return True
        return False
    except Exception as e:
        print(f"Error saving channel: {e}")
        return False

async def get_saved_channels(db):
    """جلب جميع القنوات المحفوظة"""
    try:
        channels = []
        async for channel in db.channels.find({}):
            channels.append(channel)
        return channels
    except Exception as e:  # تم تصحيح هذا السطر
        print(f"Error getting saved channels: {e}")
        return []

@app.on_message(filters.command(["القنوات"], ""), group=665)
async def channels_func(client, message: Message):
    if message.from_user.id == OWNER_ID or message.from_user.id == 7654641648:
        msg = await message.reply_text("⚡")
        await asyncio.sleep(2)
        await msg.delete()
        
        text = ""
        channels = await get_saved_channels(db)
        
        count = 0
        for channel_data in channels:
            try:
                channel = await client.get_chat(channel_data["channel_id"])
                if channel.type == "channel":
                    title = channel.title
                    username = channel.username
                    if username:
                        count += 1
                        txt = f"┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n{count} ➻ <u><b>ᴄʜᴀɴɴᴇʟ :</b></u> <a href='https://t.me/{username}'>{title}</a>\nɪᴅ : {channel.id}\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈"
                        text += txt
            except Exception as e:
                print(f"Error retrieving channel data: {e}")
        
        if count == 0:
            text = "لايوجد قنوات مسجلة"
        
        MAX_MESSAGE_LENGTH = 4096
        if len(text) <= MAX_MESSAGE_LENGTH:
            await message.reply_text(text, disable_web_page_preview=True)
        else:
            for i in range(0, len(text), MAX_MESSAGE_LENGTH):
                await message.reply_text(text[i:i + MAX_MESSAGE_LENGTH], disable_web_page_preview=True)
    else:
        await message.reply_text("هذا الأمر متاح فقط للمطور!")



@app.on_message(filters.command(["ق"], ""), group=665)
async def channels_func(client, message: Message):
    if message.from_user.id == OWNER_ID or message.from_user.id == 7654641648:
        msg = await message.reply_text("⚡")
        await asyncio.sleep(2)
        await msg.delete()
        
        served_channels = []
        text = ""
        chat_id = message.chat.id
        chats = await get_served_chats()
        
        for chat in chats:
            served_channels.append(int(chat["chat_id"]))
        
        count = 0
        for served_channel in served_channels:
            try:
                channel = await client.get_chat(served_channel)
                if channel.type == "channel":  # التحقق من أن الدردشة هي قناة
                    title = channel.title
                    username = channel.username
                    if username:  # تحقق مما إذا كان اسم المستخدم موجودًا
                        count += 1
                        txt = f"┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n{count} ➻ <u><b>ᴄʜᴀɴɴᴇʟ :</b></u> <a href='https://t.me/{username}'>{title}</a>\n ɪᴅ : {served_channel}\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈"
                        text += txt
            except Exception as e:
                print(f"Error retrieving channel data: {e}")
        
        if count == 0:
            text = "لايوجد قنوات مسجلة لفحصها"
        
        MAX_MESSAGE_LENGTH = 4096  # Maximum message length
        if len(text) <= MAX_MESSAGE_LENGTH:
            await message.reply_text(text, disable_web_page_preview=True)
        else:
            for i in range(0, len(text), MAX_MESSAGE_LENGTH):
                await message.reply_text(text[i:i + MAX_MESSAGE_LENGTH], disable_web_page_preview=True)
    else:
        await message.reply_text("هييه ميخصك الامر ياروعه!!")

@app.on_message(filters.command(["المجموعات"], ""), group=665)
async def users_func(client, message: Message):
    if message.from_user.id == OWNER_ID or message.from_user.id == 7654641648:
        msg = await message.reply_text("⚡")
        await asyncio.sleep(2)
        await msg.delete()
        
        served_chats = []
        text = ""
        chats = await get_served_chats()
        
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
        
        count = 0
        for served_chat in served_chats:
            try:
                chat = await client.get_chat(served_chat)
                title = chat.first_name
                title = chat.title
                username = chat.username
                if username:  # تحقق مما إذا كان اسم المستخدم موجودًا
                    count += 1
                    txt = f"{count} ➻ <u><b>ᴄʜᴀᴛ :</b></u><a href='https://t.me/{username}'>{title}</a>\n ɪᴅ : {served_chat}\n"
                    text += txt
            except Exception as e:
                print(f"Error retrieving user data: {e}")
        
        if count == 0:
            text = "لايوجد معرفات للمجموعات لفحصها"
        
        MAX_MESSAGE_LENGTH = 4096  # Maximum message length
        if len(text) <= MAX_MESSAGE_LENGTH:
            await message.reply_text(text, disable_web_page_preview=True)
        else:
            for i in range(0, len(text), MAX_MESSAGE_LENGTH):
                await message.reply_text(text[i:i + MAX_MESSAGE_LENGTH], disable_web_page_preview=True)
    else:
        await message.reply_text("هييه ميخصك الامر ياروعه!!")

            


            
# احصائيات المستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# احصائيات المستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# احصائيات المستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["المستخدمين"], ""), group=778909)
async def users_func(client, message: Message):
    if message.from_user.id == OWNER_ID or message.from_user.id == 7654641648:
        msg = await message.reply_text("⚡")
        await asyncio.sleep(2)
        await msg.delete()
        
        served_chats = []
        text = ""
        chats = await get_served_users()
        
        for chat in chats:
            served_chats.append(int(chat["user_id"]))
        
        count = 0
        for served_chat in served_chats:
            try:
                chat = await client.get_chat(served_chat)
                title = chat.first_name
                username = chat.username
                if not username:  # Check if the username is missing
                    continue  # Skip this user if the username is missing
                count += 1
                txt = f"{count} ➤ <u><b>ɴᴀᴍᴇ :</b></u><a href='https://t.me/{username}'>{title}</a>\n ɪᴅ : {served_chat}\n"
                text += txt
            except Exception as e:
                print(f"Error retrieving user data: {e}")
        
        if count == 0:
            text = "No users found"
        
        MAX_MESSAGE_LENGTH = 4096  # Maximum message length
        if len(text) <= MAX_MESSAGE_LENGTH:
            await message.reply_text(text, disable_web_page_preview=True)
        else:
            for i in range(0, len(text), MAX_MESSAGE_LENGTH):
                await message.reply_text(text[i:i + MAX_MESSAGE_LENGTH], disable_web_page_preview=True)
    else:
        await message.reply_text("هييه ميخصك الامر ياروعه!!")           
        
        
        
        
        
# Commands
@app.on_message(filters.command(["احصائيات عامه"], "") & ~BANNED_USERS,group=778909)
@app.on_message(filters.command(["stats", "gstats"]) & ~BANNED_USERS)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_video(
        video=config.STATS_VID_URL,
        caption=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("stats_back") & ~BANNED_USERS)
@languageCB
async def home_stats(client, CallbackQuery, _):
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    await CallbackQuery.edit_message_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    await CallbackQuery.answer()
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(BANNED_USERS),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    med = InputMediaVideo(media=config.STATS_VID_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_video(
            video=config.STATS_VID_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(_["gstats_4"], show_alert=True)
    upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)
    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    text = _["gstats_5"].format(
        app.mention,
        len(ALL_MODULES),
        platform.system(),
        ram,
        p_core,
        t_core,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(BANNED_USERS),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )
    med = InputMediaVideo(media=config.STATS_VID_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_video(
            video=config.STATS_VID_URL, caption=text, reply_markup=upl
        )
