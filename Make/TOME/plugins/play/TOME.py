import asyncio
import requests
import os
import json
import re
import time
import random
import textwrap
import aiohttp
import aiofiles
import datetime
import numpy as np
from config import *
from pyrogram.types import *
from config import START_VIDS, HELP_VID_URL
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TOME import app
from typing import Union
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from typing import Union
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from typing import Union
from config import OWNER_ID
from os import getenv







OWNER_ID = getenv("OWNER_ID")


async def load_buttons():
    try:
        if os.path.exists("source_buttons.json") and os.path.getsize("source_buttons.json") > 0:
            with open("source_buttons.json", "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    except:
        return None

async def save_buttons(buttons):
    with open("source_buttons.json", "w", encoding="utf-8") as f:
        json.dump(buttons, f, ensure_ascii=False, indent=4)
        
        


DEFAULT_MAIN_MENU = {
    "caption": """<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n╭◉ᚐᴡᴇʟᴄᴏᴍᴇ ᴛᴏ
╰⬣<a href="{SUPPORT_CHANNEL}">ᚐᴠᴇɢᴀ ꜱᴏᴜʀᴄᴇ</a>
╭⊚<a href="{SUPPORT_CHAT}">ᚐɢʀᴏᴜᴘ</a>
╰◉<a href="{SUPPORT_CHANNEL}">ᚐᴄʜᴀɴɴᴇʟ</a></b>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈""",
    "buttons": [
        {"text": "ᴠᴇɢᴀ", "url": "{SUPPORT_CHANNEL}"},
        {"text": "🌀", "callback_data": "info"}
    ],
    "media": HELP_VID_URL,
    "info_text": """┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n<blockquote>
• أفضل سورس ميوزك عربي متكامل
• يدعم تشغيل فيديوهات اليوتيوب
• سرعة عالية وجودة صوت ممتازة
• واجهة مستخدم سهلة ومتطورة</blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈""",
    "info_buttons": [
        {"text": "ᴠᴇɢᴀ", "url": "{SUPPORT_CHANNEL}"},
        {"text": "Back", "callback_data": "back_main"}
    ]
}


@app.on_message(filters.command(["تغير كليشه السورس"], "") & filters.private, group=559)
async def change_source_text(client, message):
    if str(message.from_user.id) == OWNER_ID:
    
        ask = await app.ask(
            message.chat.id,
            "<b>أرسل الكليشة الجديدة للسورس</b>",
            timeout=300
        )
    
        if ask.text:
            try:
                with open("source_text.txt", "w", encoding="utf-8") as f:
                    f.write(ask.text)
                await message.reply("<b> تم تغيير كليشة السورس بنجاح</b>")
            except Exception as e:
                await message.reply(f"❌ فشل في حفظ الكليشة: {str(e)}")



@app.on_message(filters.command(["تغير قناه السورس"], "") & filters.private, group=560)
async def change_vega_button(client: Client, message: Message):
    if str(message.from_user.id) == OWNER_ID:
        ask_text = await client.ask(
            chat_id=message.chat.id,
            text="• أرسل النص الجديد لزر ᴠᴇɢᴀ (مثال: قناة السورس)",
            timeout=300
        )
        ask_url = await client.ask(
            chat_id=message.chat.id,
            text="<b>أرسل الرابط الجديد للزر (يجب أن يبدأ بـ https://)</b>",
            timeout=300
        )
    
        if not ask_url.text.startswith(('http://', 'https://')):
            return await message.reply("❌ الرابط يجب أن يبدأ بـ http:// أو https://")
    
        try:
            buttons = await load_buttons() or DEFAULT_MAIN_MENU["buttons"].copy()
            for btn in buttons:
                if btn.get("text", "").lower() == "ᴠᴇɢᴀ".lower():
                    btn["text"] = ask_text.text
                    btn["url"] = ask_url.text
                    break
        
        # حفظ التغييرات
            await save_buttons(buttons)
        
            await message.reply("<b> تم تحديث زر ᴠᴇɢᴀ بنجاح</b>")
        except Exception as e:
            await message.reply(f"❌ فشل في تحديث الزر: {str(e)}")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
@app.on_message(filters.command(["تغير لوجو السورس"], "") & filters.private, group=561)
async def change_source_media(client, message):
    if str(message.from_user.id) == OWNER_ID:    
        ask = await app.ask(
            message.chat.id,
        "<b>أرسل الصورة او الفيديو الجديد (للسورس)</b>",
            timeout=300
        )  
        if ask.photo or ask.video:
            try:
                media_path = await ask.download()
                with open("source_media.txt", "w", encoding="utf-8") as f:
                    f.write(media_path)
                await message.reply("<b> تم تغيير لوجو السورس بنجاح</b>")
            except Exception as e:
                await message.reply(f"❌ فشل في حفظ الوسائط: {str(e)}")
        else:
            await message.reply("• يجب أن تكون الوسائط صورة أو فيديو")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")
        
        
        
@app.on_message(filters.command(["حذف تخصيص السورس"], "") & filters.private, group=562)
async def reset_source_customization(client, message):
    if str(message.from_user.id) == OWNER_ID:        
        files = ["source_text.txt", "source_buttons.json", "source_media.txt"]
        deleted = []
    
        for file in files:
            try:
                if os.path.exists(file):
                    os.remove(file)
                    deleted.append(file.split(".")[0])
            except:
                pass
    
        if deleted:
            await message.reply(f" تم حذف المتغيرات بنجاح واعادة السورس الافتراضي")
        else:
            await message.reply(" لا يوجد تخصيصات لحذفها")
    else:
        await message.reply_text("هذا الأمر يخص ❪ المطور الاساسي ❫ بس")



async def get_source_customization():
    customization = DEFAULT_MAIN_MENU.copy()
    try:
        if os.path.exists("source_text.txt"):
            with open("source_text.txt", "r", encoding="utf-8") as f:
                customization["caption"] = f.read()
    except:
        pass    
    try:
        if os.path.exists("source_buttons.json"):
            with open("source_buttons.json", "r", encoding="utf-8") as f:
                customization["buttons"] = json.load(f)
    except:
        pass    
    try:
        if os.path.exists("source_media.txt"):
            with open("source_media.txt", "r", encoding="utf-8") as f:
                customization["media"] = f.read().strip()
    except:
        pass
    
    for key in ["caption", "info_text"]:
        customization[key] = customization[key].replace("{SUPPORT_CHANNEL}", SUPPORT_CHANNEL)
        customization[key] = customization[key].replace("{SUPPORT_CHAT}", SUPPORT_CHAT)
    
    for button in customization["buttons"] + customization["info_buttons"]:
        if "url" in button:
            button["url"] = button["url"].replace("{SUPPORT_CHANNEL}", SUPPORT_CHANNEL)
    return customization

async def send_main_menu(target: Union[Message, CallbackQuery]):
    customization = await get_source_customization()   
    if isinstance(target, CallbackQuery):
        message = target.message
        edit = True
    else:
        message = target
        edit = False    
    markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(btn["text"], url=btn.get("url"), callback_data=btn.get("callback_data"))] 
         for btn in customization["buttons"]]
    )    
    if edit:
        await message.edit_text(customization["caption"], reply_markup=markup)
    else:
        if customization["media"].endswith((".jpg", ".png", ".jpeg")):
            await message.reply_photo(
                photo=customization["media"],
                caption=customization["caption"],
                reply_markup=markup
            )
        else:
            await message.reply_video(
                video=customization["media"],
                caption=customization["caption"],
                reply_markup=markup
            )

