import requests
import asyncio
import glob
import os
import time
import requests
import random
import aiohttp
import wget
import yt_dlp
import traceback
from pyrogram.types import InputMediaAudio
import asyncio
import os
import re
from typing import Union
import yt_dlp
from yt_dlp import YoutubeDL
from TOME.plugins.play.ADMANS import *
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch
import asyncio
import os
import time
import requests
import random
import aiohttp
from config import *
import config
from pyrogram import filters
from TOME.plugins.play.ADMANS import *
from pyrogram import Client
from config import OWNER_ID
from os import getenv

from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from telegraph import upload_file
from asyncio import gather
from random import  choice, randint
import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ParseMode
import requests
from TOME.utils.database import is_on_off
from TOME.utils.formatters import time_to_seconds
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from youtubesearchpython import SearchVideos
import requests
import wget
from config import *


import asyncio
import aiohttp

import os
import time
import requests
from config import START_VIDS
from pyrogram import filters
import random
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
from pyrogram import Client
from pyrogram import enums

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from random import  choice, randint
from pyrogram import Client, filters
from pyrogram.types import Message
from gtts import gTTS
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
import config
from config import OWNER_ID
from config import BANNED_USERS
from config import BANNED_USERS, OWNER_ID
from config import START_VIDS
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from random import  choice, randint
from pytube import Search
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from TOME import app
import speech_recognition as sr
from pyrogram import Client, filters
from pydub import AudioSegment
from os import remove
import asyncio
import os
import time
import requests
import random
import aiohttp
from config import *
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from telegraph import upload_file
from asyncio import gather
from random import  choice, randint
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pySmartDL import SmartDL
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube)
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import filters
import random
from pyrogram import Client

import requests
import yt_dlp
from youtube_search import YoutubeSearch





from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from TOME import  app
from config import OWNER_ID
from config import BANNED_USERS


#مكاتب كود قولي

import asyncio
import aiohttp

import os
import time
import requests
from config import START_VIDS
from pyrogram import filters
import random
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import*
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
from pyrogram import Client
from pyrogram import enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from random import  choice, randint
from pyrogram import Client, filters
from pyrogram.types import Message
from gtts import gTTS
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
from pydub import AudioSegment
from playsound import playsound
from pyrogram import Client, filters
from gtts import gTTS
import os
import glob
import random




OWNER_ID = getenv("OWNER_ID")





def cookies():
    folder_path = "/root/cookies"  # مسار مجلد الكوكيز
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    
    if not txt_files:
        return None
    
    cookie_file = random.choice(txt_files)
    return cookie_file










dowof = []


GLOBAL_DOWNLOAD_DISABLED = False 
LOCAL_DOWNLOAD_DISABLED = []     

@app.on_message(filters.command(["تعطيل التحميل عام"], "")  & filters.private, group=82826391)
async def global_disable_download(_, message: Message):
    if str(message.from_user.id) == OWNER_ID:
        global GLOBAL_DOWNLOAD_DISABLED
        if GLOBAL_DOWNLOAD_DISABLED:
            await message.reply("✅ التحميل معطل بالفعل في جميع المجموعات\n༄")
            return
        GLOBAL_DOWNLOAD_DISABLED = True
        await message.reply("🔒 تم تعطيل التحميل في جميع المجموعات\n༄")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
@app.on_message(filters.command(["تفعيل التحميل عام"], "")  & filters.private, group=8272691)
async def global_enable_download(_, message: Message):
    if str(message.from_user.id) == OWNER_ID:
        global GLOBAL_DOWNLOAD_DISABLED
        if not GLOBAL_DOWNLOAD_DISABLED:
            await message.reply("✅ التحميل مفعل بالفعل في جميع المجموعات\n༄")
            return
        GLOBAL_DOWNLOAD_DISABLED = False
        await message.reply("🔓 تم تفعيل التحميل في جميع المجموعات\n༄")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
@app.on_message(filters.command(["قفل التحميل", "تعطيل التحميل"], "")  & filters.group, group=82826389)
async def local_disable_download(_, message: Message):
    get = await client.get_chat_member(chat_id, message.from_user.id)
    if (get.status in [ChatMemberStatus.OWNER] or 
        is_owner(None, None, message) or
        is_moteerr(message.from_user.id) or  
        is_mutaw(message.from_user.id) or 
        is_malkeen(message.from_user.id) or 
        is_admann(message.from_user.id)):
        if message.chat.id in LOCAL_DOWNLOAD_DISABLED:
            await message.reply("✅ التحميل معطل بالفعل في هذه المجموعة\n༄")
            return
        LOCAL_DOWNLOAD_DISABLED.append(message.chat.id)
        await message.reply("🔒 تم تعطيل التحميل في هذه المجموعة\n༄")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")



