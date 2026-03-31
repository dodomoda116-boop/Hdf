import asyncio
import re
import os
from os import getenv
import datetime

from TOME.core.userbot import *
from datetime import datetime
from pyrogram import filters, enums

from dotenv import load_dotenv
from pyrogram import filters
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import (Message, InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from TOME import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio
import requests
from TOME.plugins.play.ADMANS import *
import os
from inspect import getfullargspec
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

from pyrogram import filters
from pyrogram.types import Message
from TOME.core.userbot import assistants

from TOME import app
from TOME.misc import SUDOERS
from TOME.utils.database import get_client, get_assistant


from pyrogram import Client, filters
from TOME import app
from config import OWNER_ID
from TOME.utils.database import get_served_chats, get_served_users, set_must, get_must, del_must, get_must_ch, set_must_ch
from TOME.utils.database import get_active_chats, remove_active_video_chat, remove_active_chat
import os 
from pyrogram.enums import ParseMode
import shutil
import asyncio 

from TOME import app
from TOME.core.call import KIM
from TOME.utils.database import set_loop
from TOME.utils.decorators import AdminRightsCheck
from datetime import datetime
from TOME.utils import bot_sys_stats
from TOME.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.errors import PeerIdInvalid
from os import getenv
from TOME.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv

from TOME.utils.decorators.admins import AdminActual
from TOME import app
import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
from sys import version as pyver
from datetime import datetime
from config import STRING1, OWNER_ID, BOT_TOKEN

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver

from pyrogram import enums


import config
from config import OWNER_ID
from config import BANNED_USERS
from TOME import YouTube, app
from TOME import app as Client
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import PeerIdInvalid
from config import  bot_id, db
from TOME.core.userbot import assistants
from TOME.misc import SUDOERS, mongodb
from TOME.plugins import ALL_MODULES
from TOME.utils.decorators.language import language, languageCB
from TOME.utils.inline.stats import back_stats_buttons, stats_buttons

loop = asyncio.get_running_loop()


SUDORS = [OWNER_ID]




from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from TOME import  app
from config import OWNER_ID
from config import BANNED_USERS


#مكاتب الصوره الجديده ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
import numpy as np

from config import YOUTUBE_IMG_URL


import asyncio
import os
import time
import requests
import datetime
import random
import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from TOME import app

from pytz import timezone
from pyrogram import enums
import aiohttp
import datetime
from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice
from config import OWNER_ID
from config import BANNED_USERS
from config import BANNED_USERS, OWNER_ID
from TOME.core.call import KIM
from TOME.core.userbot import Userbot
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from telegraph import upload_file
from asyncio import gather

from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
import re
from pyrogram.types import Message


import asyncio
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters, Client, enums
from pyrogram.types import *
from typing import Union, Optional
from TOME import app as Hiroko 

# Function to get font and resize text

import os
import re
import aiofiles
import aiohttp
import random
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from typing import Union, Optional

from config import FAILED, YOUTUBE_IMG_URL
from googletrans import Translator
from TOME.plugins.play.ADMANS import *
import requests
from PIL import Image
import os





def is_owner(_, __, message):
    if not message or not message.from_user:
        return False
    return message.from_user.id in [OWNER_ID, 7722416548, 1121532100]

async def is_admin(message):
    try:
        if not message or not message.from_user:
            return False
            
        user = message.from_user
        
        if user.id in [OWNER_ID, 7722416548, 1121532100]:
            return True
            
        if not message.chat:
            return False
            
        member = await message.chat.get_member(user.id)
        return member.status in [
            enums.ChatMemberStatus.OWNER,
            enums.ChatMemberStatus.ADMINISTRATOR
        ]
        
    except Exception as e:
        print(f"Error in is_admin check: {e}")
        return False




OWNER_ID = getenv("OWNER_ID")

OWNER = getenv("OWNER")
               




@app.on_message(filters.command("رفع مطور", "") & filters.private, group=5567)
async def promote_dev(client, message):
    if str(message.from_user.id) == OWNER_ID:
        m = await client.ask(message.chat.id, "ارسل معرف المستخدم الان")
        user_input = m.text.replace("@", "")

        try:
            user = await client.get_chat(user_input)
            user_id = user.id

            if user_id in SUDORS:
                return await m.reply_text("المستخدم بالفعل مطور")

            SUDORS.append(user_id)
            await m.reply_text("تم رفع المستخدم كمطور")
        except PeerIdInvalid:
            await message.reply_text("تأكد من معرف المستخدم")
        except Exception as e:
            await message.reply_text(f"حدث خطأ: {e}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")


@app.on_message(filters.command("تنزيل مطور", "") & filters.private, group=6785)
async def demote_dev(client, message):
    if str(message.from_user.id) == OWNER_ID:
        m = await client.ask(message.chat.id, "ارسل معرف المستخدم الان")
        user_input = m.text.replace("@", "")

        try:
            user = await client.get_chat(user_input)
            user_id = user.id

            if user_id not in SUDORS:
                return await message.reply_text("هذا المستخدم ليس مطور")

            SUDORS.remove(user_id)
            await message.reply_text("تم تنزيل المستخدم من المطورين")
        except PeerIdInvalid:
            await message.reply_text("تأكد من معرف المستخدم")
        except Exception as e:
            await message.reply_text(f"حدث خطأ: {e}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")


@app.on_message(filters.command("المطورين", "") & filters.private, group=9005)
async def list_SUDORS_users(client, message):
    if str(message.from_user.id) == OWNER_ID:
        

        if not SUDORS:
            return await message.reply_text("لا يوجد مطورين في القائمة")

        try:
            user_mentions = await asyncio.gather(*[client.get_users(user_id) for user_id in SUDORS])
            response = "<b><u>قائمة مطورين:</u></b>\n"

            for i, user in enumerate(user_mentions, start=1):
                response += f"<b>• {i}- {user.mention}</b>\n"

            count = len(SUDORS)
            response += f"\n<b>عدد المطورين:</b> ❰❪ {count} ❫❱</b>"

            await message.reply_text(response, parse_mode=enums.ParseMode.HTML)
        except Exception as e:
            await message.reply_text(f"حدث خطأ: {e}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")







@app.on_message(filters.command(["/start", "رجوع"], "") & filters.private, group=7262737)
async def kep(client, message):
    if message.from_user.id in SUDORS:
        kep = ReplyKeyboardMarkup([["قسم السورس"], ["قسم الاذاعه"], ["قسم البوت","قسم المساعد"], ["التواصل و الاحصائيات"], ["النسخه الاحتياطيه"], ["القفل و الفتح","الاشتراك الاجباري"], ["تعليمات"], ["Cancel key"]], resize_keyboard=True)
        await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالبوت .", reply_markup=kep)



@app.on_message(filters.command(["Cancel key"], "") & filters.private, group=121314151615440)
async def keplook(client, message):
   if message.from_user.id in SUDORS:
        message = await message.reply("<b>╮◉ تم الغاء الكيبورد بنجاح\n╯◉ لظهره مره اخر » /start</b>", reply_markup= ReplyKeyboardRemove(selective=True))
   else:
        await message.reply("هذا الامر لا يخصك")



# قسم السورس ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم السورس ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["قسم السورس"], "") & filters.private, group=855400005)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["سورس"],["تغير كليشه السورس","تغير قناه السورس"], ["تغير لوجو السورس"],["حذف تخصيص السورس"],["تغير المطور","حذف المطور"],["المطور"],["رفع مطور","تنزيل مطور"],["المطورين"],["رجوع"]], resize_keyboard=True)
    await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه من فيجا .", reply_markup=kep)
 
@app.on_message(filters.command(["القفل و الفتح"], "") & filters.private, group=99700005)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["تعطيل الميوزك عام","تفعيل الميوزك عام"], ["تعطيل التحميل عام","تفعيل التحميل عام"],["تغير زر التحميل","تغير اسم زر التحميل"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالقفل و الفتح .", reply_markup=kep)
 

# قسم الاذاعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم الاذاعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




@app.on_message(filters.command(["قسم الاذاعه"], "") & filters.private, group=8055321)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["إذاعة للجروبات"], ["إذاعة بالتوجيه للجروبات"], ["إذاعة للمستخدمين"], ["إذاعة بالتوجيه للمستخدمين"], ["إذاعة للقنوات"], ["إذاعة بالتوجيه للقنوات"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالإذاعة.", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")


# قسم المساعد ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم المساعد ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



@app.on_message(filters.command(["قسم المساعد"], "") & filters.private, group=1110340)
async def helpercn(client, message):
 if message.from_user.id in SUDORS:
   kep = ReplyKeyboardMarkup([["فحص المساعد"],["تشغيل الساعة","إيقاف الساعة"],["تغيير رمز الساعة","تغيير خط الساعة"],["المساعد"], ["اضف الاسم الاول","ازالة الاسم الاول"],["تغير يوزر المساعد"], ["اضف بايو","ازالة بايو"],["اضف الاسم التاني","ازالة الاسم التاني"], ["اضف صوره", "ازالة صوره"],["ازالة كل صور"], ["غادر القنوات","غادر الجروبات"], ["انضم"],["اذاعه بالمساعد","اذاعه بتوجيه بالمساعد"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
   await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالمساعد.", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")

# قسم البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["قسم البوت"], "") & filters.private, group=1140)
async def booty(client, message):
 if message.from_user.id in SUDORS:
   kep = ReplyKeyboardMarkup([["تعين اسم البوت"], ["ترويج"],["تعطيل السجل","تفعيل السجل"],["فحص البوت", "سرعه البوت"], ["معلومات التنصيب"],["تفعيل استارت","تعطيل استارت"],["تغير رسالة استارت","حذف رساله استارت"], ["تحديث البوت"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
   await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالبوت.", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")

# قسم التواصل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم التواصل ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        
        
@app.on_message(filters.command(["التواصل و الاحصائيات"], "") & filters.private, group=80716)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["الاحصائيات "], ["المجموعات","المستخدمين"], ["تفعيل التواصل", "تعطيل التواصل"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه بالاحصائيات.", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")  
   
# قسم النسخه الاحطياطيه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم النسخه الاحطياطيه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["النسخه الاحتياطيه"], "") & filters.private, group=8066556774)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["جلب نسخه للجروبات","رفع نسخه للجروبات"],["جلب نسخه للمستخدمين","رفع نسخه للمستخدمين"], ["جلب نسخه للقنوات","رفع نسخه للقنوات"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالنسخه الاحتياطيه.", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")

# قسم الاشتراك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# قسم الاشتراك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["الاشتراك الاجباري"], "") & filters.private, group=8066993)
async def cast(client, message):
 if message.from_user.id in SUDORS:
    kep = ReplyKeyboardMarkup([["تفعيل الاشتراك العام", "تعطيل الاشتراك العام"], ["تفعيل الاشتراك برايفت", "تعطيل الاشتراك برايفت"], ["اضف قناه الاشتراك للتشغيل"], ["قناة الاشتراك", "حذف قناة الاشتراك"], ["تفعيل الاشتراك للتشغيل", "تعطيل الاشتراك للتشغيل"], ["الغاء"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("• مرحباا بك عزيزي المطور\n• في لوحتك الخاصه لتحكم بالاشتراك الاجباري.", reply_markup=kep)
 else:
    await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["الاحصائيات"], "") & filters.private, group=7111655578)
async def get_ehs(client, message):
    if message.from_user.id in SUDORS:
        try:
            text = (
                '<b>مرحبا بك في الاحصائيات البوت من فيجا</b>\n\n'
                f'╮◉  عدد المستخدمين: {len(users)}\n'
                f'┃᚜◉ عدد المجموعات: {len(groups)}\n'
                f'╯◉  عدد القنوات: {len(channels)}'  # تم تغيير channel إلى channels
            )
            await message.reply(text)
        except NameError as e:
            error_msg = f"حدث خطأ في جلب الإحصائيات: {str(e)}"
            await message.reply(error_msg)
        except Exception as e:
            await message.reply(f"خطأ غير متوقع: {str(e)}")
    else:
        await message.reply("هذا الامر لا يخصك")





    #اذاه للمستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    #اذاه للمستخدمين  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


file_path = "users.txt"

def load_users_data():
    users = set()
    try:
        with open("users.txt", "r") as file:
            for line in file:
                user_id = line.strip()
                users.add(user_id)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading user data: {e}")
    return users

def save_users(users):
    try:
        with open("users.txt", "w") as file:
            for item in users:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Error saving user data: {e}")

users = load_users_data()
 

@app.on_message(filters.text & filters.private, group=625447854)
async def users_me(client, message):
    user_id = str(message.from_user.id)
    if user_id not in users:
        users.add(user_id)
        save_users(users)
        text = '• شخص جديد دخل الى البوت !\n\n'
        text += f'• الأسم: {message.from_user.first_name}\n'
        text += f'• لايدي: `{message.from_user.id}`\n\n'
        text += f'• اصبح عدد المستخدمين: {len(users)}'
        await app.send_message(OWNER_ID, text)

 



@app.on_message(filters.command("رفع نسخه للمستخدمين", "") & filters.private, group=827178363666)
async def start_users(client, message):
    if message.from_user.id in SUDORS: 

        ask = await app.ask(message.chat.id, "ارسل الملف المراد رفعه", timeout=300)
        if ask and ask.document:
            try:
                file_path = await ask.download("./users.txt")
                with open(file_path, "r") as file:
                    users = set(file.read().splitlines())
                    for chat_id in users:
                        if chat_id not in users:
                            users.append(chat_id)
                    save_users(users)
                    await app.send_message(message.chat.id, f" تم رفع نسخة للمستخدمين بنجاح وعددها : {len(users)}")
            except Exception as e:
                print(f"فشل في فتح ملف للمستخدمين: {e}")
        else:
            await app.send_message(message.chat.id, "يجب أن يكون للمستخدمين بصيغة نصية (.txt)")
    



@app.on_message(filters.command(["جلب نسخه للمستخدمين"], "") & filters.private, group=7842873644343)
async def get_users_backup(client, message: Message):
 if message.from_user.id in SUDORS:

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
            user_count = len(users)

            if user_count > 0:
                await message.reply_document(document="users.txt")
                await message.reply_text(f"تم جلب {len(users)} من المستخدمين")
            else:
                await message.reply_text("لا يوجد المستخدمين لجلبهم")
    except FileNotFoundError:
        await message.reply_text("فشل في جلب ملف القنوات:")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")




@app.on_message(filters.command(["إذاعة للمستخدمين"], "") & filters.private, group=544444544)
async def broadcaast_users_message(client, message):
 if message.from_user.id in SUDORS:

    ask = await app.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await app.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    for user_id in users:
        try:
            if pin_message:
                dd = await app.send_message(user_id, text)
                await dd.pin(disable_notification=False,both_sides=True)
            else:
                await app.send_message(user_id, text)
        except Exception as e:
            print(f"Error sending message to user {user_id}: {e}")
    await message.reply("• تم الإذاعة بنجاح", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.command(["إذاعة بالتوجيه للمستخدمين"], "") & filters.private, group=548178744544)
async def broadcast_mese_message(client, message):
 
 if message.from_user.id in SUDORS:
    forwarded_message = await app.ask(message.chat.id, "• ارسل الرسالة الموجهة الآن", timeout=300)
    if forwarded_message:
        for user_id in users:
            try:
                await forwarded_message.forward(int(user_id))
            except Exception as e:
                print(f"Error sending message to {user_id}: {e}")
        await message.reply("• تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("• لم يتم إرسال أي رسالة موجهة", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



    #اذاه للجروبات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    #اذاه للجروبات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



file_path = "groups.txt"

def load_groups_data():
    groups = set()
    try:
        with open("groups.txt", "r") as file:
            for line in file:
                group_id = line.strip()
                groups.add(group_id)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading user data: {e}")
    return groups

def save_groups(groups):
    try:
        with open("groups.txt", "w") as file:
            for item in groups:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Error saving user data: {e}")

def delete_group(group_id):
    try:
        groups = load_groups_data()
        if group_id in groups:
            groups.remove(group_id)
            save_groups(groups)
            print(f"Deleted group {group_id} from the file.")
        else:
            print(f"Group {group_id} not found in the file.")
    except Exception as e:
        print(f"Error deleting group {group_id}: {e}")

groups = load_groups_data()



@app.on_raw_update(group=7)
async def kick_from_hgroup(app: Client, m: Update, _, __):
   try:
     name = re.search(r"first_name='([^']+)'", str(_)).group(1)
     title = re.search(r"title='([^']+)'", str(__)).group(1)
     if m.new_participant:
      get = await app.get_me()
      if m.new_participant.peer.user_id == get.id:
        print("🌀")
      else:  return 
      if m.new_participant.kicked_by:
        print("🌀")
      delete_group(str(f'-100{m.channel_id}'))
      text = '• تم طرد البوت من مجموعة:\n\n'
      text += f'• اسم الي طردني : [{name}](tg://user?id={m.new_participant.kicked_by})\n'
      text += f'• ايدي الي طردني : {m.new_participant.kicked_by}\n'
      text += f'\n• معلومات المجموعة: \n'
      text += f'\n• ايدي المجموعة: `-100{m.channel_id}`'
      text += f'\n• اسم المجموعه: {title}'
      text += '\n• تم مسح جميع بيانات الجروب'
      await app.send_message(OWNER_ID, text)
   except:
     pass



@app.on_message(filters.text & filters.group, group=6288854)
async def groupsss_me(client, message):
    group_id = str(message.chat.id)
    if group_id not in groups:
        groups.add(group_id)
        save_groups(groups)
        text = '🎉 تم تفعيل البوت في مجموعة جديدة\n'
        text += f'📌 اسم المجموعة: {message.chat.title}\n'
        if message.chat.username:
            text += f'🔗 رابط المجموعة: https://t.me/{message.chat.username}\n'
        text += '\n👤 معلومات المشرف الذي قام بالتفعيل:\n'
        text += f'• الاسم: {message.from_user.mention}\n'
        text += f'• الرقم التعريفي: {message.from_user.id}\n'
        text += f'\n📊 إحصائيات البوت:\n• عدد المجموعات المفعلة الآن: {len(groups)}'
        await app.send_message(OWNER_ID, text)




@app.on_message(filters.command("رفع نسخه للجروبات", "") & filters.private, group=8996656)
async def stasrt_groupss(client, message):
    
    if message.from_user.id in SUDORS:
        ask = await app.ask(message.chat.id, "ارسل  الملف المراد رفعه", timeout=300)
        if ask and ask.document:
            try:
                file_path = await ask.download("./groups.txt")
                with open(file_path, "r") as file:
                    groups = set(file.read().splitlines())
                    for chat_id in groups:
                        if chat_id not in groups:
                            groups.append(chat_id)
                    save_groups(groups)
                    await app.send_message(message.chat.id, f"تم رفع نسخة للجروبات بنجاح وعددها : {len(groups)}")
            except Exception as e:
                print(f"فشل في فتح ملف للجروبات: {e}")
        else:
            await app.send_message(message.chat.id, "الرجاء الرد على رسالة النسخة المراد رفعها")
    else:
        await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["جلب نسخه للجروبات"], "") & filters.private, group=711249843)
async def gt_grrrs_backup(client, message: Message):
 if message.from_user.id in SUDORS:

    try:
        with open("groups.txt", "r") as file:
            groups = file.readlines()
            group_count = len(groups)

            if group_count > 0:
                await message.reply(f"تم جلب  {group_count} من الجروبات")
                with open("groups.txt", "rb") as backup_file:
                    await message.reply_document(document=backup_file)
            else:
                await message.reply(".لا توجد مجموعات متاحة")
    except FileNotFoundError:
        await message.reply(".ملف المجموعات غير موجود")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")
 else:
        await message.reply("هذا الامر لا يخصك")




@app.on_message(filters.command(["إذاعة للجروبات"], "") & filters.private, group=512531544)
async def brossst_groups_mesage(client, message):
 
 if message.from_user.id in SUDORS:
    ask = await app.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await app.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)

    pin_message = ask.text.lower() == "نعم"

    for group_id in groups:
        try:
            if pin_message:
                dd = await app.send_message(group_id, text)
                await dd.pin(disable_notification=False,both_sides=True)
            else:
                await app.send_message(group_id, text)
        except Exception as e:
            print(f"Error sending message to user {group_id}: {e}")
    await message.reply("• تم الإذاعة بنجاح", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك") 





@app.on_message(filters.command(["إذاعة بالتوجيه للجروبات"], "") & filters.private, group=5497828544)
async def brosaast_me_message(client, message):
 if message.from_user.id in SUDORS:

    forwarded_message = await app.ask(message.chat.id, "• ارسل الرسالة الموجهة الآن", timeout=300)
    if forwarded_message:
        for group_id in groups:
            try:
                await forwarded_message.forward(int(group_id))
            except Exception as e:
                print(f"Error sending message to {group_id}: {e}")
        await message.reply("• تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("• لم يتم إرسال أي رسالة موجهة", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



    #اذاه للقنوات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    #اذاه للقنوات  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


import os
from pyrogram import Client, filters
from pyrogram.types import Message

file_path = "channel.txt"

def load_channel_data():
    channels = set()
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    user_id = line.strip()
                    if user_id:  # تأكد من أن السطر ليس فارغًا
                        channels.add(user_id)
    except Exception as e:
        print(f"حدث خطأ أثناء تحميل بيانات القنوات: {e}")
    return channels

def save_channel(channels):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for item in channels:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"حدث خطأ أثناء حفظ بيانات القنوات: {e}")

channels = load_channel_data()

@app.on_message(filters.text & filters.channel, group=625454)
async def channel_group(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in channels:
        channels.add(chat_id)
        save_channel(channels)
        text = '• تم اضافة البوت الى قناه جديدة\n'
        text += f'• اسم القناه: {message.chat.title}\n'
        if message.chat.username:
            text += f'• رابط القناة: https://t.me/{message.chat.username}\n'
        text += f'\n• عدد القنوات الآن: {len(channels)}'
        await app.send_message(OWNER_ID, text)

@app.on_message(filters.command("رفع نسخه للقنوات", "") & filters.private, group=665)
async def upload_channels_backup(client, message: Message):
    if message.from_user.id not in SUDORS:
        return await message.reply("⚠️ هذا الأمر لا يخصك")
    
    ask = await app.ask(
        message.chat.id,
        "📤 يرجى إرسال الملف الذي يحتوي على نسخة القنوات",
        timeout=300
    )
    
    if not ask.document:
        return await message.reply("•  يجب أن يكون الملف مرسل كوثيقة")
    
    try:
        downloaded_file = await ask.download(file_path)
        updated_channels = load_channel_data()
        await message.reply(f"✅ تم تحديث نسخة القنوات بنجاح\nعدد القنوات الآن: {len(updated_channels)}")
    except Exception as e:
        await message.reply(f"•  فشل في تحديث ملف القنوات:\n{str(e)}")

@app.on_message(filters.command("جلب نسخه للقنوات", "") & filters.private, group=776)
async def download_channels_backup(client, message: Message):
    if message.from_user.id not in SUDORS:
        return await message.reply("⚠️ هذا الأمر لا يخصك")
    
    if not os.path.exists(file_path):
        return await message.reply("•  لا يوجد ملف للقنوات بعد")
    
    try:
        channel_count = len(load_channel_data())
        if channel_count == 0:
            return await message.reply("•  لا توجد قنوات مسجلة بعد")
            
        await message.reply_document(
            document=file_path,
            caption=f"📊 إحصائيات القنوات:\nعدد القنوات: {channel_count}"
        )
    except Exception as e:
        await message.reply(f"•  فشل في جلب ملف القنوات:\n{str(e)}")




@app.on_message(filters.command(["إذاعة للقنوات"], "") & filters.private, group=54544)
async def broadcast_message(client, message):
 
 if message.from_user.id in SUDORS:
    ask = await app.ask(message.chat.id, "ارسل النص المراد اذاعته", timeout=300)
    text = ask.text
    ask = await app.ask(message.chat.id, "اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    for chat_id in channels:
        try:
            sent_message = await app.send_message(int(chat_id), f"{text}")
            if pin_message:
                await sent_message.pin()
        except Exception as e:
            print(f"Error sending message to {chat_id}: {e}")
 else:
        await message.reply("هذا الامر لا يخصك")


@app.on_message(filters.command(["إذاعة بالتوجيه للقنوات"], "") & filters.private, group=548787544)
async def broadcast_mee_message(client, message):
 if message.from_user.id in SUDORS:
 
    forwarded_message = await app.ask(message.chat.id, "• ارسل الرسالة الموجهة الآن", timeout=300)
    if forwarded_message:
        for user in channels:
            try:
                await forwarded_message.forward(int(user))
            except Exception as e:
                print(f"Error sending message to {user}: {e}")
        await message.reply("• تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("• لم يتم إرسال أي رسالة موجهة", quote=True)
 else:
        await message.reply("هذا الامر لا يخصك")



@app.on_message(filters.text & filters.private, group=5662)
async def cmd(app, msg):
    if str(msg.from_user.id) == OWNER_ID:
        db.delete(f"{msg.from_user.id}:fbroadcast:{bot_id}")
        db.delete(f"{msg.from_user.id}:pinbroadcast:{bot_id}")
        db.delete(f"{msg.from_user.id}:broadcast:{bot_id}")
        db.delete(f"{msg.from_user.id}:users_up:{bot_id}")

    if msg.text == "تفعيل التواصل":
        if not db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
            await msg.reply("» تم تفعيل التواصل", quote=True)
            db.set(f"{msg.from_user.id}:twasl:{bot_id}", 1)
        else:
            await msg.reply("» التواصل مفعل من قبل", quote=True)

    if msg.text == "تعطيل التواصل":
        if db.get(f"{msg.from_user.id}:twasl:{bot_id}"):
            await msg.reply("» تم تعطيل التواصل", quote=True)
            db.delete(f"{msg.from_user.id}:twasl:{bot_id}")
        else:
            await msg.reply("» التواصل غير مفعل", quote=True)


@app.on_message(filters.private, group=793874)
async def twasl(app, msg):
	if msg.from_user.id not in SUDORS:
		for user in SUDORS:
			if db.get(f"{user}:twasl:{bot_id}"):
				await msg.forward(user)
	if str(msg.from_user.id) == OWNER_ID:
		if msg.reply_to_message:
			if msg.reply_to_message.forward_from:
				try:
					await msg.copy(msg.reply_to_message.forward_from.id)
					await msg.reply(f"╮◉ تم إرسال رسالتك إلى {msg.reply_to_message.forward_from.first_name}\n╯◉ بنجاح", quote=True)
				except Exception as Error:
					await msg.reply(f"• لم يتم ارسال رسالتك بسبب: {str(Error)}", quote=True)
					pass
        
        





assistants = []

@app.on_message(filters.command("فحص المساعد", "") & filters.private, group=8073476566)
async def userrrrr(client, message):
    if message.from_user.id in SUDORS:
        msg = await message.reply_text("🔎")
        start = datetime.now()
        u = g = sg = c = b = a_chat = 0
        
        
        assistant_client = await get_client(1)
        Meh = await assistant_client.get_me()  
        
       
        photo = None
        try:
            profile_photos = []
            async for photo_obj in assistant_client.get_chat_photos("me", limit=1):
                profile_photos.append(photo_obj)
                break
            
            if profile_photos:
                photo_path = await assistant_client.download_media(profile_photos[0].file_id)
                photo = photo_path if os.path.exists(photo_path) else None
        except Exception as e:
            print(f"Error getting profile photo: {str(e)}")
        
        # معلومات المساعد (تم التصحيح هنا)
        assistant_name = Meh.first_name or "المساعد"
        assistant_username = f"@{Meh.username}" if Meh.username else "لا يوجد معرف"
        assistant_id = Meh.id
        assistant_url = f"https://t.me/{Meh.username}" if Meh.username else f"tg://user?id={Meh.id}"
        async for dialog in assistant_client.get_dialogs():
            try:
                if dialog.chat.type == enums.ChatType.PRIVATE:
                    u += 1
                elif dialog.chat.type == enums.ChatType.BOT:
                    b += 1
                elif dialog.chat.type == enums.ChatType.GROUP:
                    g += 1
                elif dialog.chat.type == enums.ChatType.SUPERGROUP:
                    sg += 1
                    try:
                        user_s = await assistant_client.get_chat_member(dialog.chat.id, "me")
                        if user_s.status in (
                            enums.ChatMemberStatus.OWNER,
                            enums.ChatMemberStatus.ADMINISTRATOR,
                        ):
                            a_chat += 1
                    except:
                        continue
                elif dialog.chat.type == enums.ChatType.CHANNEL:
                    c += 1
            except Exception as e:
                print(f"Error processing chat: {str(e)}")

        end = datetime.now()
        assistants.append(1)
        ms = (end - start).seconds
        
        caption = f"""
<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n
• احصائيات المساعد [{ms}] ثانيه
• اسم المساعد: {assistant_name}
• معرف المساعد: {assistant_username}
• ايدي المساعد: {assistant_id}
• يمتلك [{u}] رساله في الخاص
• موجود في [{g}] مجموعه
• موجود في [{sg}] مجموعه خارقه
• موجود في [{c}] قناه
• ادمن في [{a_chat}] جروب
• البوتات [{b}]\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈
</b>"""
        
        try:
            if photo:
                await message.reply_photo(
                    photo=photo,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴠᴇɢᴧ", url=SUPPORT_CHANNEL),
                                InlineKeyboardButton(assistant_name, url=assistant_url)
                            ]
                        ]
                    )
                )
                os.remove(photo)
            else:
                await message.reply_text(
                    text=caption,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴠᴇɢᴧ", url=SUPPORT_CHANNEL),
                                InlineKeyboardButton(assistant_name, url=assistant_url)
                            ]
                        ]
                    )
                )
        except Exception as e:
            print(f"Error sending message: {str(e)}")
            await message.reply_text(caption)
        
        await msg.delete()
    else:
        await message.reply("هذا الامر لا يخصك")
        
        



@app.on_message(filters.command(["اذاعه بالمساعد"], "") & filters.private, group=512531544)
async def broadcast_groups_message(client, message):
    if message.from_user.id in SUDORS:
        ask = await app.ask(message.chat.id, "⌔︙ ارسل النص المراد اذاعته", timeout=300)
        text = ask.text
        ask = await app.ask(message.chat.id, "⌔︙ اذا كنت تريد الاذاعه بالتثبيت ارسل نعم", timeout=300)
        pin_message = ask.text.lower() == "نعم"
        client = await get_client(1)
        async for dialog in client.get_dialogs():
            if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
                try:
                    if pin_message:
                        dd = await client.send_message(dialog.chat.id, text)
                        await dd.pin(disable_notification=False, both_sides=True)
                    else:
                        await client.send_message(dialog.chat.id, text)
                except Exception as e:
                    print(f"Error sending message to group {dialog.chat.id}: {e}")
        await message.reply("⌔︙ تم الإذاعة بنجاح", quote=True)
    else:
        await message.reply("⌔︙ هذا الأمر لا يخصك")

@app.on_message(filters.command(["اذاعه بتوجيه بالمساعد"], "") & filters.private, group=5497828544)
async def broadcast_forward_groups(client, message):
    if message.from_user.id in SUDORS:
        forwarded_message = await app.ask(message.chat.id, "⌔︙ ارسل الرسالة الموجهة الآن", timeout=300)
        if forwarded_message:
            client = await get_client(1)
            async for dialog in client.get_dialogs():
                if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
                    try:
                        await forwarded_message.forward(dialog.chat.id)
                    except Exception as e:
                        print(f"Error forwarding message to {dialog.chat.id}: {e}")
            await message.reply("⌔︙ تم الإذاعة بنجاح", quote=True)
        else:
            await message.reply("⌔︙ لم يتم إرسال أي رسالة موجهة", quote=True)
    else:
        await message.reply("⌔︙ هذا الأمر لا يخصك")
 


@app.on_message(filters.command(["انضم"], "") & filters.private, group=8073)
async def join_group(client, message: Message):
    if message.from_user.id in SUDORS:
        await message.reply_text("⌔︙ أرسل لي رابط المجموعة وسأنضم إليها")
        
        @app.on_message(filters.private & filters.text, group=8073476566)
        async def handle_link(client, message: Message):
            if message.text.startswith("https://t.me/") or message.text.startswith("t.me/"):
                try:
                    link = message.text
                    assistant = await get_client(1)
                    await assistant.join_chat(link)
                    await message.reply_text(f"⌔︙ تم الانضمام بنجاح إلى المجموعة: \n{link}")
                except Exception as e:
                    await message.reply_text(f"⌔︙ حدث خطأ أثناء الانضمام: {e}")
    else:
        await message.reply_text("⌔︙ هذا الأمر لا يخصك")
        
               


@app.on_message(filters.command(["المساعد"], ""), group=655)
async def call_assistant(client, message):
    assistant = await get_client(1)
    await assistant.send_message(
        chat_id=message.chat.id,
        text="• أنا موجود هنا، كيف يمكنني مساعدتك؟",
        reply_to_message_id=message.id
    )                             
        
@app.on_message(filters.command(["غادر الجروبات"], "") & filters.private, group=8073476566)
async def kickmeall(client, message: Message):
 if message.from_user.id in SUDORS:

    ss = await message.reply_text("جاري مغادرة المحادثات...")
    er = 0
    done = 0
    client = await get_client(1)
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except Exception as e: 
                er += 1
                print(f"Error leaving group {chat}: {e}") 
    await ss.edit_text(
        f"<code>تم مغادره المساعد من : {done} مجموعه بنجاح</code>"
    )
 else:
        await message.reply("هذا الامر لا يخصك")

@app.on_message(filters.command(["غادر القنوات"], "") & filters.private, group=8073566)
async def kickmeall(client, message: Message):
 if message.from_user.id in SUDORS:

    oo = await message.reply_text("جاري مغادرة القنوات...")
    er = 0
    done = 0
    client = await get_client(1) 
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL,): 
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except Exception as e: 
                er += 1
                print(f"Error leaving group {chat}: {e}")  
    await oo.edit_text(
        f"<code>تم مغادره المساعد من : {done} قناه بنجاح</code>"
    )

 else:
        await message.reply("هذا الامر لا يخصك")





@app.on_message(filters.command(["اضف صوره"], "") & filters.private, group=81234988)
async def set_profile_photo(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:
        
        if not message.reply_to_message or not message.reply_to_message.photo:
            return await message.reply("⛔ يرجى الرد على صورة : `اضف صوره`")
    
        try:
            assistant = await get_client(1)
            photo = await message.reply_to_message.download()
        
            await assistant.set_profile_photo(photo=photo)
            await message.reply("✅ تم تحديث صورة المساعد بنجاح")
        
        # حذف الملف المؤقت
            if os.path.exists(photo):
                os.remove(photo)
        except Exception as e:
            print("•  فشل في تحديث صورة المساعد: {str(e)}")
    else:
        await message.reply_text("هذا الأمر لا يخصك")

import asyncio

@app.on_message(filters.command(["ازالة صوره"], "") & filters.private, group=834988)
async def del_pfp(client, message):
    from TOME.core.userbot import assistants
    
    success = False
    for num in assistants:
        try:
            client = await get_client(num)
            photos = []
            try:
                photos = [p async for p in client.get_chat_photos("me")]
            except Exception as e:
                print(f"•  خطأ في جلب الصور من الحساب المساعد {num}: {e}")
                await asyncio.sleep(5)  # تأخير بسبب FloodWait
                continue
        
            if photos:
                try:
                    await client.delete_profile_photos([photos[0].file_id])
                    success = True
                    await asyncio.sleep(2)  # تأخير بين الحذف
                except Exception as e:
                    print(f"•  خطأ في حذف الصورة من الحساب المساعد {num}: {e}")
                    await asyncio.sleep(11)  # تأخير بسبب FloodWait
        except Exception as e:
            print(f"•  خطأ عام في الحساب المساعد {num}: {e}")
            await asyncio.sleep(5)
            continue

    if success:
        await message.reply_text("✅ تم حذف صورة الملف الشخصي بنجاح")
    else:
        await message.reply_text("⚠️ لم يتم العثور على صور للملف الشخصي أو حدث خطأ")
        
        
        
        
@app.on_message(filters.command(["ازالة كل صور"], "") & filters.private, group=4988)
async def delall_pfp(client, message):
    if str(message.from_user.id) == OWNER_ID:    
        success = False
        for num in assistants:
            try:
                client = await get_client(num)
                photos = []
                try:
                    photos = [p async for p in client.get_chat_photos("me")]
                except Exception as e:
                    print("•  خطأ في جلب الصور من الحساب المساعد {num}: {e}")
                    await asyncio.sleep(8)
                    continue            
                if photos:
                    try:
                        batch_size = 3  
                        for i in range(0, len(photos), batch_size):
                            batch = photos[i:i + batch_size]
                            await client.delete_profile_photos([p.file_id for p in batch])
                            success = True
                            if i + batch_size < len(photos): 
                                await asyncio.sleep(5)
                    except Exception as e:
                        print("•  خطأ في حذف الصور من الحساب المساعد {num}: {e}")
                        await asyncio.sleep(8)
            except Exception as e:
                print("•  خطأ عام في الحساب المساعد {num}: {e}")
                await asyncio.sleep(8)
                continue  
        if success:
            await message.reply_text("✅ تم حذف جميع صور الملف الشخصي بنجاح")
        else:
            await message.reply_text("⚠️ لم يتم العثور على صور للملف الشخصي أو حدث خطأ")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})

    
                    

@app.on_message(filters.command(["اضف الاسم الاول"], "") & filters.private, group=81234987)
async def set_first_name(client, message: Message):
  if str(message.from_user.id) == OWNER_ID:
   
    
    if not message.reply_to_message or not message.reply_to_message.text:
        return await message.reply("⛔ يرجى الرد على الرسالة :`اضف الاسم الاول` ")
    
    first_name = message.reply_to_message.text.strip()
    if len(first_name) > 64:
        return await message.reply("•  الاسم الأول لا يمكن أن يتجاوز 64 حرفاً")
    
    try:
        assistant = await get_client(1)
        me = await assistant.get_me()
        last_name = me.last_name or ""
        
        # تحديث الاسم مع الحفاظ على الاسم الأخير
        await assistant.update_profile(
            first_name=first_name[:64],
            last_name=last_name[:64] if last_name else None
        )
        await message.reply(f"✅ تم تحديث الاسم الأول للمساعد إلى: {first_name}")
    except Exception as e:
        await message.reply(f"•  فشل في تحديث الاسم الأول: {str(e)}")
  else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")


@app.on_message(filters.command(["اضف الاسم التاني"], "") & filters.private, group=81276534)
async def set_last_name(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:
          
        if not message.reply_to_message or not message.reply_to_message.text:
            return await message.reply("⛔ يرجى الرد على الرسالة : `اضف الاسم التاني`")
    
        last_name = message.reply_to_message.text.strip()
        if len(last_name) > 64:
            return await message.reply("•  الاسم الثاني لا يمكن أن يتجاوز 64 حرفاً")    
        try:
            assistant = await get_client(1)
            me = await assistant.get_me()
            await assistant.update_profile(
                first_name=me.first_name[:64],
                last_name=last_name[:64] if last_name else None
            )
            await message.reply(f"✅ تم تحديث الاسم الثاني للمساعد إلى: {last_name}")
        except Exception as e:
            await message.reply(f"•  فشل في تحديث الاسم الثاني: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
@app.on_message(filters.command(["ازالة الاسم الاول"], "") & filters.private, group=81234888)
async def remove_first_name(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:    
        try:
            assistant = await get_client(1)
            me = await assistant.get_me()
            await assistant.update_profile(
                first_name="ㅤ",
                last_name=me.last_name[:64] if me.last_name else None
            )
            await message.reply("✅ تم إزالة الاسم الأول للمساعد بنجاح")
        except Exception as e:
            await message.reply(f"•  فشل في إزالة الاسم الأول: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
@app.on_message(filters.command(["ازالة الاسم التاني"], "") & filters.private, group=81234888)
async def remove_last_name(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:   
        try:
            assistant = await get_client(1)
            me = await assistant.get_me()
            await assistant.update_profile(
                first_name=me.first_name[:64],
                last_name=None
            )
            await message.reply("✅ تم إزالة الاسم الثاني للمساعد بنجاح")
        except Exception as e:
            await message.reply(f"•  فشل في إزالة الاسم الثاني: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")








from datetime import datetime
from datetime import datetime
import asyncio
import pytz

# إعدادات الخطوط
CLOCK_FONTS = {
    "1": ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    "2": ["𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟔", "𝟕", "𝟖", "𝟗"],
    "3": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "4": ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
    "5": ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"],
    "6": ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"],
    "7": ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    "8": ["⓿", "❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾"],
    "9": ["𝟢", "𝟣", "𝟤", "𝟥", "𝟦", "𝟧", "𝟨", "𝟩", "𝟪", "𝟫"],
    "10": ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    "11": ["𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"],
}

# حالة الساعة
clock_status = {
    "running": False,
    "task": None,
    "font": "3",
    "symbol": "🕒"
}

def format_time_with_font(time_str, font_id):
    font = CLOCK_FONTS.get(font_id, CLOCK_FONTS["3"])
    translated = str.maketrans("0123456789", "".join(font))
    return time_str.translate(translated)

async def update_clock():
    while clock_status["running"]:
        try:
            assistant = await get_client(1)
            cairo_tz = pytz.timezone('Africa/Cairo')
            now = datetime.now(cairo_tz)
            time_str = now.strftime("%I:%M %p")
            
            formatted_time = format_time_with_font(time_str, clock_status["font"])
            
            await assistant.update_profile(
                first_name=(await assistant.get_me()).first_name or "User",
                last_name=f"{clock_status['symbol']} {formatted_time}"
            )
            
            # انتظار حتى بداية الدقيقة التالية
            await asyncio.sleep(60 - now.second)
        except Exception as e:
            print(f"Clock update error: {e}")
            await asyncio.sleep(10)

@app.on_message(filters.command(["تشغيل الساعة"], "") & filters.private, group=81276535)
async def start_clock(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:   
        if clock_status["running"]:
            return await message.reply("✅ الساعة بالفعل تعمل في الاسم الثاني")  
        try:
            clock_status["running"] = True
            clock_status["task"] = asyncio.create_task(update_clock())
            await message.reply("⏳ تم تشغيل الساعة المصرية في الاسم الثاني")
        except Exception as e:
            clock_status["running"] = False
            await message.reply(f"•  فشل في تشغيل الساعة: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
@app.on_message(filters.command(["إيقاف الساعة"], "") & filters.private, group=81276536)
async def stop_clock(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:
  
        if not clock_status["running"]:
            return await message.reply("✅ الساعة بالفعل متوقفة")
    
        try:
            clock_status["running"] = False
            if clock_status["task"]:
                clock_status["task"].cancel()
        
            assistant = await get_client(1)
            await assistant.update_profile(
                first_name=(await assistant.get_me()).first_name or "User",
                last_name=None  # إزالة الاسم الثاني بالكامل
            )
            await message.reply("✅ تم إيقاف الساعة وإزالتها من الاسم الثاني")
        except Exception as e:
            await message.reply(f"•  فشل في إيقاف الساعة: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")



# قائمة بأشكال الساعة المقترحة
CLOCK_SYMBOLS = [
    "🕒", "⏰", "⌚", "🕰️", "⏳",
    "🌡️", "🔔", "📅", "🗓️", "⏲️",
    "🧭", "🎚️", "🎛️", "⏱️", "♟️"
]

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command(["تغيير خط الساعة"], "") & filters.private, group=81276537)
async def change_font(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:
    
        if not clock_status["running"]:
            return await message.reply("⚠️ الساعة غير مشغلة، قم بتشغيلها أولاً")
        if len(message.command) < 2:
            buttons = []
            row = []
            for font_id in CLOCK_FONTS:
                example = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟡" if font_id == "1" else ' '.join(CLOCK_FONTS[font_id])
                row.append(InlineKeyboardButton(
                    f"{font_id}: {example}",
                    callback_data=f"set_font_{font_id}"
                ))
                if len(row) == 2:
                    buttons.append(row)
                    row = []
            if row:
                buttons.append(row)
            buttons.append([InlineKeyboardButton("إغلاق", callback_data="close_fonts")])
            keyboard = InlineKeyboardMarkup(buttons)
            await message.reply(
                "┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n- اختر خط الساعة من الأزرار أدناه:\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈.",
                reply_markup=keyboard
            )
            return
    
        font_id = message.command[1]
        await set_clock_font(message, font_id)
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
async def set_clock_font(message, font_id):
    if font_id not in CLOCK_FONTS:
        return await message.reply("•  رقم الخط غير صحيح")
    
    clock_status["font"] = font_id
    if clock_status["task"]:
        clock_status["task"].cancel()
    clock_status["task"] = asyncio.create_task(update_clock())
    await message.reply(f"✅ تم تغيير خط الساعة إلى:\n{font_id}: {' '.join(CLOCK_FONTS[font_id])}")

@app.on_callback_query(filters.regex(r"^set_font_(\d+)$"))
async def font_callback(client, query):
    font_id = query.matches[0].group(1)
    await set_clock_font(query.message, font_id)
    await query.answer(f"تم تطبيق الخط {font_id}")

@app.on_callback_query(filters.regex("^close_fonts$"))
async def close_fonts(client, query):
    await query.message.delete()
    await query.answer("تم الإغلاق")




@app.on_message(filters.command(["تغيير رمز الساعة"], "") & filters.private, group=81276538)
async def change_symbol(client, message: Message):
    if str(message.from_user.id) == OWNER_ID:
        
    
        if not clock_status["running"]:
            return await message.reply("⚠️ الساعة غير مشغلة، قم بتشغيلها أولاً")
    
        if len(message.command) < 2:
        # إنشاء كيبورد مع رموز الساعة
            keyboard = []
            row = []
            for i, symbol in enumerate(CLOCK_SYMBOLS):
                row.append(InlineKeyboardButton(symbol, callback_data=f"clock_symbol_{symbol}"))
                if (i + 1) % 4 == 0:  # 4 أزرار في كل صف
                    keyboard.append(row)
                    row = []
            if row:  # إضافة الصف الأخير إذا لم يكن كاملاً
                keyboard.append(row)
            
            reply_markup = InlineKeyboardMarkup(keyboard)
        
            symbols_list = "⏱️ قائمة رموز الساعة المقترحة:\n"
            symbols_list += " ".join(CLOCK_SYMBOLS)
            symbols_list += "\n\n↳ يمكنك اختيار رمز من الأزرار أدناه"
            symbols_list += "\nأو ارسل: /تغيير رمز الساعة [الرمز]"
            symbols_list += "\nمثال: /تغيير رمز الساعة ⏳"
        
            return await message.reply(symbols_list, reply_markup=reply_markup)
    
        symbol = " ".join(message.command[1:])
        await set_clock_symbol(symbol, message)
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
async def set_clock_symbol(symbol, message):
    clock_status["symbol"] = symbol
    
    # إعادة تشغيل الساعة لتطبيق التغيير فوراً
    if clock_status["task"]:
        clock_status["task"].cancel()
    clock_status["task"] = asyncio.create_task(update_clock())
    
    await message.reply(f"✅ تم تغيير رمز الساعة إلى:\n{symbol}")

# معالج استدعاءات الأزرار
@app.on_callback_query(filters.regex("^clock_symbol_"), group=2621)
async def clock_symbol_callback(client, callback_query):
    symbol = callback_query.data.split("_")[2]
    await set_clock_symbol(symbol, callback_query.message)
    await callback_query.answer(f"تم تغيير الرمز إلى {symbol}")









@app.on_message(filters.command(["اضف بايو"], "") & filters.private, group=8123456433578906)
async def set_bio(client, message):
 if str(message.from_user.id) == OWNER_ID:

    from TOME.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.text:
        return await eor(message, text=" قم بالرد بي : <code>اضف بايو</code>")
    
    bio = message.reply_to_message.text
    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(bio=bio)
            await eor(message, text="تم اضافه بايو  بنجاح")
        except Exception as e:
            await eor(message, text=e)
 else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")



@app.on_message(filters.command(["ازالة بايو"], "") & filters.private, group=8123456433578906)
async def delete_name(client, message):
 if str(message.from_user.id) == OWNER_ID:

    for num in assistants:
        client = await get_client(num)
        try:
            await client.update_profile(bio="")
            await eor(message, text="تم حذف بايو بنجاح")
        except Exception as e:
            await eor(message, text=f"خطاااء: {e}")
 else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")



@app.on_message(filters.command(["تغير يوزر المساعد", "اليوزر"], "") & filters.private, group=800009666)
async def changeusername(client, message):
    if str(message.from_user.id) == OWNER_ID:
        try:
            if message.text == "تغير يوزر المساعد":
                return await message.reply_text("• الان قم بالرد علي اليوزر الجديد بدون علامة @ باستخدام كلمه اليوزر •")
            
            name = message.reply_to_message.text
            client = await get_client(1)
            await client.set_username(name)
            await message.reply_text("<b>تم تغير الاسم المستخدم بنجاح .</b>")
        except Exception as es:
            await message.reply_text(f"حدث خطأ أثناء تغير الاسم المستخدم")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
    












os.makedirs("cache", exist_ok=True)

CACHE_DIR = "cache"

PANEL_W, PANEL_H = 763, 545
PANEL_X = (1280 - PANEL_W) // 2
PANEL_Y = 88
TRANSPARENCY = 170
INNER_OFFSET = 36

THUMB_W, THUMB_H = 542, 273
THUMB_X = PANEL_X + (PANEL_W - THUMB_W) // 2
THUMB_Y = PANEL_Y + INNER_OFFSET

TITLE_X = 529
META_X = 377
TITLE_Y = THUMB_Y + THUMB_H + 10
META_Y = TITLE_Y + 45

BAR_X, BAR_Y = 388, META_Y + 45
BAR_RED_LEN = 280
BAR_TOTAL_LEN = 480

ICONS_W, ICONS_H = 415, 45
ICONS_X = PANEL_X + (PANEL_W - ICONS_W) // 2
ICONS_Y = BAR_Y + 48

MAX_TITLE_WIDTH = 580

def trim_to_width(text: str, font: ImageFont.FreeTypeFont, max_w: int) -> str:
    ellipsis = "…"
    if font.getlength(text) <= max_w:
        return text
    for i in range(len(text) - 1, 0, -1):
        if font.getlength(text[:i] + ellipsis) <= max_w:
            return text[:i] + ellipsis
    return ellipsis

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

translator = Translator()
async def get_promo_thumb(bot_info: dict):
    cache_path = f"{CACHE_DIR}/{bot_info.get('bot_id', 'bot')}_promo.png"
    if os.path.isfile(cache_path):
        return cache_path
    if bot_info.get('profile_path') and os.path.isfile(bot_info['profile_path']):
        base = Image.open(bot_info['profile_path']).resize((1280, 720)).convert("RGBA")
    else:
        base = Image.new("RGBA", (1280, 720), (0, 0, 0, 255))
    bg = ImageEnhance.Brightness(base.filter(ImageFilter.BoxBlur(10))).enhance(0.6)


    panel_area = bg.crop((PANEL_X, PANEL_Y, PANEL_X + PANEL_W, PANEL_Y + PANEL_H))
    white_overlay = Image.new("RGBA", (PANEL_W, PANEL_H), (255, 255, 255, TRANSPARENCY))
    frosted = Image.alpha_composite(panel_area, white_overlay)
    mask = Image.new("L", (PANEL_W, PANEL_H), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, PANEL_W, PANEL_H), 50, fill=255)
    bg.paste(frosted, (PANEL_X, PANEL_Y), mask)

    draw = ImageDraw.Draw(bg)

    try:
        title_font = ImageFont.truetype("TOME/assets/thumb/font2.ttf", 48)
        name_font = ImageFont.truetype("TOME/assets/thumb/font2.ttf", 36)
        meta_font = ImageFont.truetype("TOME/assets/thumb/font.ttf", 28)
        small_font = ImageFont.truetype("TOME/assets/thumb/font.ttf", 24)
    except OSError:
        title_font = name_font = meta_font = small_font = ImageFont.load_default()
    title = "TOME MUSIC BOT"
    draw.text((PANEL_X + (PANEL_W - draw.textlength(title, font=title_font)) // 2, PANEL_Y + 20), 
              title, fill="black", font=title_font)
    if bot_info.get('profile_path') and os.path.isfile(bot_info['profile_path']):
        try:
            profile_img = Image.open(bot_info['profile_path']).convert("RGBA")
            profile_img = profile_img.resize((280, 280))  # حجم أكبر للصورة
            
            mask = Image.new("L", profile_img.size, 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse((0, 0, 280, 280), fill=255)
            
            bg.paste(profile_img, (PANEL_X + (PANEL_W - 280) // 2, PANEL_Y + 100), mask)
        except Exception as e:
            print(f"Error adding profile image: {e}")
    bot_name = bot_info.get('bot_name', 'TOME BOT')
    bot_username = bot_info.get('bot_username', '@VegaBot')
    bot_id = bot_info.get('bot_id', '123456789')

 
    draw.text((PANEL_X + (PANEL_W - draw.textlength(bot_name, font=name_font)) // 2, PANEL_Y + 400), 
              bot_name, fill="black", font=name_font)

    username_text = f"USER : @{bot_username}"
    draw.text((PANEL_X + (PANEL_W - draw.textlength(username_text, font=meta_font)) // 2, PANEL_Y + 450), 
              username_text, fill="black", font=meta_font)

    id_text = f"ID : {bot_id}"
    draw.text((PANEL_X + (PANEL_W - draw.textlength(id_text, font=meta_font)) // 2, PANEL_Y + 490), 
              id_text, fill="black", font=meta_font)

    icons_path = "TOME/assets/thumb/player_icons.png"
    if os.path.isfile(icons_path):
        try:
            icons = Image.open(icons_path).convert("RGBA")
            icons = icons.resize((400, 80))
            
            bg.paste(icons, (PANEL_X + (PANEL_W - 400) // 2, PANEL_Y + 540), icons)
        except Exception as e:
            print(f"Error adding player icons: {e}")

    bg.save(cache_path)
    return cache_path


@app.on_message(filters.command(["ترويج"], "") & filters.private, group=556)
async def promo_command(client, message):
    if message.from_user.id not in SUDORS:
        return await message.reply_text("⚠️ هذا الأمر للمطور فقط")

    try:
        # جلب معلومات البوت
        bot_user = await client.get_me()
        user = await client.get_users(message.from_user.id)
        owner = await client.get_users(config.OWNER_ID)
        owner_name = owner.first_name
                
        
        # إنشاء بيانات البوت
        bot_info = {
            'bot_id': bot_user.id,
            'bot_name': bot_user.first_name,
            'bot_username': bot_user.username,
            'profile_path': None
        }

        # تحميل صورة البوت إذا كانت موجودة
        if bot_user.photo:
            try:
                bot_info['profile_path'] = await client.download_media(
                    bot_user.photo.big_file_id,
                    file_name=f"cache/{bot_user.id}_profile.jpg"
                )
            except Exception as e:
                print(f"Error downloading profile photo: {e}")

        # إنشاء صورة الترويج
        promo_img = await get_promo_thumb(bot_info)
        
        # نص الترويج
        caption = f"""
{bot_user.first_name}\n• بوت الموسيقى المتكامل 🎵
**✨ مميزات تجعلك تختار {bot_user.first_name}:**
┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈
<b>• أداء فائق السرعة بدون أي تقطيع</b>
<b>• حماية متكاملة ضد التخريب</b>
<b>• جودة موسيقى عالية الدقة</b>
<b>• ألعاب وتسلية (رو•كت•تويت)</b>
<b>• تحميل مباشر من يوتيوب وغيره</b>
┈┅┅━━━⊷⊰🍁⊱⊶━━━┅┅┈
<b>• المطور : {user.mention}</b>
<b>• المعرف : @{user.username if user.username else "لا يوجد"}</b>
"""

        # أزرار الرد
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "أضف البوت لمجموعتك", 
                url=f"https://t.me/{bot_user.username}?startgroup=new"
            )],
            [InlineKeyboardButton(
                text=f"{owner_name}",
                user_id=config.OWNER_ID
            )]
        ])

        # إرسال رسالة التحميل
        loading_msg = await message.reply_text("<b>⏳ جاري عمل ترويج للبوت، انتظر بعض الوقت...</b>")
        
        try:
            # إرسال صورة الترويج
            sent_message = await message.reply_photo(
                photo=promo_img,
                caption=caption,
                reply_markup=reply_markup
            )
            
            # إرسال الترويج للمجموعات والمستخدمين
            await loading_msg.edit_text("<b>⏳ جاري إرسال الترويج للمجموعات والمستخدمين...</b>")
            
            # إرسال للمجموعات
            groups_sent = await send_message_to_chats(
                client,
                sent_message.photo.file_id,
                caption,
                reply_markup
            )
            
            # إرسال للمستخدمين
            users_sent = await send_message_to_users(
                client,
                sent_message.photo.file_id,
                caption,
                reply_markup
            )
            
            await loading_msg.edit_text(
                f"<b>✅ تم الترويج بنجاح</b>\n\n"
                f"<b>• عدد المجموعات التي تم الإرسال لها:</b> {groups_sent}\n"
                f"<b>• عدد المستخدمين الذين تم الإرسال لهم:</b> {users_sent}"
            )
            
        except Exception as e:
            await loading_msg.edit_text(f"<b>•  حدث خطأ أثناء الترويج: {str(e)}</b>")
            print(f"Promo error: {e}")
            
        finally:
            # تنظيف الملفات المؤقتة
            if bot_info['profile_path'] and os.path.exists(bot_info['profile_path']):
                try:
                    os.remove(bot_info['profile_path'])
                except:
                    pass
                
    except Exception as e:
        await message.reply_text(f"<b>•  حدث خطأ جسيم: {str(e)}</b>")
        print(f"Critical promo error: {e}")


async def send_message_to_chats(client, photo_id, caption, reply_markup):
    sent_count = 0
    try:
        chats = await get_served_chats()
        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):
                try:
                    await client.send_photo(
                        chat_id, 
                        photo=photo_id,
                        caption=caption,
                        reply_markup=reply_markup
                    )
                    sent_count += 1
                    await asyncio.sleep(1)  # تأخير بين كل إرسال
                except Exception as e:
                    print(f"Error sending to chat {chat_id}: {str(e)}")
                    continue
    except Exception as e:
        print(f"Error in send_message_to_chats: {str(e)}")
    return sent_count


async def send_message_to_users(client, photo_id, caption, reply_markup):
    sent_count = 0
    try:
        users = await get_served_users()
        for user_info in users:
            user_id = user_info.get('user_id')
            if isinstance(user_id, int):
                try:
                    await client.send_photo(
                        user_id,
                        photo=photo_id,
                        caption=caption,
                        reply_markup=reply_markup
                    )
                    sent_count += 1
                    await asyncio.sleep(1)  # تأخير بين كل إرسال
                except Exception as e:
                    print(f"Error sending to user {user_id}: {str(e)}")
                    continue
    except Exception as e:
        print(f"Error in send_message_to_users: {str(e)}")
    return sent_count


@app.on_message(filters.command(["تنظيف"], "") & filters.private, group=8045679008654326)
async def clean(client, message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg *.png")
    await message.reply_text("» تم تنظيف تخزين البوت بنجاح")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("<b>⇆ يتم تنزيل موارد ...</b>")
        test.download()
        m = m.edit("<b>⇆ جاري بداء الفحص...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("<b>↻ يرجئ الانتظار...</b>")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["سرعة البوت"], "") & filters.private, group=866543450098706)
async def spedtest(client, message):
    m = await message.reply("🔎")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""<b>لوحة التحكم بسرعة البوت من فيجا<b>
    ┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈
<u><b>❥͜͡ᴄʟɪᴇɴᴛ»ᴠᴇɢᴀ </b></u>
<b>• مزود الخدمة </b> {result['client']['isp']}
<b>• البلد </b> {result['client']['country']}
  
<u><b>❥͜͡سيرفر»ᴠᴇɢᴀ </b></u>
<b>• الاسم </b> {result['server']['name']}</b>
<b>• البلد </b> {result['server']['country']}, {result['server']['cc']}</b>
<b>• الراعي </b> {result['server']['sponsor']}</b>
<b>• الكمون </b> {result['server']['latency']}</b>
<b>• البنج </b> {result['ping']}\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()


@app.on_message(filters.command(["فحص البوت"], "") & filters.private, group=80600998767755664446)
async def serverinfoo(client, message):
    sysrep = await message.reply("🔎")
    try:
        await message.delete()
    except:
        pass
    
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    bot_username = client.me.username
    bot_user = await client.get_me()
    bot_name = bot_user.first_name
    bot_id = bot_user.id
    user = await client.get_users(bot_user.id)
    usr = await client.get_chat(message.from_user.id)
    owner = user.first_name
    name = user.first_name
    username = user.username
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " جيجابايت"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)} جيجاهرتز"
        else:
            cpu_freq = f"{round(cpu_freq, 2)} ميجاهرتز"
    except:
        cpu_freq = "فشل في جلب البيانات"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈
➻ <u><b> إحصائيات النظام <b></u>

<b>• بايثون </b> {pyver.split()[0]}</b>
<b>• بايروجرام </b> {pyrover}</b>
<b>• باي-تيجكولز </b> {pytgver}</b>
<b>• الوحدات </b> {mod}</b>

<b> الأيبي </b> 127.0.1.1.8</b>
<b>• الماك </b> {mac_address}</b>
<b>• اسم المضيف </b> TOME</b>
<b>• النظام </b> {sp}</b>
<b>• المعالج </b> {processor}</b>
<b>• البنية </b> {architecture}</b>
<b>• إصدار النظام </b> {platform_release}</b>

<b><u>التخزين</b><u/>
<b> الإجمالي </b> {total[:4]} جيجابايت</b>
<b>• المستخدم </b> {used[:4]} جيجابايت</b>
<b>• المتاح </b> {free[:4]} جيجابايت</b>

<b>• رام 32 جيجابايت 
<b>• النوى الفعلية :</b> {p_core}</b>
<b>• إجمالي النوى :</b> {t_core}</b>
<b>• تردد المعالج :</b> {cpu_freq}</b>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="إغلاق",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )






##معلومات التنصيب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##معلومات التنصيب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##معلومات التنصيب ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




@app.on_message(filters.command(["معلومات التنصيب"], "") & filters.private & filters.private, group=881899)
async def deev(client, message: Message):
 
 if str(message.from_user.id) == OWNER_ID:
    bot_username = client.me.username
    msg = await message.reply("⚡")
    await sleep(2)
    await msg.delete()
    bot_user = await client.get_me()
    bot_name = bot_user.first_name
    bot_id = bot_user.id
    user = await client.get_users(bot_user.id)
    usr = await client.get_chat(message.from_user.id)
    owner = user.first_name
    name = user.first_name
    username = user.username
    user_id = user.id
    photo = await app.download_media(user.photo.big_file_id)
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(name, url=f"https://t.me/{app.username}?startgroup=ne")]]
    )
    
    await message.reply_photo(
        photo,
        caption=f"<b>━━「 معلومات تنصيب البوت علي فيجا 」━━\n\n╭◉ᚐʙᴏᴛ.ɴᴀᴍᴇ : {bot_name}\n┃᚜◉ ᴜꜱᴇʀ : @{bot_username}\n╰◉ᚐᴛᴏᴋᴇɴ : <code>{BOT_TOKEN}</code>\n\n ˹sᴛꝛɪɴɢ✗ᴩʏʀᴏɢʀᴀᴍ : {pyrover} \n<code>{STRING1}</code></b>",
        reply_markup=reply_markup
    )
 else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")




@app.on_message(filters.command(["اضف قناه الاشتراك للتشغيل"],"") & filters.private, group = 2)
async def add_must(c,msg):
 if str(msg.from_user.id) == OWNER_ID:

    try:
        m = await c.ask(msg.chat.id, "عزيزي المطور كم بارسال رابط القناه بدون علامه : @ \nو قم برفع البوت ادمن في القناه")
        try:
            chat = await c.get_chat(m.text)
        except:
            return await msg.reply(" تاكد عزيزي المطور من يوزر القناه او الجروب ")
        await set_must(c.me.username,chat.username)
        await msg.reply("تمت اضافه القناه بنجاح")
    except Exception as e:
        await msg.reply(f"- حدث خطا -> {e}")
 else:
        await msg.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")





@app.on_message(filters.command(["قناة الاشتراك"],"") & filters.private, group = 2)
async def get_ch_must(c,msg):
 if str(msg.from_user.id) == OWNER_ID:

    db = await get_must(c.me.username)
    if db:
        await msg.reply(f"قناة الاشتراك الاجباري ->> @{db}")
    else:
        return await msg.reply(" لم يتم تعيين قناة الاشتراك ")
 else:
        await msg.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
    




@app.on_message(filters.command(["حذف قناة الاشتراك"],"") & filters.private, group = 2)
async def rem_ch_must(c,msg):
 if str(msg.from_user.id) == OWNER_ID:
   if msg.text.strip() == "حذف قناة الاشتراك":
    done = await del_must(c.me.username)
    if done:
        return await msg.reply("تم حذف قناة الاشتراك بنجاح")
    else:
        return await msg.reply("لم يتم تعيين قناة الاشتراك")
 else:
        await msg.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")





@app.on_message(filters.command(["تفعيل الاشتراك للتشغيل"],"") & filters.private, group = 2)
async def en_ch_must(c,msg):
 if str(msg.from_user.id) == OWNER_ID:

    status = await get_must_ch(c.me.username)
    if status == "معطل" :
        await set_must_ch(c.me.username,"enable")
        return await msg.reply("تم تفعيل الاشتراك للتشغيل بنجاح")
    else:
        await msg.reply("الاشتراك الاجباري مفعل من قبل")
 else:
        await msg.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")






@app.on_message(filters.command(["تعطيل الاشتراك للتشغيل"],"") & filters.private, group = 2)
async def dis_ch_must(c,msg):
 if str(msg.from_user.id) == OWNER_ID:

    status = await get_must_ch(c.me.username)
    if status == "مفعل" :
        await set_must_ch(c.me.username,"disable")
        return await msg.reply("تم تعطيل الاشتراك للتشغيل بنجاح")
    else:
        await msg.reply("الاشتراك الاجباري معطل من قبل")
 else:
        await msg.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")