@app.on_callback_query(filters.regex("^info$"), group=65555)
async def info_handler(client: Client, query: CallbackQuery):
    await query.answer()
    customization = await get_source_customization()
    
    markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton(btn["text"], url=btn.get("url"), callback_data=btn.get("callback_data"))] 
         for btn in customization["info_buttons"]]
    )    
    await query.edit_message_text(
        customization["info_text"],
        reply_markup=markup
    )
    
    
@app.on_message(filters.command(["سورس", "تومي", "السورس", "/vega", "ᴠᴇɢᴀ"], ""), group=12662)
async def source_handler(client: Client, message: Message):
    await send_main_menu(message)

@app.on_callback_query(filters.regex("^back_main$"), group=62)
async def back_handler(client: Client, query: CallbackQuery):
    await query.answer()
    await send_main_menu(query)


# async def send_main_menu(target: Union[Message, CallbackQuery]):
    # if isinstance(target, CallbackQuery):
        # message = target.message
        # edit = True
    # else:
        # message = target
        # edit = False
    
    # caption = f"""<b>┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n╭◉ᚐᴡᴇʟᴄᴏᴍᴇ ᴛᴏ
# ╰⬣<a href="{SUPPORT_CHANNEL}">ᚐᴠᴇɢᴀ ꜱᴏᴜʀᴄᴇ</a>
# ╭⊚<a href="{SUPPORT_CHAT}">ᚐɢʀᴏᴜᴘ</a>
# ╰◉<a href="{SUPPORT_CHANNEL}">ᚐᴄʜᴀɴɴᴇʟ</a></b>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈"""
    
    # markup = InlineKeyboardMarkup(
        # [
            # [InlineKeyboardButton("ᴠᴇɢᴀ", url=SUPPORT_CHANNEL)],
            # [InlineKeyboardButton("🌀", callback_data="info")]
        # ]
    # )
    
    # if edit:
        # await message.edit_text(caption, reply_markup=markup)
  
    # else:
        # await message.reply_video(
            # video=HELP_VID_URL,
            # caption=caption,
            # reply_markup=markup
        # )

