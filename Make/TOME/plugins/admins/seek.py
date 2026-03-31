from pyrogram import filters
from pyrogram.types import Message

from TOME import YouTube, app
from TOME.core.call import KIM
from TOME.misc import db
from TOME.utils import AdminRightsCheck, seconds_to_min
from TOME.utils.inline import close_markup
from config import BANNED_USERS
from strings import get_string










@app.on_message(filters.command(["/seek", "قدم", "seekback", "cseekback"], "") & filters.channel)
async def seek_commg(cli, message):
    _ = get_string("en")
    chat_id = message.chat.id
    if len(message.command) == 1:
        return await message.reply_text(_["admin_20"])
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text(_["admin_21"])
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_22"])
    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    if message.command[0][-2] == "c":
        if (duration_played - duration_to_skip) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played - duration_to_skip + 1
    else:
        if (duration_seconds - (duration_played + duration_to_skip)) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played + duration_to_skip + 1
    mystic = await message.reply_text(_["admin_24"])
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text(_["admin_22"])
    check = (playing[0]).get("speed_path")
    if check:
        file_path = check
    if "index_" in file_path:
        file_path = playing[0]["vidid"]
    try:
        await KIM.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except:
        return await mystic.edit_text(_["admin_26"], reply_markup=close_markup(_))
    if message.command[0][-2] == "c":
        db[chat_id][0]["played"] -= duration_to_skip
    else:
        db[chat_id][0]["played"] += duration_to_skip
    await mystic.edit_text(
        text=_["admin_25"].format(seconds_to_min(to_seek), message.chat.title),
        reply_markup=close_markup(_),
    )
    




@app.on_message(filters.command(["/seekback", "ارجع", "رجع", "رجوع"], "") & filters.channel)
async def seek_back_commm(cli, message):
    _ = get_string("en")
    chat_id = message.chat.id
    if len(message.command) == 1:
        return await message.reply_text("⚠️ يرجى تحديد عدد الثواني للرجوع للخلف.\nمثال: `/seekback 30` للرجوع 30 ثانية للخلف")
    
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text("❌ يجب أن يكون عدد الثواني رقماً صحيحاً!\nمثال: `10` للرجوع 10 ثواني للخلف")
    
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text("❌ لا يوجد أي شيء قيد التشغيل حاليًا!")
    
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text("⚠️ لا يمكن الرجوع للخلف في البث المباشر أو الملفات غير محددة المدة")
    
    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    
    # التحقق من عدم الرجوع قبل بداية الملف
    if (duration_played - duration_to_skip) <= 10:
        remaining_time = seconds_to_min(duration_played)
        total_duration = duration
        return await message.reply_text(
            text=f"⏮️ لا يمكن الرجوع للخلف أكثر من الوقت الحالي!\n\n⏳ الوقت الحالي: {remaining_time}\n🕒 المدة الكلية: {total_duration}",
            reply_markup=close_markup(_),
        )
    
    to_seek = duration_played - duration_to_skip + 1
    
    mystic = await message.reply_text("🔄 جاري الرجوع للخلف...")
    
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text("❌ فشل في معالجة الفيديو، يرجى المحاولة مرة أخرى")
    
    check = (playing[0]).get("speed_path")
    if check:
        file_path = check
    
    if "index_" in file_path:
        file_path = playing[0]["vidid"]
    
    try:
        await KIM.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except:
        return await mystic.edit_text("❌ حدث خطأ أثناء محاولة الرجوع للخلف!", reply_markup=close_markup(_))
    
    db[chat_id][0]["played"] -= duration_to_skip
    
    new_position = seconds_to_min(to_seek)
    await mystic.edit_text(
        text=f"» تم رجوع البث بنجاح.\n\nالمدة:  {new_position}\nبواسطة: {message.chat.title}",
        reply_markup=close_markup(_),
    )
    
    








@app.on_message(filters.command(["/seek", "قدم", "مرر", "cseekback"], "") & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def seek_comm(cli, message: Message, _, chat_id):
    if len(message.command) == 1:
        return await message.reply_text(_["admin_20"])
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text(_["admin_21"])
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_22"])
    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    if message.command[0][-2] == "c":
        if (duration_played - duration_to_skip) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played - duration_to_skip + 1
    else:
        if (duration_seconds - (duration_played + duration_to_skip)) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played + duration_to_skip + 1
    mystic = await message.reply_text(_["admin_24"])
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text(_["admin_22"])
    check = (playing[0]).get("speed_path")
    if check:
        file_path = check
    if "index_" in file_path:
        file_path = playing[0]["vidid"]
    try:
        await KIM.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except:
        return await mystic.edit_text(_["admin_26"], reply_markup=close_markup(_))
    if message.command[0][-2] == "c":
        db[chat_id][0]["played"] -= duration_to_skip
    else:
        db[chat_id][0]["played"] += duration_to_skip
    await mystic.edit_text(
        text=_["admin_25"].format(seconds_to_min(to_seek), message.from_user.mention),
        reply_markup=close_markup(_),
    )





@app.on_message(filters.command(["/seekback", "ارجع", "رجع", "رجوع"], "") & filters.group & ~BANNED_USERS, group=5)
@AdminRightsCheck
async def seek_back_comm(cli, message: Message, _, chat_id):
    if len(message.command) == 1:
        return await message.reply_text("⚠️ يرجى تحديد عدد الثواني للرجوع للخلف.\nمثال: `/seekback 30` للرجوع 30 ثانية للخلف")
    
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text("❌ يجب أن يكون عدد الثواني رقماً صحيحاً!\nمثال: `10` للرجوع 10 ثواني للخلف")
    
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text("❌ لا يوجد أي شيء قيد التشغيل حاليًا!")
    
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text("⚠️ لا يمكن الرجوع للخلف في البث المباشر أو الملفات غير محددة المدة")
    
    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    
    # التحقق من عدم الرجوع قبل بداية الملف
    if (duration_played - duration_to_skip) <= 10:
        remaining_time = seconds_to_min(duration_played)
        total_duration = duration
        return await message.reply_text(
            text=f"⏮️ لا يمكن الرجوع للخلف أكثر من الوقت الحالي!\n\n⏳ الوقت الحالي: {remaining_time}\n🕒 المدة الكلية: {total_duration}",
            reply_markup=close_markup(_),
        )
    
    to_seek = duration_played - duration_to_skip + 1
    
    mystic = await message.reply_text("🔄 جاري الرجوع للخلف...")
    
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text("❌ فشل في معالجة الفيديو، يرجى المحاولة مرة أخرى")
    
    check = (playing[0]).get("speed_path")
    if check:
        file_path = check
    
    if "index_" in file_path:
        file_path = playing[0]["vidid"]
    
    try:
        await KIM.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except:
        return await mystic.edit_text("❌ حدث خطأ أثناء محاولة الرجوع للخلف!", reply_markup=close_markup(_))
    
    db[chat_id][0]["played"] -= duration_to_skip
    
    new_position = seconds_to_min(to_seek)
    await mystic.edit_text(
        text=f"» تم رجوع البث بنجاح.\n\nالمدة:  {new_position}\nبواسطة: {message.from_user.mention}",
        reply_markup=close_markup(_),
    )