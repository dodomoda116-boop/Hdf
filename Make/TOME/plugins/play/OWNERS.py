import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
import time
import requests
import datetime
import sys
import config

from config import *
import numpy as np


from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions, Message, CallbackQuery
from TOME.plugins.play.ADMANS import *


from pyrogram.enums import ChatMemberStatus, ChatType
import asyncio
from datetime import datetime, timedelta
from TOME import app
from config import OWNER_ID
import random
from random import choice
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatPermissions, Message, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ChatType
import asyncio
from datetime import datetime, timedelta
from TOME import app
from config import OWNER_ID
from config import*
import random
from random import choice
from collections import defaultdict
import re
import requests
import asyncio
import glob
import os
import time

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

import requests
from PIL import Image
import os








from pytz import timezone
from pyrogram import enums


from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice
from TOME.core.call import TOM
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
###
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums


from TOME import app




from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from TOME import app
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from TOME import app
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

# قاموس لتخزين الردود المخصصة
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

from TOME import  app

from pytz import timezone
from pyrogram import enums


from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice

from TOME.core.call import TOM
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




from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters, Client, enums
from pyrogram.types import *
from typing import Union, Optional
from TOME import app as Hiroko 





from PIL import Image





from pytz import timezone
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums




from pytz import timezone
from pyrogram import enums


from pytz import timezone
from pyrogram import filters
from pyrogram import Client
from typing import Union
from random import choice
from TOME.core.call import TOM
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
###
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums


from TOME import app



from pyrogram import filters

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from TOME import app
from random import  choice, randint

from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ParseMode

from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from TOME import app
from TOME import app
from TOME.utils.database import is_on_off
from pyrogram import Client, filters
from pyrogram.types import Message, Photo, Video, Sticker, Audio, Document
import asyncio
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from os import getenv
from dotenv import load_dotenv



load_dotenv()

OWNER_ID = getenv("OWNER_ID")

SUDOERS = [OWNER_ID]




def is_owner(_, __, message):
    if not message or not message.from_user:
        return False
    return message.from_user.id in [OWNER_ID, 7722416548]

async def is_admin(message):
    if not message or not message.from_user:
        return False
        
    user = message.from_user
    if user.id in [OWNER_ID, 7722416548]:
        return True
        
    try:
        member = await message.chat.get_member(user.id)
        return (member.status in [enums.ChatMemberStatus.OWNER] or
                is_owner(None, None, message) or
                is_mutaw(user.id) or
                is_malkeen(user.id) or
                is_admann(user.id))
    except:
        return False









def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            # "voice",
            # # "contact",
            # # "dice",
            # # "poll",
            # # "location",
            # # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj




#مطور البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#مطور البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps

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

