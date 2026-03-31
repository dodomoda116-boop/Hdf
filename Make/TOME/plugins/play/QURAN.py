from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup as InlineKeyboardMarkup, InlineKeyboardButton as InlineKeyboardButton
from TOME import app 
import json 
from config import BANNED_USERS
import requests 
from TOME.core.call import TOME
from TOME import app
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from TOME import app
import random
#ماكاتب موقيت صلاه تحت
from requests import Session
from requests import Response
from typing import Union
from TOME import app
from pyrogram import Client, filters
from pyrogram.types import Message

import json
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

## ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

import asyncio
import config
import re
import os
import requests
from os import getenv
from pyrogram import Client, filters
from TOME import app
from config import OWNER_ID
from pyrogram import filters, Client
from pyrogram import filters
from pyrogram import Client
from typing import Union
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from TOME.misc import SUDOERS

from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ChatMemberStatus, ParseMode
from TOME import app
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from telegraph import upload_file
from asyncio import gather
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio
import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from TOME.utils.database import (set_cmode,get_assistant)
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.errors import MessageNotModified


from pyrogram.types import CallbackQuery

from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TOME import app
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup                           
import asyncio
from TOME import (Apple, Resso, SoundCloud, Spotify, Telegram)
from TOME import app
import pyrogram
from TOME.misc import SUDOERS
from emoji import emojize
from config import *
from pyrogram import filters
from config import OWNER_ID
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from pyrogram.enums import ParseMode
from TOME import app
from TOME.utils.database import is_on_off


chat = []


@app.on_message(filters.group, group = 768)
async def azkarr(c, msg):
  if msg.text == "تفعيل الاذكار":
    if msg.chat.id in chat:
      return await msg.reply_text("<b>الاذكار مفعله من قبل\n༄</b>")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الاذكار بنجاح\n༄")
  elif msg.text == "تعطيل الاذكار":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الاذكار بنجاح\n༄")
    else:
      return await msg.reply_text("الاذكار معطله من قبل\n༄")
      


