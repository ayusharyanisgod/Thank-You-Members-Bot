import os 
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, Sticker, Document, ChatMember

    
bughunter0 = Client(
    "Member-Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_STRING_PRIVATE = """ Hi {},
I'm Member Sticker Bot. 
I Can Send Relevant Thankyou Sticker in Groups and Channel
\n All Member count doesn't return a sticker, so I will send a Thank you message for the count which have no sticker,

😎 This message will be deleted after 10 second. \n
Nothing to Do here !! 😕
🥺 **ADD ME TO A GROUP THEN TRIGGER ME**
"""

START_STRING_GROUP = """ **I need Admin rights to Send sticker in {}**

`Join My Updates Channel for Getting more familiar with me`

"""

REPORT_STRING_PRIVATE = """ Hi {},
●I am Currently using [this](https://t.me/addstickers/DownloadStics_ThankYouMembers) sticker pack, if found another pack report it here @MasterAyushAryan_Bot with sticker.

we will try to remove it.
"""

REPORT_STRING_GROUP = """●I am Currently using [this](https://t.me/addstickers/DownloadStics_ThankYouMembers) sticker pack, if found another pack report it here @MasterAyushAryan_Bot with sticker.

we will try to remove it.

"""

ABOUT = """
● **BOT:** `Member Sticker BOT` 
● **SERVER :** `Heroku` 
● **LIBRARY :** `Pyrogram` 
● **LANGUAGE :** `Python 3.9` 

"""
HELP = """
● Still Wonder How I Work ? 
● Use /help get a Full Brief on How i Works.

●I am Currently using [this](https://t.me/addstickers/DownloadStics_ThankYouMembers) sticker pack, if found another pack report it here @MasterAyushAryan_Bot with sticker.

we will try to remove it.
"""


CHANNEL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Updates Channel ⬆️' ,url='https://t.me/PremiumValleyUpdates'),
        InlineKeyboardButton('Support Group 🆘' ,url='https://t.me/PremiumValleySupport')
        ]]
    )
ADDME_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↗ ADD ME TO A GROUP ↗', url="t.me/ThanksMembers_Bot?startgroup=true")
        ]]
    )
START_BUTTON = InlineKeyboardMarkup(
    
        [[
        InlineKeyboardButton('Updates Channel ⬆️' ,url='https://t.me/PremiumValleyUpdates'),
        InlineKeyboardButton('Support Group 🆘' ,url='https://t.me/PremiumValleySupport')
        ],
        [
        InlineKeyboardButton('ABOUT',callback_data='cbabout'),
        InlineKeyboardButton('HELP',callback_data='cbhelp')
        ],
        [InlineKeyboardButton('➕ ADD ME TO A GROUP ➕', url="t.me/ThanksMembers_Bot?startgroup=true")
        ]]
        
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back',callback_data='cbclose'),
        ]]
    )

@bughunter0.on_callback_query() # callbackQuery()
async def cb_data(bot, update):  
    if update.data == "cbhelp":
        await update.message.edit_text(
            text=HELP,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "cbabout":
        await update.message.edit_text(
            text=ABOUT,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.edit_text(
            text=START_STRING_PRIVATE.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTON
        )


@bughunter0.on_message(filters.command(["start"]) & filters.private)
async def start_private(bot, update):
    text = START_STRING_PRIVATE.format(update.from_user.mention)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_message((filters.command(["start"]) & filters.group) | filters.regex("/start@ThanksMembers_Bot"))
async def start_group(bot, update):
    text = START_STRING_GROUP.format(update.chat.title)
    reply_markup = CHANNEL_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_message(filters.command(["report"]) & filters.private)
async def start_private(bot, update):
    text = START_STRING_PRIVATE.format(update.from_user.mention)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )

@bughunter0.on_message((filters.command(["report"]) & filters.group) | filters.regex("/report@ThanksMembers_Bot"))
async def start_group(bot, update):
    text = START_STRING_GROUP.format(update.chat.title)
    reply_markup = CHANNEL_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )
    
@bughunter0.on_message(filters.command(["ping"]))
async def ping(bot, message):
    start_t = time.time()
    rm = await message.reply_text("Checking")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@bughunter0.on_message(filters.new_chat_members & filters.group)
async def sticker_group(bot, message):
   try:
      chat_id = int(message.chat.id)
      count = await bughunter0.get_chat_members_count(chat_id)
      if count == 25:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAcWDbNvSOrJU6oRg29s6IYp0zT04PAAJ1AgACb8FkFDCUuHcEvpgrIAQ")
      elif count == 50:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIED2DbUA8YaVbYncLCyKBD80VrysOgAAJ2AgACb8FkFMQhQH7icivgHgQ")
      elif count == 75:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEIWDbUJgYjt4nVaK2TN9ILxXE7AprAAJ3AgACb8FkFNnvojLmMWChHgQ")
      elif count == 100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBVGEGC_DaJrlvBL0oRbTZ2cXm11duAAJ4AgACb8FkFCHyjB1WKhwIHgQ")
      elif count == 150:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBY2EGDByOJhVJFvCgvp9JMUhw2-SnAAJ5AgACb8FkFC0-klBbFUOcHgQ")
      elif count == 200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBamEGDD9wm3gsHfta5rpv33fCedUiAAJ6AgACb8FkFDqPwakq2etKHgQ")
      elif count == 250:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBcWEGDIwd6lLLO0dz-R3O5ZAWQ3_FAAJ7AgACb8FkFCFLPuqC5veCHgQ")
      elif count == 300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBeGEGDLwUILkTdyks_B-s-xpxJeFTAAJ8AgACb8FkFCmoLzif0k1eHgQ")
      elif count == 350:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBf2EGDP1u83P57I_soaz07F-Rnh-tAAJ9AgACb8FkFOItmI8tdunbHgQ")
      elif count == 400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIBhmEGDSfYROpMpNBJxKOjS0jjEdpjAAJ-AgACb8FkFLEuZPK4e-XOHgQ")
      elif count == 450:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEqmDcEL-Sn-KPtQIQVOp7-INSAAEkyAACjwEAAlvWKhj-Xyo1z-wAASseBA")
      elif count == 500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAICOGEGHXIepa-fdwt_Sqi01dSsPgogAAKAAgACb8FkFDdNlq54yRL6HgQ")
      elif count == 550:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAICOWEGHbiCk-0U-QfPUE9Wuoo8pgtWAAKBAgACb8FkFI-m1UbQWrgkHgQ")
      elif count == 600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAICQGEGHdhpkjwjjsKbxJl6YEUmd9ImAAKCAgACb8FkFM9xskyitVWxHgQ")
      elif count == 650:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAICRWEGHfGkD4YssU08CsTGKbLjs4-TAAKDAgACb8FkFC_AIV8PCOW8HgQ")
      elif count == 700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAICSGEGHhQPi57AqrotveKfwI86umVkAAKEAgACb8FkFHeWcxlF2xjEHgQ")
      elif count == 750:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAsmDbOmrNDjq0yIr3eWCoIy91syzpAAKbAQACW9YqGOtGZWA98zCaIAQ")
      elif count == 800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIEzmDcEadN5kE_Su3tayEahBjUxWrNAAKdAQACW9YqGIBhBKzK4V0cHgQ")
      elif count == 850:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE0GDcEdwjArhgbjNw6zqg7Gf81qN4AAKfAQACW9YqGE_RowPqmchSHgQ")
      elif count == 900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE0mDcEj9_kL_DAAGI_mCTbuIca2CcLQACoQEAAlvWKhjEOfieo8C4ox4E")
      elif count == 950:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE1GDcEmRPod5gxQ7IgvAkG-nNK2tfAAKjAQACW9YqGB1ij6GWOAMMHgQ")
      elif count == 1000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALAvGDbOnFkRPePdhEWXBwTSV4eJfjTAAKlAQACW9YqGAluL79s0KEQIAQ")
      elif count == 1100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE5GDcEpc_TgE3d3jqO1j7O4ehyr23AAKmAQACW9YqGNmy9ZJmPsQUHgQ")
      elif count == 1200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA6WDbO1TxfZyF69PzmCw7nsrB2LDvAAKnAQACW9YqGEVp0JPc4nO6IAQ")
      elif count == 1300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE52DciNL-2hlKIz-225JCVozKD7SCAAKoAQACW9YqGLjrkXe6ArJJHgQ")
      elif count == 1400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA62DbO1YL1arJf9zVgdTGIVB7MUGhAAKpAQACW9YqGAWw3fw07KjYIAQ")
      elif count == 1500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE6GDciT3DrSed3KGLqX1rVcPwU_xuAAKqAQACW9YqGN0Vs6wobkM7HgQ")
      elif count == 1600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA7WDbO1jGcxdqGAVsFhsXKoMp1epDAAKrAQACW9YqGLsCrwgNIGYkIAQ")
      elif count == 1700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE6WDciVyqWjpKkMINJiKpYicFwXyOAAKsAQACW9YqGDw9w7xAMVc2HgQ")
      elif count == 1800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA72DbO1jWqU4PWKin9Bp9YEAZVnqQAAKtAQACW9YqGKEnAe3tZlvHIAQ")
      elif count == 1900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA8GDbO1lPUheD5q2KRr1E0ue07bVGAAKuAQACW9YqGOq5CMnZqqvdIAQ")
      elif count == 2000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALA8WDbO1lSjFdU0zOJsCxglr41pTVOAAKvAQACW9YqGPFJNraaGLBkIAQ")
      elif count == 2100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE6mDciXh6JuJ1QMSEXVksP0Fuw8oaAAKwAQACW9YqGFPovfk8HR_fHgQ")
      elif count == 2200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBQmDbPPPsIgABUtrgFfZsu7GdAAEUxQYAArEBAAJb1ioYog7dqaYf2M0gBA")
      elif count == 2300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBQ2DbPPRsp7QrM-wQBgHBb0SZzl13AAKyAQACW9YqGDH2xakhpikbIAQ")
      elif count == 2400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE62Dcimptq28z1ZRWDJg5oP513hdlAAKzAQACW9YqGEXNpSVgfaxQHgQ")
      elif count == 2500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE7GDcinzSnQ5zQ5cJ2qjrlvZZMQEbAAK0AQACW9YqGNfPUT-wLVZfHgQ")
      elif count == 2600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBRmDbPPXuU7h3tgaF1PEGHUtR4jp0AAK1AQACW9YqGIrf25Ws6cZgIAQ")
      elif count == 2700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE-2Dcir1OhXW6ogrw3uf_Nn6HO-GYAAK2AQACW9YqGEqRGCn0L8j0HgQ")
      elif count == 2800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE_GDcis2We8LY2R89ICjDj1NyMauzAAK3AQACW9YqGGPdw7iHyjmZHgQ")
      elif count == 2900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE_WDciu5e52XCAf_UzaZPvltnutPNAAK4AQACW9YqGPKt5abxW-lJHgQ")
      elif count == 3000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAALBOmDbPKJTEw96snijk3zWDju5o0cwAAK5AQACW9YqGNTV9iTuJqtXIAQ")
      elif count == 3100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIE_2DcixPJFDqIcErYXTxAy9PTdwwGAAK6AQACW9YqGO65_NqjiZU3HgQ")
      elif count == 3200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFAAFg3IskT3g2CtuSoI0hn4nqKxMB2QACuwEAAlvWKhho36LfXBFaIh4E")
      elif count == 3300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFOGDd3CKAe9hLi0gOfRZO_xQH2i2lAAK8AQACW9YqGDhjoXmI779cHgQ")
      elif count == 3400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFL2Dd3AU5jLwjOV8onJ75EegmqLAXAAK9AQACW9YqGDwxkTZBXKotHgQ")
      elif count == 3500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFO2Dd3E-1uwE25sHnjYU_UBtqfkztAAKPAgACb8FkFLFEIXI21CkuHgQ")
      elif count == 3600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFMWDd3GwevbENR2p8x78GokaYYteqAAK_AQACW9YqGPVRJh07Zpn5HgQ")
      elif count == 3700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFMmDd3H7wtAGYQi6TywG6UatvlkDSAALAAQACW9YqGHoZ0ubp8M5OHgQ")
      elif count == 3800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFM2Dd3JsusEfodZm9O-u5cRqrdcjQAALBAQACW9YqGPWMatfdz1KnHgQ")
      elif count == 3900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFNGDd3K9cSMHBZfPbkEEBLzv8rEq-AALCAQACW9YqGPC3vxs5FRdwHgQ")
      elif count == 4000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFNWDd3MvRlt1qclu1i0D2GXFeyXFwAALDAQACW9YqGOZMAlkiSrFOHgQ")
      elif count == 4100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFSWDd3uS5fAkTfAWTAUH2Gl4XG7NbAAKgAgACW9YqGAABHHE3YBc1dR4E")
      elif count == 4200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFSmDd3vh7mhp3yGHLKwG14ryNdxGGAAKhAgACW9YqGLxjAjd06-geHgQ")
      elif count == 4300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFS2Dd3wvdAq0RJH1-WvnOhDuh1-UlAAKiAgACW9YqGAs0uI0YFeglHgQ")
      elif count == 4400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFTGDd3x-8VSY7cqq63Gr5EC-RXuQzAAKjAgACW9YqGK8N7fDG_-R7HgQ")
      elif count == 4500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFTWDd3zJadmfYTNzyrmo_wf6szgWQAAKRAgACb8FkFCnulLRifUoPHgQ")
      elif count == 4600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFTmDd30Ws7gdD-0JgChN79EF7B3TOAAKlAgACW9YqGJGhk_wPK6TUHgQ")
      elif count == 4700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFT2Dd327zVRufqW_U218_V-anPww5AAKmAgACW9YqGAiNoWri8QjDHgQ")
      elif count == 4800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFUGDd34e8Iui7e1RKVNlRGA3d1VnHAAKnAgACW9YqGKIqhLomiwKjHgQ")
      elif count == 4900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFUWDd35xqS99ZxWM5puSPHNeIFLmUAAKoAgACW9YqGDO0wPQ5CT0eHgQ")
      elif count == 5000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFUmDd37NaW8s7XgLx2f25f6lg-9oCAAKmAgACb8FkFAABmvRInkQq1B4E")
      elif count == 5100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFU2Dd384atosoiX0IPg7GgALyqRhRAAKqAgACW9YqGEgUpy_SuQxeHgQ")
      elif count == 5200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFVGDd3-OmeiB3oj26tfe9BexkwYyKAAKrAgACW9YqGF-T9qG5zmhYHgQ")
      elif count == 5300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFVWDd3_dmZe7YxWJY-bRQnOs1eBUhAAKsAgACW9YqGAABeyF9Zt_WQB4E")
      elif count == 5400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFVmDd4A1rbNqSeaOMHGO9zEJoQHX_AAKtAgACW9YqGJW4byYrekp8HgQ")
      elif count == 5500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFV2Dd4C1X58dj_CS85Qcl1GDmIeiPAAKnAgACb8FkFHy9dkRdqy85HgQ")
      elif count == 5600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFWGDd4FBfJBNWByT7YdWKn8mbs2z3AAKvAgACW9YqGKlj4NZI7n8HHgQ")
      elif count == 5700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFWWDd4GA0aJCOjuCMO7Di9a0gy58hAAKwAgACW9YqGGiUAAEP_4abXB4E")
      elif count == 5800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFWmDd4Hgl5rw5jb7XxzchAsp97QavAAKxAgACW9YqGN7rbwt5WzvLHgQ")
      elif count == 5900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFW2Dd4KQ2d-yzM1xl9NLqEwzGuSzeAAKyAgACW9YqGHvPdYKQ9kUAAR4E")
      elif count == 6000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFXGDd4LaeggTjeRls3th9hhomi7NQAAKSAgACb8FkFO-7G5rKq-OGHgQ")
      elif count == 6100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFXWDd4NbSzB_FDXBBgL_r3HRDdzexAAK0AgACW9YqGBeKMqaKD2KLHgQ")
      elif count == 6200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFXmDd4OqE-cYU2JkdIV_UtyXsJZcYAAK1AgACW9YqGNlkkYwmNHDCHgQ")
      elif count == 6300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFX2Dd4P1zmE8dsJRQE5_hNRba1iadAAK2AgACW9YqGHSmP4mFnWj6HgQ")
      elif count == 6400:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFYGDd4ScV5lChuwrhrHYqXeqHZmMIAAK3AgACW9YqGCHwELlT4T4uHgQ")
      elif count == 6500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFYWDd4T2wlK1Ko7CqMkFezv-9SuPCAAKTAgACb8FkFIyO8XGfp2-LHgQ")
      elif count == 6600:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFYmDd4VVM-TcRPIrZ2E4hUZsOoeSuAAK5AgACW9YqGIs_QwiYQjVSHgQ")
      elif count == 6700:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFY2Dd4WiVmQeTVYvhFebLnbaJWEckAAK6AgACW9YqGGTX9sEcJ7vsHgQ")
      elif count == 6800:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFZGDd4XykR02p-dsWp2Q0FosXVZgtAAK7AgACW9YqGLxacVedeCH7HgQ")
      elif count == 6900:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFZWDd4ZNQMeW5T3AGJ7t_SeISKIRcAAK8AgACW9YqGN7w5F87AaH_HgQ")
      elif count == 7000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFZmDd4aVplUsNVhTHmgRMQ6W9_WJ6AAKUAgACb8FkFIxl1Y3Zh7DUHgQ")
      elif count == 7100:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFZ2Dd4bgjdYswN_jjcXFyEe5toFn4AAK-AgACW9YqGOjrbmCID2WcHgQ")
      elif count == 7200:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFaGDd4dpocwLfH_xywgT2myouDiCeAAK_AgACW9YqGM8zZPjcoWXcHgQ")      
      elif count == 7300:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFaWDd4e7cN_MKrTbuN1lqa-SsYBOXAALAAgACW9YqGEJEKq5tgeqxHgQ")
      elif count == 7500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFamDd4gutFBT-422Bq7m5-LmZghERAAKWAgACb8FkFDJuVxkIH49nHgQ")
      elif count == 8000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFa2Dd4thoRujUXkfDIibEdPEdHEqHAAIJAwACW9YqGK5V-iQ8HWU3HgQ")
      elif count == 8500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFbGDd4uyUrJWp69o8Y9S0TDcyvaTHAAIKAwACW9YqGO9Zs1209EcXHgQ")
      elif count == 9000:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFbWDd4x1G_DzeQGaE1gNWQ3ghvm9nAAILAwACW9YqGGTOL1FdSBRYHgQ")
      elif count == 9500:
                    await bot.send_sticker(chat_id,"CAACAgEAAxkBAAIFbmDd4zICYzggW6MLGHZl0c4h_PNRAAIMAwACW9YqGNzaIZjGU3xAHgQ")
      elif count == 10000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 11000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 12000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 13000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 14000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 15000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 16000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 17000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 18000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 19000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 20000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 25000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      elif count == 30000:
                    await bot.send_sticker(chat_id,"AgADQQYAAmMr4gk")
      
      else : 
            txt = await message.reply_text(f"**We are Happy to Have you as Our** `{count} th Member`")
           
           
            
   except Exception as error:
            await message.reply("@admins , \nAs per Your Group Permission Members of This Group Can't send Stickers to this Chat (`I'm a Member, Not an Admin`) .\n**To Solve this Issue add me as Admin Or Give permission to send stickers in the Chat** \n\n\n ©@BugHunterBots")


@bughunter0.on_message(filters.command(["start"]) & (filters.new_chat_members & filters.channel))
async def sticker_channel(bot, message):
 await message.reply("We are working this Feature, Will Available soon...")





@bughunter0.on_message(filters.command(["help"]))
async def help(bot, message):
 chat_id = str(message.chat.id)
 await bot.send_sticker(chat_id,"CAACAgIAAxkBAAEEDq1g6Y5LLm2DtFwCV2pPNCddwwZQHgAC6AkAAowucAABsFGHedLEzeUgBA")  
 

bughunter0.run()