# @app.on_message(filters.command(["سورس", "تومي", "السورس", "/vega", "ᴠᴇɢᴀ"], ""), group=12662)
# async def source_handler(client: Client, message: Message):
    # await send_main_menu(message)

# @app.on_callback_query(filters.regex("^info$"), group=65555)
# async def info_handler(client: Client, query: CallbackQuery):
    # await query.answer()
    # await query.edit_message_text(
        # """┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈\n<blockquote>
# ╮❶  أفضل سورس ميوزك عربي متكامل
# ┃᚜❷ يدعم تشغيل فيديوهات اليوتيوب
# ┃᚜❸ سرعة عالية وجودة صوت ممتازة
# ╯❹  واجهة مستخدم سهلة ومتطورة</blockquote>\n┈┅┅━━━⊷⊰🤍⊱⊶━━━┅┅┈""",
        # reply_markup=InlineKeyboardMarkup(
            # [
                # [InlineKeyboardButton("ᴠᴇɢᴀ", url=SUPPORT_CHANNEL)],
                # [InlineKeyboardButton("Back", callback_data="back_main")]
            # ]
        # )
    # )

# @app.on_callback_query(filters.regex("^back_main$"), group=62)
# async def back_handler(client: Client, query: CallbackQuery):
    # await query.answer()
    # await send_main_menu(query)
    
#مصنع تومي خاص لمطورين تومي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#مصنع تومي خاص لمطورين تومي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓




cclyof = []
@app.on_message(filters.command(["قفل مصنع", "تعطيل مصنع"], ""), group=27181882)
async def cclylock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if message.from_user.id == 6753126490:
      if message.chat.id in cclyof:
        return await message.reply_text("مصنع معطل من قبل")
      cclyof.append(message.chat.id)
      return await message.reply_text("تم تعطيل مصنع بنجاح")
   else:
      return await message.reply_text("هذا الامر يخص ❪ مطورين تومي ❫ بس")
   


@app.on_message(filters.command(["فتح مصنع", "تفعيل مصنع"], ""), group=288)
async def cclyopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if message.from_user.id == 8040979911:
      if not message.chat.id in cclyof:
        return await message.reply_text("مصنع مفعل من قبل\n")
      cclyof.remove(message.chat.id)
      return await message.reply_text("تم فتح مصع بنجاح")
   else:
      return await message.reply_text("هذا الامر يخص ❪ مطورين تومي ❫ بس")