async def azkar():
   azkarl = [
   "لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
   "اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
   "ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
   "ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "سبحان الله وبحمده سبحان الله العظيم🌸",
   "أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
   "اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
   "استغفر الله العظيم وأتوبُ إليه 🌹",
   "لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
   "قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
   "يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
   "﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
   "‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
   "‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
   "ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
   "‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
   "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
   "اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
   "استغفر الله العظيم وأتوبُ إليه.",
   "‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
   " أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
   "ماتستغفر ربنا كده🥺❤️",
   "فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
   "ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
   "يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
   "قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
   "اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
   "- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
   "- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
   "أصبحنا وأصبح الملك لله ولا اله الا الله.",
   "‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
   "‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
   "يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
   "- اللهم القبول الذي لا يزول ❤️🍀.",
   "- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
   "سبحان الله وبحمده ،سبحان الله العظيم.",
   "لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
   " عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
   "- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
   "بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
   "- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
   "- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
   "‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
   "يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
   "‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
   "صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
   "اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
   "- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
   "اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
   "‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
   "- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
   "صلي على النبي بنيه الفرج❤️",
   "استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
   "اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
   "لا اله الا الله سيدنا محمد رسول الله🌿💜",
   "قول معايا - استغفر الله استفر الله استغفر الله -",
   "مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
   "أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
   "صلي على اشرف الخلق سيدنا محمد صلاةً الله عليه وسلم تسليما كثيرا ❤️",
   "ربي اجعلني مقيم الصلاة ومن ذريتي ربنا وتقبل دعاءنا . ربنا تقبل منا إنك أنت السميع العليم وتب علينا إنك أنت التواب الرحيم",
   "رب اغفر لي خطيئتي يوم الدين❤️",
   "اللهم اهدني فيمن هديت، وعافني فيمن عافيت، وتولني فيمن توليت، وبارك لي فيما أعطيت، وقني شرما قضيت، إنه لا يذل من واليت، تباركت ربنا وتعاليت",
   "اللهم إني أعوذ بك من عذاب النار، وأعوذ بك من عذاب القبر، وأعوذ بك من الفتن ما ظهر منها وما بطن، وأعوذ بك من فتنة الدجال",
   "اللهم إني أعوذ بك من علم لا ينفع وعمل لا يرفع وقلب لا يخشع وقول لا يسمع",
   "اللهم لا تخزني يوم القيامة",
   "اللهم إني أعوذ بك من صلاة لا تنفع",
   "اللهم إني أسألك الفردوس أعلى الجنة",
   "أَعـوذُ بِكَ مِنْ شَـرِّ ما صَنَـعْت، أَبـوءُ لَـكَ بِنِعْـمَتِـكَ عَلَـيَّ وَأَبـوءُ بِذَنْـبي فَاغْفـِرْ لي فَإِنَّـهُ لا يَغْـفِرُ الذُّنـوبَ إِلاّ أَنْتَ. مرة واحدة",
   "اللهم يا رحمن يا حنان يا منان استودعك يا رب قلبي فلا تجعل فيه أحدا سواك واستودعتك شهادة لا إله إلا الله فألهمني بها يا رب عند الممات واستودعك اللهم نفسي فلا تجعلني أخطو خطوة واحدة إلا في مرضاتك واستودعك روقي وعافيتي فاحفظها لي.",
   "اللهم يا كريم يا ودود يا رحيم يا عظيم انك قادر على كل شيء انك تقول للشيء كن فيكون ارحم اهلي رحمة دائمة واجعلهم من أهل الجنه في الفردوس لأعلي اللهم تقبلهم إليك واسعدهم بلقائك",
   "اللهم يا رحمن يارحيم ارحمني برحمتك الواسعه يارب ونقني من زنوبي مثل نقاء الثوب الأبيض من الدنس",
   "رَبَّنَا اغفِر لي وَلِوالِدَيَّ وَلِلمُؤمِنينَ يَومَ يَقومُ الحِسابُ",
   "رَّبِّ اغْفِرْ لِي وَلِوَالِدَيَّ وَلِمَن دَخَلَ بَيْتِيَ مُؤْمِنًا وَلِلْمُؤْمِنِينَ وَالْمُؤْمِنَاتِ وَلَا تَزِدِ الظَّالِمِينَ إِلَّا تَبَارًا",
   "اللهمَّ اغفر لوالدي وارحمهما كما ربّياني صغيراً، اللهمّ يا باسط اليدين بالعطايا ابسط على والدي من فضلك العظيم وجودك الواسع ما تشرح به صدرهما لعبادتك وطاعتك، والأنس بك والعمل بما يُرضيك، وبارك لهما في عُمرها، واغنهما من فضلك، وأعنهما في حلّهما وترحالهما وذهابهما وإيابهما، وأطل في عمرهما مع العافية في صحتهما ودِينهما، واجعل اللهمَّ آخر كلامهما من الدنيا لا إله إلّا الله محمدٌ رسول الله",
   "(اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ فِي الدُّنْيَا وَالآخِرَةِ، اللَّهُمَّ إِنِّي أَسْأَلُكَ الْعَفْوَ وَالْعَافِيَةَ: فِي دِينِي وَدُنْيَايَ وَأَهْلِي، وَمَالِي، اللَّهُمَّ اسْتُرْ عَوْرَاتِي، وَآمِنْ رَوْعَاتِي، اللَّهُمَّ احْفَظْنِي مِنْ بَينِ يَدَيَّ، وَمِنْ خَلْفِي، وَعَنْ يَمِينِي، وَعَنْ شِمَالِي، وَمِنْ فَوْقِي، وَأَعُوذُ بِعَظَمَتِكَ أَنْ أُغْتَالَ مِنْ تَحْتِي)).",
   "يا حيّ يا قيّوم برحمتك أستغيث أصلح لي شأني كله ولا تكلني إلى نفسي طرفة عينٍ أبداً ...",
   "‏﴿ وَاذْكُر ربّكَ إِذَا نَسِيتَ ﴾ ",
   "- اللهم صلِ وسلم على نبينآ محمد ❥⇣",
   "((اللَّهُمَّ صَلِّ وَسَلِّمْ عَلَى نَبَيِّنَا مُحَمَّدٍ)) (عشرَ مرَّاتٍ).",
   "اللهم يا عزيز يا جبار اجعل قلوبنا تخشع من تقواك واجعل عيوننا تدمع من خشياك واجعلنا يا رب من أهل التقوى وأهل المغفر",
   "استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب اليه - استغفر الله و اتوب الي",
   "اللهم إنك عفو تُحب العفو فاعفُ عن",
   "اللهم إني أسألك الثبات في الامر والعزيمة على الرشد واسالك قلبا سليما ولسانا صادقا واسالك شكر نعمتك و حسن عبادت",
   "اللهم إني أسألك العافية في الدنيا والآخرة، اللهم إني أسألك العفو والعافية في ديني ودنياي، وأهلي ومالي، اللهم استُر عوراتي، وآمِن رَوعاتي، اللهم احفظني من بين يدي ومن خلفي، وعن يميني وعن شمالي، ومن فوقي، وأعوذ بعظمتك أن أُغتال من تحتي",
   "((اللَّهُمَّ قِنِي عَذَابَكَ يَوْمَ تَبْعَثُ عِبَادَكَ)).",
   "((لاَ إِلَهَ إِلاَّ اللَّهُ، وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ)) (مائةَ مرَّةٍ).",
   "((اللَّهُمَّ عَالِمَ الغَيْبِ وَالشَّهَادَةِ فَاطِرَ السَّمَوَاتِ وَالْأَرْضِ، رَبَّ كُلِّ شَيْءٍ وَمَلِيكَهُ، أَشْهَدُ أَنْ لاَ إِلَهَ إِلاَّ أَنْتَ، أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَمِنْ شَرِّ الشَّيْطانِ وَشِرْكِهِ، وَأَنْ أَقْتَرِفَ عَلَى نَفْسِي سُوءاً، أَوْ أَجُرَّهُ إِلَى مُسْلِمٍ))",
   "اللهم اكفني بحلالك عن حرامك، وأغنني بفضلك عمن سواك",
   "(بِسْمِ اللَّهِ، تَوَكَّلْتُ عَلَى اللَّهِ، وَلَاَ حَوْلَ وَلَا قُوَّةَ إِلاَّ بِاللَّهِ)",
   "((أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ)) (مِائَةَ مَرَّةٍ فِي الْيَوْمِ).",
   "اللهم نشكوا إليك ضعفنا وقلة حيلتنا من امرنا فأغثنا وارحمنا واغفرلنا ولا تكل امرنا لمن لايخافك ولا يرحمنا ولا تؤخذنا بما فعل السفهاء منا",
   "مَنْ كَانَ آخِرُ كَلاَمِهِ لاَ إِلَهَ إِلاَّ اللَّهُ دَخَلَ الْجَنَّة"
   "لا إِلَهَ إِلا أَنتَ سُبْحَانَكَ إِنِّي كُنتُ مِنَ الظَّالِمِينَ🌸",
"اللَّهُمَّ أَعِنِّي عَلَى ذِكْرِكَ , وَشُكْرِكَ , وَحُسْنِ عِبَادَتِكَ🎈💞",
"استغفر الله العظيم وأتوبُ إليه 🌹",
"حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيم"
"ِ سبع مرات، كفاه الله تعالى ما أهمه من أمور الدنيا والآخرة🌹🌸",
"ربنا اغفر لنا ذنوبنا وإسرافنا فِي أمرنا وثبت أقدامنا وانصرنا على القوم الكافرين🌸",
"أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
"سبحان الله وبحمده سبحان الله العظيم🌸",
"أشهد أنْ لا إله إلا الله وحده لا شريك له، وأشهد أن محمدًا عبده ورسوله🌺",
"اللهم إنك عفو تُحب العفو فاعفُ عنّا 🌿🌹",
"استغفر الله العظيم وأتوبُ إليه 🌹",
"لا تقطع صلاتك، إن كنت قادراً على الصلاة في الوقت فصلِي و أكثر من الدعاء لتحقيق ما تتمنى💙",
"قال ﷺ : ”حَيْثُمَا كُنْتُمْ فَصَلُّوا عَلَيَّ، فَإِنَّ صَلَاتَكُمْ تَبْلُغُنِي“.",
"يا رب أفرحني بشيئاً انتظر حدوثه،اللهم إني متفائلاً بعطائك فاكتب لي ما أتمنى🌸",
"﴿ رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي ﴾",
"‏{ تَوَفَّنِي مُسْلِمًا وَأَلْحِقْنِي بِالصَّالِحِينَ }",
"‏اللهّم لطفك بقلوبنا وأحوالنا وأيامنا ،‏اللهّم تولنا بسعتك وعظيم فضلك ",
"ومن أحسن قولاً ممن دعا إلى الله وعمل صالحاً وقال أنني من المسلمين .💕",
"‏إن الله لا يبتليك بشيء إلا وبه خيرٌ لك فقل الحمدلله.",
"رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ",
"اللهم اشفي كل مريض يتألم ولا يعلم بحاله إلا أنت",
"استغفر الله العظيم وأتوبُ إليه.",
"‏لَم تعرف الدنيا عظيماً مِثله صلّوا عليه وسلموا تسليم",
" أنتَ اللّطيف وأنا عبدُك الضّعيف اغفرلي وارحمني وتجاوز عنّي.",
"ماتستغفر ربنا كده🥺❤️",
"فاضي شويه نصلي ع النبي ونحز خته فى الجنه❤️❤️",
"ماتوحدو ربنا يجماعه قولو لا اله الا الله❤️❤️",
"يلا كل واحد يقول سبحان الله وبحمده سبحان الله العظيم 3 مرات🙄❤️",
"قول لاحول ولا قوه الا بالله يمكن تفك كربتك🥺❤️",
"اللهم صلي عللى سيدنا محمد ماتصلي على النبي كده",
"- أسهل الطرق لإرضاء ربك، أرضي والديك 🥺💕",
"- اللهُم صبراً ، اللهم جبراً ، اللهم قوّة",
"أصبحنا وأصبح الملك لله ولا اله الا الله.",
"‏إنَّ اللهَ يُحِبُ المُلحِينَ فِي الدُّعَاء.",
"‏إن الله لا يخذل يداً رُفعت إليه أبداً.",
"يارب دُعاء القلب انت تسمعه فأستجب لهُ.",
"- اللهم القبول الذي لا يزول ❤️🍀.",
"- اللهُم خذ بقلبّي حيث نورك الذي لا ينطفِئ.",
"سبحان الله وبحمده ،سبحان الله العظيم.",
"لا تعودوا أنفسكم على الصمت، اذكرو الله، استغفروه، سبّحوه، احمدوه،"
" عودوا السنتكم على الذكر فإنها إن اعتادت لن تصمت أبدًا.",
"- اللهم بلغنا رمضان وأجعلنا نختم القرآن واهدنا لبر الامان يالله يا رحمان 🌙",
"بسم الله الذي لا يضر مع اسمه شيء في الأرض ولا في السماء وهو السميع العلي- ثلاث مرات -",
"- اللهم احرمني لذة معصيتك وارزقني لذة طاعتك 🌿💜.",
"- اللهُم إن في صوتي دُعاء وفي قلبِي أمنية اللهُم يسر لي الخير حيث كان.",
"‏اللهم أرني عجائب قدرتك في تيسير أموري 💜.",
"يغفر لمن يشاء إجعلني ممن تشاء يا الله.*",
"‏يارب إن قصّرنا في عبادتك فاغفرلنا، وإن سهينا عنك بمفاتن الدنيا فردنا إليك رداً جميلاً 💜🍀",
"صلوا على من قال في خطبة الوداع  ‏و إني مُباهٍ بكم الأمم يوم القيامة♥️⛅️",
"اللهـم إجعلنا ممن تشهد أصابعهم بذكـر الشهادة قبل الموت 🌿💜.",
"- وبك أصبحنا يا عظيم الشأن 🍃❤️.",
"اللهُم الجنة ونعيَّم الجنة مع من نحب💫❤️🌹",
"‏اللهم قلبًا سليمًا عفيفًا تقيًا نقيًا يخشاك سرًا وعلانية🤍🌱",
"- أسجِد لربِك وأحضِن الارض فِي ذِ  لاضَاق صَدرِك مِن هَموم المعَاصِي 🌿.",
"صلي على النبي بنيه الفرج❤️",
"استغفر ربنا كده 3 مرات هتاخد ثواب كبير اوى❤️",
"اشهد ان لا اله الا الله وان محمدا عبده ورسوله",
"لا اله الا الله سيدنا محمد رسول الله🌿💜",
"قول معايا - استغفر الله استفر الله استغفر الله -",
"مُجرد ثانية تنفعِك : أستغفُرالله العظيِم وأتوب إليّه.",
"أدعُ دُعاء الواثِق فالله لايُجرّبُ معه‌‏",
"صلي على محمد❤️",
"ماتيجو نقرء الفاتحه سوا🥺"
   ]
   while not await asyncio.sleep(1000):
     for i in chat:
       try:
         await app.send_message(i, random.choice(azkarl))
       except:
         pass
    
     