@app.on_message(filters.command(["فتح التحميل", "تفعيل التحميل"], "")  & filters.group, group=8272689)
async def local_enable_download(_, message: Message):
    get = await client.get_chat_member(chat_id, message.from_user.id)
    if (get.status in [ChatMemberStatus.OWNER] or 
        is_owner(None, None, message) or
        is_moteerr(message.from_user.id) or  
        is_mutaw(message.from_user.id) or 
        is_malkeen(message.from_user.id) or 
        is_admann(message.from_user.id)):
        if message.chat.id not in LOCAL_DOWNLOAD_DISABLED:
            await message.reply("✅ التحميل مفعل بالفعل في هذه المجموعة\n༄")
            return
        LOCAL_DOWNLOAD_DISABLED.remove(message.chat.id)
        await message.reply("🔓 تم تفعيل التحميل في هذه المجموعة\n༄")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")






import os
import re
import yt_dlp
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch

# المتغيرات العامة
BUTTON_NAME = "ᴠᴇɢᴀ"
BUTTON_URL = "https://t.me/TopTOME"  # يمكن تغييرها عبر الأوامر
disabled_chats = []
GLOBAL_DOWNLOAD_DISABLED = False
LOCAL_DOWNLOAD_DISABLED = []



if not os.path.exists("downloads"):
    os.makedirs("downloads")

@app.on_message(filters.command(["تحميل","يوت","حمل"], ""), group=56)
async def song_downloader(_, message):
    if GLOBAL_DOWNLOAD_DISABLED:
        return await message.reply_text("⛔ التحميل معطل حاليًا في جميع المجموعات")
    if message.chat.id in LOCAL_DOWNLOAD_DISABLED:
        return await message.reply_text("⛔ التحميل معطل في هذه المجموعة")
    
    original_user = message.from_user.id
    if len(message.command) > 1:
        query = " ".join(message.command[1:])
    else:
        ask = await app.ask(message.chat.id, "🎵 أرسل اسم الأغنية التي تريد تحميلها")
        if ask.from_user.id != original_user:
            return
        query = ask.text
    
    m = await message.reply("ثواني وتجيك ♪ ..")
    
    # إعدادات yt-dlp محسنة
    ydl_ops = {
        'format': 'bestaudio/best',
        'cookiefile': cookies(),
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'noplaylist': True,
        'ignoreerrors': True,
        'no_warnings': True,
    }
    
    try:
        # البحث مع معالجة أفضل للأخطاء
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results or not results[0].get('url_suffix'):
            return await m.edit("⚠️ لم يتم العثور على نتائج أو رابط غير صالح")

        video_info = results[0]
        link = f"https://youtube.com{video_info['url_suffix']}"
        video_id = video_info.get('id', '')
        
        if not video_id:
            return await m.edit("⚠️ لا يمكن تحديد معرف الفيديو")

        title = video_info.get("title", "غير معروف")[:40]
        duration = video_info.get("duration", "غير معروف")
        views = video_info.get("views", "غير معروف")

        audio_file = f"downloads/{video_id}.mp3"
        
        # التحقق من وجود الملف مسبقًا
        if os.path.exists(audio_file):
            await m.edit("🔄 جاري إرسال الملف من الذاكرة...")
        else:
            await m.edit("⏬ جاري تحميل الملف من اليوتيوب..")
            try:
                with yt_dlp.YoutubeDL(ydl_ops) as ydl:
                    info_dict = ydl.extract_info(link, download=True)
                    if not info_dict:
                        return await m.edit("⚠️ فشل في جلب معلومات الفيديو")
                    
                    audio_file = ydl.prepare_filename(info_dict)
                    audio_file = os.path.splitext(audio_file)[0] + '.mp3'
                    
                    if not os.path.exists(audio_file):
                        return await m.edit("⚠️ فشل في تحميل الملف الصوتي")
            except Exception as download_error:
                return await m.edit(f"⚠️ خطأ في التحميل: {str(download_error)}")

        # إعداد معلومات الإرسال
        rep = (
            f"<b>╭◉ ᚐᴛɪᴛʟᴇ : </b>{title}\n"
            f"<b>┃᚜◉ ᴅᴜʀᴀᴛɪᴏɴ : </b><code>{duration}</code>\n"
            f"<b>╰◉ ᚐɴᴠɪᴇᴡs : </b>{views}"
        )
        
        reply_markup = None
        if BUTTON_NAME and BUTTON_URL:
            reply_markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton(BUTTON_NAME, url=BUTTON_URL)]]
            )
        
        # حساب المدة بالثواني
        try:
            dur_arr = str(duration).split(":")
            dur = sum(int(x) * 60 ** i for i, x in enumerate(reversed(dur_arr)))
        except:
            dur = 0
        
        # إرسال الملف الصوتي
        await message.reply_audio(
            audio_file,
            caption=rep,
            title=title,
            duration=dur,
            reply_markup=reply_markup,
            thumb=None,
        )
        await m.delete()

    except Exception as e:
        error_msg = f"⚠️ حدث خطأ: {str(e)}" if str(e) else "⚠️ حدث خطأ غير متوقع"
        await m.edit(error_msg)
        print(f"Error: {str(e)}")

        