@app.on_message(filters.command(["مصنع", "ᴍᴀᴋᴇʀ", "مصانع", "المصانع"], ""), group=32799805)
async def vegafactories(client, message):
    # Check if chat is blocked
    if message.chat.id in cclyof:
        return await message.reply_text("⛔ المصنع معطل مؤقتًا من قبل إدارة تومي")
    
    try:
        # Get bot info
        bot_user = await client.get_me()
        bot_name = bot_user.first_name
        
        # Send factory presentation
        await message.reply_video(
            video="https://telegra.ph/file/b4e36c287943f89d00a42.mp4",
            caption=f"""
🌟 **تم برمجة وتطوير {bot_name} بواسطه : تومي** 🌟
• هذه هيا المصانع الوحيده لدي تيم تومي
• صانع متكامله و مدمجه بتشغيل الاغاني و الحماية
• لدينا مانع تصفيه و تليثون فائق و سريع جداً ضد اي تهديد
• افضل سورس ميوزك و حماية في تليجرام الادراة المجموعات

⇜<i>تحذير لا نطلب المال او اخذ بيانات لتشغيل البوتات</i>

""",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🎧 الصانع الاول 🎧", 
                        url="https://t.me/MuiscOneBot"
                    ),
                    InlineKeyboardButton(
                        "🎧 صانع الثاني 🎧", 
                        url="https://t.me/TOME_1BOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 القناة الرسمية", 
                        url=SUPPORT_CHANNEL
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "إغلاق", 
                        callback_data="close"
                    )
                ]
            ])
        )
        
    except Exception as e:
        await message.reply_text(f"⚠️ حدث خطأ: {str(e)}")





##مميزات ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
##مميزات ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

from pyrogram import Client, filters

@app.on_message(filters.command(["مميزات", "المميزات", "تعليمات", "ارشادات"], ""), group=772)
async def commands_handler(client, message):
    if message.command[0] in ["مميزات", "المميزات"]:
        await message.reply_text(
            "<b>✨ قائمة مميزات سورس تومي:</b>\n\n"
            "<b>🔹 قسم الأدوات العامة:</b>\n"
            "1. ايدي - عرض معلومات المستخدم\n"
            "2. صورتي - عرض صورتك الشخصية\n"
            "3. اسمي - عرض اسمك\n"
            "4. لقبي - عرض لقبك في المجموعة\n"
            "5. رتبتي - عرض رتبتك في المجموعة\n"
            "6. بايو - عرض البايو الخاص بك\n"
            "7. جمالي - تقييم جمالك\n\n"
            
            "<b>🔹 قسم الترفيه:</b>\n"
            "8. تويت - إنشاء تويت عشوائي\n"
            "9. قولي - جعل البوت يقول شيئاً\n"
            "10. نكت - عرض نكتة عشوائية\n"
            "11. غنيلي - طلب أغنية عشوائية\n"
            "12. العاب - الألعاب المتاحة\n"
            "13. لو خيروك - لعبة لو خيروك\n"
            "14. احكام - لعبة الأحكام\n"
            "15. همسه - إرسال همسة\n\n"
            
            "<b>🔹 قسم الوسائط:</b>\n"
            "16. بحث - البحث عن ملفات\n"
            "17. يوتيوب - تنزيل من اليوتيوب\n"
            "18. تنزيل - تنزيل ملفات\n"
            "19. قرآن - تشغيل القرآن\n"
            "20. استوري - عرض استوري\n"
            "21. صور - البحث عن صور\n\n"
            
            "<b>🔹 قسم الإدارة:</b>\n"
            "22. كتم - كتم مستخدم\n"
            "23. حظر - حظر مستخدم\n"
            "24. تقيد - تقييد مستخدم\n"
            "25. انذار - إعطاء إنذار\n"
            "26. طرد البوتات - طرد البوتات\n"
            "27. كشف البوتات - عرض البوتات\n"
            "28. افتح الكول - فتح المكالمة\n"
            "29. اقفل الكول - إغلاق المكالمة\n\n"
            
            "<b>🔹 قسم المطور:</b>\n"
            "30. اذاعه - بث رسالة\n"
            "31. سورس - معلومات السورس\n"
            "32. معلومات التنصيب - معلومات الخادم\n"
            "33. رفع مطور - رفع مطور جديد\n"
            "34. الاحصائيات - إحصائيات البوت"
        )
    
    elif message.command[0] in ["تعليمات", "ارشادات"]:
        await message.reply_text(
            "<b>📚 دليل استخدام بوت تومي:</b>\n\n"
            "<b>🔸 التعليمات الأساسية:</b>\n"
            "1. اكتب /مميزات لرؤية جميع الأوامر\n"
            "2. معظم الأوامر تعمل بالرد على الرسائل\n"
            "3. للأوامر الطويلة استخدم علامات التنصيص\n\n"
            
            "<b>🔸 تعليمات الموسيقى:</b>\n"
            "- استخدم /شغل + اسم الأغنية لتشغيل الموسيقى\n"
            "- استخدم /تخطي لتخطي الأغنية الحالية\n"
            "- استخدم /ايقاف لإيقاف التشغيل\n\n"
            
            "<b>🔸 تعليمات الإدارة:</b>\n"
            "- لحظر عضو: /حظر بالرد على المستخدم\n"
            "- لإلغاء الحظر: /الغاء_حظر بالرد\n"
            "- لكتم عضو: /كتم بالرد على المستخدم\n\n"
            
            "<b>🔸 نصائح مهمة:</b>\n"
            "- لإنشاء رابط دعوة: /رابط\n"
            "- لرؤية صلاحياتك: /صلاحياتي\n\n"
            
            "<b>❓ للاستفسارات:</b>\n"
            "- تواصل مع المطور @TopTOME"
        )


        