asyncio.create_task(azkar())

#وقت صلاه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#وقت صلاه ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

s = Session()
@app.on_message(filters.regex(r"^(مواقيت صلاة|مواقيت صلاه|وقت الصلاه)") & filters.group & filters.private, group=800906)
async def sendAdhan(_: Client, message: Message) -> None:
    address: str = message.text.rsplit(maxsplit=1)[-1]
    if address == "مواقيت الصلاة": return await message.reply(" اكتب اسم المنطقه بجانب الأمر،")
    adhan: Union[str, bool] = getAdhan(address)
    if not adhan: return await message.reply(" حدث خطأ أثناء جلب مواقيت الصلاة.", reply_to_message_id=message.id)
    await message.reply(adhan, reply_to_message_id=message.id)    


def getAdhan(address: str) -> Union[str, bool]:
    method: int = 1
    params = {
        "address" : address,
        "method" : method, 
        "school" : 0
    }
    res: Response = s.get("http://api.aladhan.com/timingsByAddress", params=params)
    data: dict = res.json()
    if data["code"] != 200: return print(data)
    data: dict = data["data"]
    timings: dict = data["timings"]
    date: dict = data["date"]["hijri"]
    weekday: str = date["weekday"]["ar"] + " - " + date["weekday"]["en"]
    month: str = date["month"]["ar"] + " - " + date["month"]["en"]
    date: str = date["date"]
    caption: str = f"<b>⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴧ♪</b>\n<u>اوقات الصلاه من فيجا</u>\n╮◉ الـفـجـر: {timings['Fajr']}\n‣ الـشـروق: {timings['Sunrise']}\n‣ الـظـهـر: {timings['Dhuhr']}\n‣ الـعـصـر: {timings['Asr']}\n‣ الـمـغـرب: {timings['Maghrib']}\n‣ الـعـشـاء: {timings['Isha']}\n╮◉  اللمساك : {timings['Imsak']}\n‣ الثلت الاول من الليل: {timings['Firstthird']}\n‣ منتصف الليل: {timings['Midnight']}\n‣ الثلث الاخير من الليل: {timings['Lastthird']}"
    caption += f"\n\n╮◉ التاريخ: {date} (هـ)\n‣ يـوم: {weekday}\n‣ الشهر: {month}"
    return caption


