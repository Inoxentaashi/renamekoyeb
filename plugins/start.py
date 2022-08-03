"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from os import environ
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

FLOOD = int(environ.get("FLOOD", "30"))
START_PIC = environ.get("START_PIC", "https://telegra.ph/file/04d08445dce68c9a57b25.jpg")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢〘 Jᴏɪɴ Uᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 〙📢", url=client.invitelink) ]]
    text = "**⚠️ Sᴏʀʀʏ ʙᴀʙʏ Yᴏᴜ ᴅɪᴅɴ'ᴛ Jᴏɪɴᴇᴅ Oᴜʀ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Jᴏɪɴ ɴᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ᴀɢᴀɪɴ 😟**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""🌹 Hᴇʏ ʙᴀʙʏ {message.from_user.mention} \n**I'ᴍ ᴀ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ Bᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ 💞**\n**Pᴏᴡᴇʀᴇᴅ ʙʏ** ❗ **@robo_glitch**""",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("😈 Dᴇᴠᴇʟᴏᴘᴇʀ 😈", callback_data='dev')
           ],[
           InlineKeyboardButton('🔮 ᴏᴛʜᴇʀ ʙᴏᴛs 🔮', url='https://t.me/robo_glitch'),
           InlineKeyboardButton('🍂 Sᴜᴘᴘᴏʀᴛ 🦋', url='https://t.me/hddubhub4uhelp')
           ],[
           InlineKeyboardButton('🏆 Aʙᴏᴜᴛ', callback_data='about'),
           InlineKeyboardButton('📮 Hᴇʟᴘ', callback_data='help')
           ]]
          )
       )
    return


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__💋 ʙᴀʙʏ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜɪs ғɪʟᴇ ❓__**\n\n**Fɪʟᴇ Nᴀᴍᴇ ⪼** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 Yᴇᴀʜ Rᴇɴᴀᴍᴇ 📁", callback_data="rename") ],
                   [ InlineKeyboardButton("🔐 Cʟᴏsᴇ 🔐 ", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.x)
        text = f"""**__💋 ʙᴀʙʏ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜɪs ғɪʟᴇ ❓__**\n\n**Fɪʟᴇ Nᴀᴍᴇ ⪼** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 Yᴇᴀʜ Rᴇɴᴀᴍᴇ 📁", callback_data="rename") ],
                   [ InlineKeyboardButton("🔐 Cʟᴏsᴇ 🔐", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""🌹 Hᴇʏ ʙᴀʙʏ {query.from_user.mention} \n**I'ᴍ ᴀ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ Bᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ Sᴜᴘᴘᴏʀᴛ 💞**\n**Pᴏᴡᴇʀᴇᴅ ʙʏ** ❗ **@robo_glitch**""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("😈 Dᴇᴠᴇʟᴏᴘᴇʀ 😈", callback_data='dev')                
                ],[
                InlineKeyboardButton('🔮 ᴏᴛʜᴇʀ ʙᴏᴛs 🔮', url='https://t.me/robo_glitch'),
                InlineKeyboardButton('🍂 Sᴜᴘᴘᴏʀᴛ 🦋', url='https://t.me/hddubhub4uhelp')
                ],[
                InlineKeyboardButton('🏆 Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('📮 Hᴇʟᴘ', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("📽 ᴀʟʟ ᴍᴏᴠɪᴇ's ʙᴏᴛ 🎞", url="https://t.me/OlMoviesBot")
               ],[
               InlineKeyboardButton("📈 Bᴏᴛs ʟɪᴠᴇ sᴛᴀᴛᴜs 📍", url='https://t.me/futurebackups/754')
               ],[
               InlineKeyboardButton("🔐 Cʟᴏsᴇ 🔐", callback_data = "close"),
               InlineKeyboardButton("◁ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("🔱 ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ 🔱", url="https://t.me/GlitchAutoCaptionBot")
               ],[
               InlineKeyboardButton("💀 ᴇᴠɪʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇʀ ʙᴏᴛ 💀", url="https://t.me/EvilGroupManagerBot")
               ],[
               InlineKeyboardButton("🔐 Cʟᴏsᴇ 🔐", callback_data = "close"),
               InlineKeyboardButton("◁ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("📽 Mᴏᴠɪᴇs ɢʀᴏᴜᴘ 👥", url="https://t.me/dubbedweb")
               ],[
               InlineKeyboardButton("📁 ꜰɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ 📁", url="https://t.me/CopyrightFreeBot")
               ],[
               InlineKeyboardButton("🔐 Cʟᴏsᴇ 🔐", callback_data = "close"),
               InlineKeyboardButton("◁ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