@app.on_message(filters.command(["/vsong","/YouTube","يوتيوب"], ""), group=8272689)
async def video_downloader(_, message):
   
        
    try:
        # التحقق من حالة التحميل
        if GLOBAL_DOWNLOAD_DISABLED:
            return await message.reply_text("⛔ التحميل معطل حاليًا في جميع المجموعات")
        if message.chat.id in LOCAL_DOWNLOAD_DISABLED:
            return await message.reply_text("⛔ التحميل معطل في هذه المجموعة")

        # الحصول على اسم الفيديو
        if len(message.command) > 1:
            query = " ".join(message.command[1:])
        else:
            ask = await app.ask(message.chat.id, "🎬 أرسل اسم الفيديو الذي تريد تحميله")
            if ask.from_user.id != message.from_user.id:
                return
            query = ask.text

        m = await message.reply("ثواني وتجيك ♪  ..")

        # إعداد خيارات التنزيل
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': '%(id)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'cookiefile': cookies(),
            'extract_flat': True,
            'geo_bypass': True,
            'nocheckcertificate': True,
            'retries': 3,
        }

        # البحث عن الفيديو
        try:
            search = VideosSearch(query, limit=1)
            result = search.result().get('result', [])
            if not result:
                return await m.edit("⚠️ لم يتم العثور على نتائج")

            video = result[0]
            video_id = video['id']
            title = video['title'][:60]
            duration = video.get('duration', '00:00')
            views = video.get('viewCount', {}).get('short', 'N/A')
            thumbnail = video['thumbnails'][0]['url']
            link = f"https://youtube.com/watch?v={video_id}"

            # تحميل الصورة المصغرة
            thumb_name = f"{video_id}.jpg"
            async with aiohttp.ClientSession() as session:
                async with session.get(thumbnail) as resp:
                    if resp.status == 200:
                        with open(thumb_name, 'wb') as f:
                            f.write(await resp.read())

        except Exception as e:
            await m.edit("⚠️ حدث خطأ أثناء البحث")
            print(f"Search Error: {str(e)}")
            return

        # تحميل الفيديو
        video_file = None
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                video_file = ydl.prepare_filename(info_dict)

                if not os.path.exists(video_file):
                    return await m.edit("⚠️ فشل في تحميل ملف الفيديو")

                # تحويل المدة إلى ثواني
                duration_sec = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(':'))))

                # إعداد التنسيق
                rep = f"""🎬 
• العنوان <b>{title}</b>
•  المدة: <code>{duration}</code>
•  المشاهدات: <code>{views}</code>
"""
                reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(BUTTON_NAME, url=BUTTON_URL)]]
                )

                # إرسال الفيديو
                await message.reply_video(
                    video_file,
                    caption=rep,
                    duration=duration_sec,
                    thumb=thumb_name,
                    reply_markup=reply_markup,
                )
                await m.delete()

        except yt_dlp.utils.DownloadError as e:
            if "Video unavailable" in str(e):
                await m.edit("⚠️ هذا المحتوى غير متاح على يوتيوب")
            else:
                await m.edit("⚠️ حدث خطأ أثناء التحميل")
            print(f"Download Error: {str(e)}")
            return
        except Exception as e:
            await m.edit("⚠️ حدث خطأ غير متوقع أثناء التحميل")
            print(f"Download Error: {str(e)}")
            return

        finally:
            # تنظيف الملفات المؤقتة
            try:
                if video_file and os.path.exists(video_file):
                    os.remove(video_file)
                if thumb_name and os.path.exists(thumb_name):
                    os.remove(thumb_name)
            except Exception as e:
                print(f"Cleanup Error: {str(e)}")

    except Exception as e:
        await message.reply_text(f"⚠️ حدث خطأ غير متوقع: {str(e)}")
        print(f"Unexpected Error: {str(e)}")