import random
import asyncio

chatt = []

@app.on_message(filters.text  & filters.group, group=77677668)
async def aarr(c, msg):
    if msg.text == "تفعيل نداء" or  msg.text == "تفعيل النداء" or  msg.text == "فتح النداء":
        if msg.chat.id in chatt:
            return await msg.reply_text("<b>نداء مفعله من قبل\n༄</b>")
        else:
            chatt.append(msg.chat.id)
            return await msg.reply_text("تم تفعيل نداء بنجاح\n༄")
    elif msg.text == "تعطيل نداء" or  msg.text == "تعطيل النداء" or  msg.text == "قفل الدناء":
        if msg.chat.id in chatt:
            chatt.remove(msg.chat.id)
            return await msg.reply_text("تم تعطيل نداء بنجاح\n༄")
        else:
            return await msg.reply_text("نداء معطله من قبل\n༄")

async def ndaaa():
    while True:
        await asyncio.sleep(1200)  
        for i in chatt:
            members = [] 
            try:
                async for member in app.get_chat_members(i):
                    if not member.user.is_bot:
                        members.append(member)
            except Exception as e:
                print(f"Error retr✨: {e}")
                continue
            if members:  
                random_member = random.choice(members)
                random_member_mention = f"<a href=\"tg://user?id={random_member.user.id}\">{random_member.user.first_name}</a>"
                
                random_message = [
                    f"⇜متجي : {random_member_mention}",
                    f"⇜• يـا قمـري ❤️‍🔥 : {random_member_mention}",
                    f" ⇜ولك فينك يعمري 😂 : {random_member_mention}",
                    f"⇜حبيبي وينك  :  {random_member_mention}",
                    f" ⇜انت منيح : {random_member_mention}",
                    f" ⇜ولله اشتقتلك اكتير : {random_member_mention}",
                    f" ⇜ حياااااااتي : {random_member_mention}",
                    f"⇜ اخي بدك تشارك معانا : {random_member_mention}",
                    f"⇜يعمررررري انا :  {random_member_mention}",
                    f"⇜حبــي الـڪ ادمان 💋😍 :  {random_member_mention}",
                    f" ⇜اوووه حبيبي هنا : {random_member_mention}",
                    f"⇜استغفر الله :  {random_member_mention}",
                    f"⇜ واحد الله : {random_member_mention}",
                    f" ⇜اذكر الله : {random_member_mention}",
                    f" ⇜يسمر يسمر : {random_member_mention}",
                    f" ⇜حبيبي وينك : {random_member_mention}",
                    f" ⇜حب الحب : {random_member_mention}",
                    f" ⇜تحبنــي ؟ 🙊🫶 : {random_member_mention}",
                    f" ⇜عادوغري انا مشتاق : {random_member_mention}",
                    f" ⇜مكنتش متخيل انك تسبيني : {random_member_mention}",
                    f" ⇜مكنتش متخيلي انا القمر هنا : {random_member_mention}",
                    f" ⇜مشتاقيـن حــب وينڪ 😥🍓 : {random_member_mention}",
                    f" اموت انا واعيد السنه : {random_member_mention}",
                    f" ⇜عامل ايه يجمييل  : {random_member_mention}",
                    f" ⇜قلب قلبي : {random_member_mention}",
                    f" ⇜فينك يروحي  : {random_member_mention}",
                    f" ⇜ولك يروحي : {random_member_mention}",
                    f" ⇜شوو هدا الجمال : {random_member_mention}",
                    f" ⇜خطفت قلبي : {random_member_mention}",
                    f" ⇜ههـلاوات ڪبد حياتـي 😊 : {random_member_mention}",
                    f" ⇜Hello : {random_member_mention}",
                    f" ⇜انت شخه 😛 : {random_member_mention}",
                    f"⇜ اخاف انا كدا يعني 🥱:  {random_member_mention}",
                    f" ⇜اضحك يبختك اعم🙂 : {random_member_mention}",
                    f" ⇜فينك يحب شارك معانا : {random_member_mention}",
                    f" ⇜اللي مصبرني هنا انت  : {random_member_mention}",
                    f"⇜ تع يمز نكلم شويه : {random_member_mention}",
                    f" ⇜يخرااشي عالقمر : {random_member_mention}",
                    f" ⇜منين يودي عالفين يجميل : {random_member_mention}",
                    f" ⇜براحه عالجروب مش بتاعنا : {random_member_mention}",
                    f" ⇜ماتجي ونجيب مليجي : {random_member_mention}",
                    f" ⇜يلا نروح ونجيب ممدوح : {random_member_mention}",
                    f" ⇜اوع الفحت لتقع تحت : {random_member_mention}",
                    f"⇜ ما تمسي علينا : {random_member_mention}"

                ]
                
                try:
                    await app.send_message(i, random.choice(random_message))
                except Exception as e:
                    print(f"Error sending message 🤦‍♂️: {e}")

asyncio.create_task(ndaaa())