#اصدار تومي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#اصدار تومي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#اصدار تومي ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["حول","ʀᴇʟᴇᴀꜱᴇ","اصدار"], ""), group=8236)
async def handle_user_info(client, message):
    if len(message.command) == 1:  # التأكد من عدم وجود نصوص إضافية مع الأمر
        user = await client.get_chat("vipvega")
        name = user.first_name
        if user.photo:
            photo = await app.download_media(user.photo.big_file_id)
            await message.reply_photo(photo, caption=f"""<b><blockquote>
╭⦿  ꜱᴏᴜʀᴄᴇ.ɴᴧᴍᴇ: ᴠᴇɢᴧ
│᚜⦿ ꜱʏꜱᴛᴇᴍ: ᴘʏᴛʜᴏɴ
│᚜⦿ ʟᴧɴɢᴜᴧɢᴇ: ɪꜱ ᴧʀᴧʙɪᴄ
│᚜⦿ ʀᴇʟᴇᴧꜱᴇ: 2.1 ᴠ
│᚜⦿ ᴅᴧᴛᴇ ᴄʀᴇᴧᴛᴇᴅ: 1 -8 -2016
╰⦿  ᴏᴡɴᴇʀ ᴏꜰ ᴠᴇɢᴧ:[ @TopTOME ]
</b></blockquote>""", 
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴠᴇɢᴧ", url=SUPPORT_CHANNEL)    
                        ],
                    ]
                ),
            )
        else:
            await message.reply_text(f"""<b><blockquote>
╭⦿  ꜱᴏᴜʀᴄᴇ.ɴᴧᴍᴇ: ᴠᴇɢᴧ
│᚜⦿ ꜱʏꜱᴛᴇᴍ: ᴘʏᴛʜᴏɴ
│᚜⦿ ʟᴧɴɢᴜᴧɢᴇ: ɪꜱ ᴧʀᴧʙɪᴄ
│᚜⦿ ʀᴇʟᴇᴧꜱᴇ: 2.1 ᴠ
│᚜⦿ ᴅᴧᴛᴇ ᴄʀᴇᴧᴛᴇᴅ: 1 -8 -2016
╰⦿  ᴏᴡɴᴇʀ ᴏꜰ ᴠᴇɢᴧ:[ @TopTOME ]
</b></blockquote>""",    
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴠᴇɢᴧ", url=SUPPORT_CHANNEL
                            )
                        ]
                    ]
                )
            )
    else:
        return  # تجاهل الرسالة إذا كان هناك نصوص إضافية