# قفل المشاهده ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قفل المشاهده  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓







#بحث ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#بحث ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["بحث"], ""), group=4458890044)
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("يمكن البحث عبر تومي")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("⏳")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"◉ العنوان : {results[i]['title']}\n"
            text += f"◉ المدة : <code>{results[i]['duration']}</code>\n"
            text += f"◉ المشاهدات : <code>{results[i]['views']}</code>\n"
            text += f"◉ القناه : {results[i]['channel']}\n"
            text += f"◉ الرابط : https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "⸢ᴠᴇɢᴧ⸥", url=SUPPORT_CHANNEL),
                ],[
                    InlineKeyboardButton(
                        text="⸢✘⸥",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
    


#قولي او قوله ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#قولي او قوله ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




kolyof = []

@app.on_message(filters.command(["قفل قولي", "تعطيل قولي"], ""), group=27727181882)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if message.chat.id in kolyof:
        return await message.reply_text("قولي معطل من قبل\n༄")
      kolyof.append(message.chat.id)
      return await message.reply_text("تم تعطيل قولي بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")

@app.on_message(filters.command(["فتح قولي", "تفعيل قولي"], ""), group=7262627288)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if not message.chat.id in kolyof:
        return await message.reply_text("قولي مفعل من قبل\n")
      kolyof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل قولي بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")





def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files) 
    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"ᴇʀʀᴏʀ: {response.status_code} - {response.text}"

@app.on_message(filters.command(["tgm", "تلجراف", "telegraph", "تلغراف","ميديا","تلجراف ميديا",], ""), group=87556778)
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "**قم بالرد علي الصوره او الفيديو لستخراج الرابط**"
        ) 
    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size 
    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("الحد المسموح به لوزن هو :  200MB.") 
    try:
        text = await message.reply("🛠️") 
        async def progress(current, total):
            try:
                await text.edit_text(f"⚙️")
            except Exception:
                pass 
        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("⛓️‍💥") 
            success, upload_path = upload_file(local_path) 
            if success:
                await text.edit_text(
                    f"• [رابـط المـيديـا]\n`{upload_path}`\n-",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(text="فتح الرابط", url=upload_path),
                                InlineKeyboardButton(text="مشاركه الرابط", url=f"https://telegram.me/share/url?url={upload_path}")
                            ]
                        ]
                    ),
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await text.edit_text(
                    f"حدث خطاء\n{upload_path}"
                )
            try:
                os.remove(local_path)
            except Exception:
                pass 
        except Exception as e:
            await text.edit_text(f"حدث خطاء في : : {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass




becallllof = []

@app.on_message(filters.command(["قفل بيقول ايه", "تعطيل بيقول ايه"], ""), group=27727181882)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if message.chat.id in becallllof:
        return await message.reply_text("تحويل لنص معطل من قبل\n༄")
      becallllof.append(message.chat.id)
      return await message.reply_text("تم تعطيل تحويل لنص بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")

@app.on_message(filters.command(["فتح بيقول ايه", "تفعيل بيقول ايه"], ""), group=7262627288)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6753126490 or message.from_user.id == 6760053475:
      if not message.chat.id in becallllof:
        return await message.reply_text("تحويل لنص مفعل من قبل\n")
      becallllof.remove(message.chat.id)
      return await message.reply_text("تم تفعيل تحويل لنص بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")
      



@app.on_message(filters.command(["بيقول ايه"], ""), group=92820)
async def speech_to_text(client, message):
    if message.chat.id in becallllof:
        return await message.reply_text('تحويل لنص معطل من قبل الادمن\n༄')
        
    if not message.reply_to_message:
        await message.reply("قم بي الرد علي الصوت اولا")
        return
    voice_down = await message.reply_to_message.download("./recyad.wav")
    voice = sr.Recognizer()
    sound = AudioSegment.from_ogg(voice_down)
    wav_file = sound.export(voice_down, format="wav")
    with sr.AudioFile(wav_file) as source:
        audio_source = voice.record(source)
    msg = await message.reply("🧐")
    await asyncio.sleep(2)
    await msg.delete()
    try:
        text = voice.recognize_google(audio_source, language='ar-EG')
    except Exception as e:
        text = f"فشل التعرف علي الكلام\n{e}"
    await message.reply(text)
    remove("recyad.wav") 
    




@app.on_message(filters.command(['قولي', 'قوله'], ''), group=125060901007)
async def speak(_, message: Message):
    if message.chat.id in kolyof:
        return await message.reply_text('قولي معطل من قبل الادمن\n༄')
    chat_id = message.chat.id
    usr = await app.get_chat(message.from_user.id)
    name = usr.first_name
    data = message.text.split(maxsplit=1)
    if len(data) < 2:
        return await message.reply('اقولك ايه يروحي\n༄', reply_to_message_id=message.id)
    
    wait = await message.reply('👄', reply_to_message_id=message.id)
    
    if data[1].isascii():
        language = 'en'
    else:
        language = 'ar'
    
    audio_path = f'{message.from_user.username}.mp3'
    
    tts = gTTS(text=data[1], lang=language)
    tts.save(audio_path)
    
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(name, url=f'https://t.me/{message.from_user.username}')]]
    )
    
    with open(audio_path, 'rb') as audio_file:
        await app.send_voice(chat_id=chat_id, voice=audio_file, caption=data[1], reply_to_message_id=message.id, reply_markup=reply_markup)
    
    await wait.delete()
    os.remove(audio_path)   