async def get_dev_thumb(user_info: dict):
    cache_path = f"{CACHE_DIR}/{user_info.get('user_id', 'dev')}_promo.png"
    if os.path.isfile(cache_path):
        return cache_path
        
    if user_info.get('profile_path') and os.path.isfile(user_info['profile_path']):
        base = Image.open(user_info['profile_path']).resize((1280, 720)).convert("RGBA")
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
        
    title = "TOME DEVELOPER"
    draw.text((PANEL_X + (PANEL_W - draw.textlength(title, font=title_font)) // 2, PANEL_Y + 20), 
              title, fill="black", font=title_font)
              
    if user_info.get('profile_path') and os.path.isfile(user_info['profile_path']):
        try:
            profile_img = Image.open(user_info['profile_path']).convert("RGBA")
            profile_img = profile_img.resize((280, 280))
            
            mask = Image.new("L", profile_img.size, 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.ellipse((0, 0, 280, 280), fill=255)
            
            bg.paste(profile_img, (PANEL_X + (PANEL_W - 280) // 2, PANEL_Y + 100), mask)
        except Exception as e:
            print(f"Error adding profile image: {e}")

    dev_name = user_info.get('name', 'TOME DEV')
    dev_username = user_info.get('username', '@VegaDev')
    user_id = user_info.get('user_id', '123456789')
    

    draw.text((PANEL_X + (PANEL_W - draw.textlength(dev_name, font=name_font)) // 2, PANEL_Y + 400), 
              dev_name, fill="black", font=name_font)

    username_text = f"USER : @{dev_username}"
    draw.text((PANEL_X + (PANEL_W - draw.textlength(username_text, font=meta_font)) // 2, PANEL_Y + 450), 
              username_text, fill="black", font=meta_font)

    id_text = f"ID : {user_id}"
    draw.text((PANEL_X + (PANEL_W - draw.textlength(id_text, font=meta_font)) // 2, PANEL_Y + 490), 
              id_text, fill="black", font=meta_font)
              
    
    

    icons_path = "TOME/assets/thumb/dev_icons.png"
    if os.path.isfile(icons_path):
        try:
            icons = Image.open(icons_path).convert("RGBA")
            icons = icons.resize((400, 80))
            
            bg.paste(icons, (PANEL_X + (PANEL_W - 400) // 2, PANEL_Y + 580), icons)
        except Exception as e:
            print(f"Error adding dev icons: {e}")

    bg.save(cache_path)
    return cache_path

# @app.on_message(filters.command(["المطور", "مطور", "مطور البوت"], ""), group=50136)
# async def devbots(client: Client, message: Message):
    # bot_username = client.me.username
    # user = await client.get_chat(OWNER_ID)
    # name = user.first_name
    # username = user.username
    # bio = user.bio
    # user_id = user.id
    # photo = None

    # if user.photo:
        # photo = user.photo.big_file_id
        # photo = await client.download_media(photo)
        # link = f"https://t.me/{message.chat.username}"
        # title = message.chat.title if message.chat.title else message.chat.first_name

        # chat_title = f"<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n╭◉ɴᴧᴍᴇ : {message.from_user.mention} \n┃᚜◉ ᴄʜᴀᴛ ɴᴧᴍᴇ : {title}\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈" if message.from_user else f"╰◉ᴄʜᴀᴛ ɴᴧᴍᴇ: {message.chat.title}</b>"
        
        # try:
            # await client.send_message(username, f"<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈</b>\n<b><blockquote>عـزيزي المطور هناك شخص يريدك</b></blockquote>\n<b><blockquote>{chat_title}</b></blockquote>\n<b><blockquote>‣ᴄʜᴀᴛ ɪᴅ : {message.chat.id}</b></blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈",
            # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
        # except:
            # pass
    
    # if photo:
        # dev_info = {
            # 'name': name,
            # 'username': username,
            # 'user_id': user_id,
            # 'profile_path': photo
        # }
        
        # welcome_photo = await get_dev_thumb(dev_info)
        # await message.reply_photo(
            # photo=welcome_photo,
            # caption=f"<b><u>.معلومات مطوري</u>:\n• الاسم:  {name}\n• المعرف: @{username}\n• البايو : {bio}</b>",
            # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
        # )
    # else:
        # await message.reply_text(
            # f"<b><u>.معلومات مطوري</u>:\n• الاسم:  {name}\n• المعرف: @{username}\n• البايو : {bio}</b>",
            # reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{username}")]])
        # )
    
    # try:
        # if photo:
            # os.remove(photo)
            # os.remove(welcome_photo)
    # except:
        # pass
#مطور البوت ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓







SUDORS = [OWNER_ID]  # المطور الأساسي الافتراضي
CURRENT_OWNER_ID = OWNER_ID  # المطور الحالي (يمكن أن يتغير)

@app.on_message(filters.command(["المطور", "مطور", "مطور البوت"], ""), group=50136)
async def devbots(client: Client, message: Message):
    global SUDORS, CURRENT_OWNER_ID
    # نستخدم المطور الحالي إذا كان موجودًا، وإلا نستخدم المطور الأساسي
    dev_id = CURRENT_OWNER_ID if CURRENT_OWNER_ID else SUDORS[0]
    user = await client.get_chat(dev_id)
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = None
    if user.photo:
        photo = user.photo.big_file_id
        photo = await client.download_media(photo)
        link = f"https://t.me/{message.chat.username}"
        title = message.chat.title if message.chat.title else message.chat.first_name

        chat_title = f"<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n╭◉ɴᴧᴍᴇ : {message.from_user.mention} \n┃᚜◉ ᴄʜᴀᴛ ɴᴧᴍᴇ : {title}\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈" if message.from_user else f"╰◉ᴄʜᴀᴛ ɴᴧᴍᴇ: {message.chat.title}</b>"
        
        try:
            await client.send_message(username, f"<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈</b>\n<b><blockquote>عـزيزي المطور هناك شخص يريدك</b></blockquote>\n<b><blockquote>{chat_title}</b></blockquote>\n<b><blockquote>‣ᴄʜᴀᴛ ɪᴅ : {message.chat.id}</b></blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
        except:
            pass
    
    if photo:
        dev_info = {
            'name': name,
            'username': username,
            'user_id': user_id,
            'profile_path': photo
        }        
        welcome_photo = await get_dev_thumb(dev_info)
        await message.reply_photo(
            photo=welcome_photo,
            caption=f"<b><u>.معلومات مطوري</u>:\n\n• الاسم:  {name}\n• المعرف: @{username}\n• البايو : {bio}</b>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
        )
    else:
        await message.reply_text(
            f"<b><u>.معلومات مطوري</u>:\n\n• الاسم:  {name}\n• المعرف: @{username}\n• البايو : {bio}</b>",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{username}")]])
        )    
    try:
        if photo:
            os.remove(photo)
            os.remove(welcome_photo)
    except:
        pass

@app.on_message(filters.command("تغير المطور", "") & filters.private, group=50137)
async def change_dev(client: Client, message: Message):
    global SUDORS, CURRENT_OWNER_ID
    # فقط المطور الأساسي أو المطور الحالي يمكنه تغيير المطور
    if str(message.from_user.id) in SUDORS or (CURRENT_OWNER_ID and str(message.from_user.id) == str(CURRENT_OWNER_ID)):
        try:
            msg = await client.ask(
                chat_id=message.chat.id,
                text="•  أرسل المعرف أو الأيدي الخاص بالمطور الجديد:",
                timeout=60,
                reply_to_message_id=message.id,
                filters=filters.user(message.from_user.id)
            )
        
            if not msg.text:
                return await message.reply_text("• يجب إرسال معرف أو أيدي صالح")           
            new_dev = msg.text.strip()
            if new_dev.startswith("@"):
                user = await client.get_users(new_dev)
            else:
                user = await client.get_users(int(new_dev))
        
            CURRENT_OWNER_ID = user.id
        
            await message.reply_text(
                f"• تم تغيير المطور بنجاح\n"
                f"• المطور الجديد: {user.mention}\n"
                f"• الأيدي: {user.id}\n"
                f"• المعرف: @{user.username if user.username else 'لا يوجد'}"
            )
        except ValueError:
            await message.reply_text("• يجب أن يكون الأيدي أرقام فقط")
        except Exception as e:
            await message.reply_text(f"• لم أتمكن من تغيير المطور: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي أو المطور الحالي ❫ فقط")

@app.on_message(filters.command("حذف المطور", "") & filters.private, group=50138)
async def delete_dev(client: Client, message: Message):
    global SUDORS, CURRENT_OWNER_ID
    # فقط المطور الأساسي أو المطور الحالي يمكنه حذف المطور
    if str(message.from_user.id) in SUDORS or (CURRENT_OWNER_ID and str(message.from_user.id) == str(CURRENT_OWNER_ID)):
        if CURRENT_OWNER_ID is None:
            return await message.reply_text("• لا يوجد مطور إضافي ليتم حذفه\n• المطور الحالي هو المطور الأساسي الافتراضي")
        
        try:
            current_dev = await client.get_chat(CURRENT_OWNER_ID)
            default_dev = await client.get_chat(SUDORS[0])
            
            CURRENT_OWNER_ID = None  # الرجوع إلى المطور الأساسي
            
            await message.reply_text(
                f"• تم حذف المطور الإضافي بنجاح\n"
                f"• الاسم: {current_dev.first_name}\n"
                f"• الأيدي: {current_dev.id}\n\n"
                f"• تم الرجوع إلى المطور الأساسي:\n"
                f"• الاسم: {default_dev.first_name}\n"
                f"• الأيدي: {default_dev.id}"
            )
        except Exception as e:
            await message.reply_text(f"• لم أتمكن من حذف المطور: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي أو المطور الحالي ❫ فقط")










response_dict = {}
adding_process = {}



@app.on_message(filters.command("اضف ردي", "") & filters.group, group=50998)
async def add_response(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if (get.status in [ChatMemberStatus.OWNER] or 
        is_owner(None, None, message) or 
        is_moteerr(message.from_user.id) or 
        is_mutaw(message.from_user.id) or 
        is_malkeen(message.from_user.id) or 
        is_admann(message.from_user.id)):
        user_id = message.from_user.id
        chat_id = message.chat.id
    
        adding_process[user_id] = {
            "chat_id": chat_id,
            "step": "waiting_keyword"
        }
    
        await message.reply("• أرسل الكلمة للرد")
    else:
        await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس\n༄")
        
        
@app.on_message(filters.command("حذف ردي", "") & filters.group, group=58766)
async def delete_response(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if (get.status in [ChatMemberStatus.OWNER] or 
        is_owner(None, None, message) or 
        is_moteerr(message.from_user.id) or 
        is_mutaw(message.from_user.id) or 
        is_malkeen(message.from_user.id) or 
        is_admann(message.from_user.id)):
        if len(message.command) < 2:
            await message.reply("يجب استخدام الأمر هكذا: `حذف رد الكلمة`")
            return
    
        keyword = " ".join(message.command[1:]).lower()
    
        if keyword in response_dict:
            del response_dict[keyword]
            await message.reply(f"تم حذف الرد للكلمة: {keyword}")
        else:
            await message.reply(f"لا يوجد رد مضاف للكلمة: {keyword}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس\n༄")
        
        
@app.on_message(filters.group, group=5099)
async def handle_input(client: Client, message: Message):
    user_id = message.from_user.id   
    if user_id in adding_process:
        current_step = adding_process[user_id]["step"]
        
        # مرحلة إدخال الكلمة المفتاحية
        if current_step == "waiting_keyword":
            if not message.text:
                await message.reply(" يجب إرسال كلمة نصية كمفتاح")
                return                
            adding_process[user_id] = {
                "chat_id": message.chat.id,
                "step": "waiting_response",
                "keyword": message.text.lower()
            }
            await message.reply("• أرسل الآن الرد\n<b>• (يمكن أن يكون نص، صورة، فيديو، ملصق، صوت، أو ملف)</b>")
        elif current_step == "waiting_response":
            keyword = adding_process[user_id]["keyword"]
            if message.text:
                response = {"type": "text", "content": message.text}
            elif message.photo:
                response = {"type": "photo", "file_id": message.photo.file_id}
            elif message.video:
                response = {"type": "video", "file_id": message.video.file_id}
            elif message.sticker:
                response = {"type": "sticker", "file_id": message.sticker.file_id}
            elif message.audio:
                response = {"type": "audio", "file_id": message.audio.file_id}
            elif message.document:
                response = {"type": "document", "file_id": message.document.file_id}
            else:
                await message.reply("⚠️ نوع الرد غير مدعوم")
                return
            response_dict[keyword] = response
            await message.reply(f"•  تم حفظ الرد بنجاح للكلمة: <b>{keyword}</b>")
            del adding_process[user_id]
    else:
        keyword = message.text.lower() if message.text else ""
        if keyword in response_dict:
            response = response_dict[keyword]
            
            if response["type"] == "text":
                await message.reply(response["content"])
            elif response["type"] == "photo":
                await message.reply_photo(response["file_id"])
            elif response["type"] == "video":
                await message.reply_video(response["file_id"])
            elif response["type"] == "sticker":
                await message.reply_sticker(response["file_id"])
            elif response["type"] == "audio":
                await message.reply_audio(response["file_id"])
            elif response["type"] == "document":
                await message.reply_document(response["file_id"])





   

# custom_replies = {}

# @app.on_message(filters.command(["اضف رد"], "") & filters.group, group=544)
# async def add_custom_reply(client, message):
    # try:
        # get = await client.get_chat_member(message.chat.id, message.from_user.id)
        # if (get.status in [ChatMemberStatus.OWNER] or 
            # is_owner(None, None, message) or 
            # is_moteerr(message.from_user.id) or 
            # is_mutaw(message.from_user.id) or 
            # is_malkeen(message.from_user.id) or 
            # is_admann(message.from_user.id)):
            # name_msg = await client.ask(
                # chat_id=message.chat.id,
                # text="• أرسل اسم الرد الذي تريد اضافته:",
                # timeout=300,
                # reply_to_message_id=message.id,
                # filters=filters.user(message.from_user.id)
            # )
        
            # if not name_msg.text:
                # return await message.reply_text("• يجب إرسال اسم صالح للرد")            
            # reply_name = name_msg.text.strip().lower()
            # content_msg = await client.ask(
                # chat_id=message.chat.id,
                # text=f"• أرسل الآن المعرف أو النص المراد رده عند كتابة {reply_name}:\n(مثال: @username أو أي نص آخر)",
                # timeout=300,
                # reply_to_message_id=message.id,
                # filters=filters.user(message.from_user.id)
            # )
        
            # if not content_msg.text:
                # return await message.reply_text("• يجب إرسال محتوى صالح للرد")
            
            # reply_content = content_msg.text.strip()
            # custom_replies[reply_name] = reply_content
        
            # await message.reply_text(
                # f"• تم حفظ الرد بنجاح!\n"
                # f"• اسم الرد: {reply_name}\n"
                # f"• المحتوى: {reply_content}"
            # )        
        # except TimeoutError:
            # await message.reply_text("• انتهى الوقت المحدد لإدخال البيانات")
        # except Exception as e:
            # await message.reply_text(f"• حدث خطأ: {str(e)}")
    # else:
        # await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس")        
        
        
# @app.on_message(filters.command(["حذف رد"], ""), group=252)
# async def delete_custom_reply(client, message):
    # get = await client.get_chat_member(message.chat.id, message.from_user.id)
    # if (get.status in [ChatMemberStatus.OWNER] or 
        # is_owner(None, None, message) or 
        # is_moteerr(message.from_user.id) or 
        # is_mutaw(message.from_user.id) or 
        # is_malkeen(message.from_user.id) or 
        # is_admann(message.from_user.id)):
        # if len(message.command) < 2:
            # await message.reply("** الاستخدام الصحيح:**\nحذف رد [اسم الرد]")
            # return        
        # reply_name = message.command[1].lower()
        
        # if reply_name in custom_replies:
            # del custom_replies[reply_name]
            # await message.reply(f"• تم حذف الرد: {reply_name}")
        # else:
            # await message.reply(f"• لا يوجد رد بهذا الاسم: {reply_name}")
    # else:
        # await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس")
        
        
# @app.on_message(filters.command(["الردود"], "") & filters.group, group=26721)
# async def list_custom_replies(client, message):
    # get = await client.get_chat_member(message.chat.id, message.from_user.id)
    # if (get.status in [ChatMemberStatus.OWNER] or 
        # is_owner(None, None, message) or 
        # is_moteerr(message.from_user.id) or 
        # is_mutaw(message.from_user.id) or 
        # is_malkeen(message.from_user.id) or 
        # is_admann(message.from_user.id)):
        # if not custom_replies:
            # await message.reply("• لا توجد ردود مضافة حالياً.")
            # return
        # reply_list = "• الردود المضافة:\n\n"
        # for name, username in custom_replies.items():
            # reply_list += f"• {name} → @{username}\n"
        
        # await message.reply(reply_list)
    # else:
        # await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس")
        
        
        
# @app.on_message(filters.group, group=626)
# async def handle_custom_replies(client, message):
    # if not message.text or not message.from_user:
        # return
    # command = message.text.lower().split()[0].replace("/", "")
    # if command in custom_replies:
        # username = custom_replies[command]
        # try:
            # user = await client.get_chat(username)
            # name = user.first_name
            # username = user.username if user.username else "لا يوجد"
            # bio = user.bio if user.bio else "لا يوجد"
            
            # if user.photo:
                # photo = await app.download_media(user.photo.big_file_id)
                # await message.reply_photo(
                    # photo,
                    # caption=f"┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n<blockquote><b>╭◉ ɴᴧᴍᴇ : {name}\n┃᚜◉ ᴜsᴇꝛ : @{username}\n┃᚜◉ ɪᴅ : <code>{user.id}</code>\n╰◉ʙɪᴏ : {bio}</b></blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈", 
                    # reply_markup=InlineKeyboardMarkup([
                        # [InlineKeyboardButton(name, url=f"https://t.me/{username}")]
                    # ])
                # )
                # if os.path.exists(photo):
                    # os.remove(photo)
            # else:
                # await message.reply_text(
                    # f"┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n<blockquote><b>╭◉ ɴᴧᴍᴇ : {name}\n‣ᴜsᴇꝛ : @{username}\n┃᚜◉ ɪᴅ : <code>{user.id}</code>\n╰◉ ʙɪᴏ : {bio}</b></blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈", 
                    # reply_markup=InlineKeyboardMarkup([
                        # [InlineKeyboardButton(name, url=f"https://t.me/{username}")]
                    # ])
                # )
        # except Exception as e:
            # await message.reply(f"• حدث خطأ: {str(e)}")


custom_replies = {}

@app.on_message(filters.command(["اضف رد"], "") & filters.group, group=544)
async def add_custom_reply(client, message):
    try:
        get = await client.get_chat_member(message.chat.id, message.from_user.id)
        if (get.status in [ChatMemberStatus.OWNER] or 
            is_owner(None, None, message) or 
            is_moteerr(message.from_user.id) or 
            is_mutaw(message.from_user.id) or 
            is_malkeen(message.from_user.id) or 
            is_admann(message.from_user.id)):
            name_msg = await client.ask(
                chat_id=message.chat.id,
                text="• أرسل اسم الرد الذي تريد اضافته:",
                timeout=300,
                reply_to_message_id=message.id,
                filters=filters.user(message.from_user.id)
            )
        
            if not name_msg.text:
                return await message.reply_text("• يجب إرسال اسم صالح للرد")            
            reply_name = name_msg.text.strip().lower()
            content_msg = await client.ask(
                chat_id=message.chat.id,
                text=f"• أرسل الآن المعرف أو النص المراد رده عند كتابة {reply_name}:\n(مثال: @username أو أي نص آخر)",
                timeout=300,
                reply_to_message_id=message.id,
                filters=filters.user(message.from_user.id)
            )
            if not content_msg.text:
                return await message.reply_text("• يجب إرسال محتوى صالح للرد")
            group_id = message.chat.id
            if group_id not in custom_replies:
                custom_replies[group_id] = {}
            custom_replies[group_id][reply_name] = content_msg.text.strip()
        
            await message.reply_text(
                f"• تم حفظ الرد بنجاح!\n"
                f"• اسم الرد: {reply_name}\n"
                f"• المحتوى: {content_msg.text.strip()}"
            )
        else:
            await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس")
    except TimeoutError:
        await message.reply_text("• انتهى الوقت المحدد لإدخال البيانات")
    except Exception as e:
        await message.reply_text(f"• حدث خطأ: {str(e)}")
        
        
@app.on_message(filters.command(["حذف رد"], "") & filters.group, group=252)
async def delete_custom_reply(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if (get.status in [ChatMemberStatus.OWNER] or 
        is_owner(None, None, message) or 
        is_moteerr(message.from_user.id) or 
        is_mutaw(message.from_user.id) or 
        is_malkeen(message.from_user.id) or 
        is_admann(message.from_user.id)):
        if len(message.command) < 2:
            await message.reply("** الاستخدام الصحيح:**\nحذف رد [اسم الرد]")
            return        
        reply_name = message.command[1].lower()
        group_id = message.chat.id        
        if group_id in custom_replies and reply_name in custom_replies[group_id]:
            del custom_replies[group_id][reply_name]
            await message.reply(f"• تم حذف الرد: {reply_name}")
        else:
            await message.reply(f"• لا يوجد رد بهذا الاسم: {reply_name}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس")
        
        
@app.on_message(filters.command(["الردود"], "") & filters.group, group=26721)
async def list_custom_replies(client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if (get.status in [ChatMemberStatus.OWNER] or 
        is_owner(None, None, message) or 
        is_moteerr(message.from_user.id) or 
        is_mutaw(message.from_user.id) or 
        is_malkeen(message.from_user.id) or 
        is_admann(message.from_user.id)):
        group_id = message.chat.id
        if group_id not in custom_replies or not custom_replies[group_id]:
            await message.reply("• لا توجد ردود مضافة حالياً.")
            return
        reply_list = "• الردود المضافة:\n\n"
        for name, content in custom_replies[group_id].items():
            reply_list += f"• {name} → {content}\n"
        
        await message.reply(reply_list)
    else:
        await message.reply_text("هذا الأمر يخص ❪ الأدمن وفوق ❫ بس")
        
        
@app.on_message(filters.group, group=626)
async def handle_custom_replies(client, message):
    if not message.text or not message.from_user:
        return
    
    group_id = message.chat.id
    if group_id not in custom_replies:
        return
    
    command = message.text.lower().split()[0].replace("/", "")
    if command in custom_replies[group_id]:
        username = custom_replies[group_id][command]
        try:
            user = await client.get_chat(username)
            name = user.first_name
            username = user.username if user.username else "لا يوجد"
            bio = user.bio if user.bio else "لا يوجد"
            
            if user.photo:
                photo = await app.download_media(user.photo.big_file_id)
                await message.reply_photo(
                    photo,
                    caption=f"┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n<blockquote><b>╭◉ ɴᴧᴍᴇ : {name}\n┃᚜◉ ᴜsᴇꝛ : @{username}\n┃᚜◉ ɪᴅ : <code>{user.id}</code>\n╰◉ʙɪᴏ : {bio}</b></blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈", 
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(name, url=f"https://t.me/{username}")]
                    ])
                )
                if os.path.exists(photo):
                    os.remove(photo)
            else:
                await message.reply_text(
                    f"┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n<blockquote><b>╭◉ ɴᴧᴍᴇ : {name}\n‣ᴜsᴇꝛ : @{username}\n┃᚜◉ ɪᴅ : <code>{user.id}</code>\n╰◉ ʙɪᴏ : {bio}</b></blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈", 
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(name, url=f"https://t.me/{username}")]
                    ])
                )
        except Exception as e:
            await message.reply(f"• حدث خطأ: {str(e)}")



##توكسي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##توكسي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


import asyncio

@app.on_message(filters.command(["توكس","ꜰᴏx","فوكس"], ""), group=82036)
async def handle_uer_info(client, message):
    try:
        # الحصول على معلومات المستخدم
        user = await client.get_chat("devVega")
        name = user.first_name
        username = user.username if user.username else "لا يوجد"
        bio = user.bio if user.bio else "لا يوجد"
        
        caption = (
            f"<blockquote><b>"
            f"╭◉ɴᴧᴍᴇ : {name}\n"
            f"┃᚜◉ ᴜsᴇꝛ : @{username}\n"
            f"┃᚜◉ ɪᴅ : <code>{user.id}</code>\n"
            f"╰◉ʙɪᴏ : {bio}"
            f"</b></blockquote>"
        )
        
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton(name, url=f"https://t.me/{username}")]]
        )

        if user.photo:
            # حل مشكلة CHAT_PHOTO باستخدام download_media
            photo = await app.download_media(user.photo.big_file_id)
            
            await message.reply_photo(
                photo=photo,  # استخدام المسار المحلي بدلاً من file_id
                caption=caption,
                reply_markup=button,
                has_spoiler=True
            )
            
            # حذف الملف المؤقت
            
        else:
            await message.reply_text(
                caption,
                reply_markup=button
            )
            
    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text("❌ حدث خطأ في جلب المعلومات")











# وقت او الساعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
# وقت او الساعه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["الساعه","الوقت","تاريخ","وقت"], ""), group=88000666556413218)
async def khalid(client: Client, message: Message):
    egypt_tz = timezone('Egypt')
    current_time = datetime.datetime.now(egypt_tz).strftime("%H:%M:%S")    
    date = message.date.strftime("%Y-%m-%d")
    await message.reply_video(
        video=f"https://telegra.ph/file/6594430ed5f7209f39a36.mp4",
        caption=f"""<b><blockquote> ˚‧TOME˳+</b></blockquote>\n\n<b><blockquote>عـزيـزي :{message.from_user.mention}</b></blockquote>\n<blockquote> الـيك الان الوقت والتاريخ بتوقيت القاهره\n\n‣ᴅᴀᴛᴇ : {date}\n‣ᴛɪᴍᴇ : <code>{current_time}</code></b></blockquote>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "⸢ᴠᴇɢᴧ⸥", url=f"https://t.me/TOMEOne"),
                ],
            ]
        ),
    )
    
    
@app.on_message(filters.command(["توم","مطور توم","صاحب سورس توم","مبرمج السورس","مطور السورس","ᴋɪᴍᴍʏ","TOM","توم","مبرمج","المبرمج"], ""), group=11)
async def handle_uer_info(client, message):
    try:
        # الحصول على معلومات المستخدم
        user = await client.get_chat("TopTOME")
        name = user.first_name
        username = user.username if user.username else "لا يوجد"
        bio = user.bio if user.bio else "لا يوجد"
        
        caption = (
            f"<blockquote><b>"
            f"╭◉  ɴᴧᴍᴇ : {name}\n"
            f"┃᚜◉ ᴜsᴇꝛ : @{username}\n"
            f"┃᚜◉ ɪᴅ : <code>{user.id}</code>\n"
            f"╰◉  ʙɪᴏ : {bio}"
            f"</b></blockquote>"
        )
        
        button = InlineKeyboardMarkup(
            [[InlineKeyboardButton(name, url=f"https://t.me/{username}")]]
        )

        if user.photo:
            photo = await app.download_media(user.photo.big_file_id)
            
            await message.reply_photo(
                photo=photo,
                caption=caption,
                reply_markup=button,
                has_spoiler=True
            )
            
        else:
            await message.reply_text(
                caption,
                reply_markup=button
            )
            
    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text("❌ حدث خطأ في جلب المعلومات")
        
                






#سوهيلا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#سوهيلا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




@app.on_message(filters.command(["دعم", "رئيس", "تنفيذي", "هكر"], ""), group=8236)
async def handle_user_info(client, message):
    user = await client.get_chat("CeoVega")
    name = user.first_name
    if user.photo:
        photo = await app.download_media(user.photo.big_file_id)
        await message.reply_photo(
            photo,
            caption=f"╭◉ɴᴧᴍᴇ : {name}\n┃◉ᴜsᴇꝛ : @{user.username}\n┃◉ɪᴅ : <code>{user.id}</code>\n╰◉ʙɪᴏ : {user.bio}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name,
                            url=f"https://t.me/{user.username}"
                        )
                    ],
                ]
            ),
        )
    else:
        await message.reply_text(
            f"╭◉ɴᴧᴍᴇ : {name}\n┃᚜◉ᴜsᴇꝛ : @{user.username}\n┃᚜◉ɪᴅ : <code>{user.id}</code>\n╰◉ʙɪᴏ : {user.bio}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            name,
                            url=f"https://t.me/{message.from_user.username}"
                        )
                    ]
                ]
            )
        )


@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=65443)
async def welcome_devs(_, response: ChatMemberUpdated):
    dev_ids = [8122544723, 7722416548]
    if response.from_user.id in dev_ids and response.new_chat_member.status == ChatMemberStatus.MEMBER:
        info = await app.get_chat(response.from_user.id)
        name = info.first_name
        username = info.username
        bio = info.bio
        markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(name, url=f"https://t.me/{username}")],
                [
                    InlineKeyboardButton(
                        "ᴠᴇɢᴧ", url=SUPPORT_CHANNEL
                    ),
                ],
            ]
        )
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="downloads/developer.jpg", 
            caption=f"<blockquote><b> تم برمجتي بواسطة توم\n• مرحباً بـك : {name}\n المبرمج الاساسي لتوم</b></blockquote>"
        )