@app.on_message(filters.command(["قولي","قوله"], ""), group=125060901007)
async def speak(_, message: Message):
    chat_id = message.chat.id
    data = message.text.split(maxsplit=1)
    if len(data) < 2:return await message.reply("اقولك ايه يروحي", reply_to_message_id=message.id)
    wait = await message.reply('استني حبي هكلم', reply_to_message_id=message.id)
    if data[1].isascii():
        language = 'en'
    else:
        language = 'ar'
    audio = gTTS(text=data[1], lang=language)
    audio.save(f"{message.from_user.username}.mp3")
	
    with open(f"{message.from_user.username}.mp3", "rb") as audio:
        await app.send_voice(chat_id=chat_id, voice=audio, reply_to_message_id=message.id)
        await wait.delete()
    os.remove(f"{message.from_user.username}.mp3")
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["هكرو"], ""), group=9282230)
async def tahker_1(client, msg):
    user_id = (
        msg.reply_to_message.from_user.id
        if msg.reply_to_message
        else msg.from_user.id
    )
    chat_id = msg.chat.id
    animation_chars = [
        "**يتم الربط بقاعدة بيانات التلجرام**",
        "يتم تهكير من : [ @TopTOME ]",
        "جار الاختراق. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
        (
            "حساب الضحية تم اختراقه...\n\nادفع المال $ وسيتم حذف معلوماتك\n\n\n"
            "الترمنال:\nيتم تحميل:\n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\n"
            "يتم تجميع حزمة البيانات \n  يتم تحميل Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\n"
            "يتم التصنيع لـ Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عملية 'النجاح'\n"
            "جار الإنشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 "
            "sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n"
            "يتم الحفظ في الجهاز:\n /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n"
            "**تم بنجاح اختراق قاعدة بيانات التلجرام**\n\n\n"
            "✰︎ تم حفظ بيانات الواتساب  ✅\n"
            "✰︎ تم حفظ بيانات الفيسبوك ✅\n"
            "✰︎ تم حفظ بيانات التلجرام  ✅\n"
            "✰︎ تم حفظ صورة المعرض  ✅\n"
            "✰︎ تم حفظ جهات الاتصال  ✅\n"
            "✰︎ تم حفظ جميع الرسائل  ✅\n"
            "سيتم نشرها علي دارك ويب ✅"
            
        )
    ]
    
    message = await msg.reply_text(animation_chars[0])
    for i in range(1, len(animation_chars)):
        await asyncio.sleep(5)
        try:
            await message.edit_text(animation_chars[i])
        except Exception as e:
            print(f"⚠️ خطأ في تحديث الرسالة: {e}")
            break
    
    # التأكد من إرسال الرسالة النهائية
    await asyncio.sleep(1)
    await message.edit_text(animation_chars[-1])





