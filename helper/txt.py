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

class mr(object):
    PROGRESS_BAR = """\n
╭━━━━❰ ✧ᴘʀᴏɢʀᴇss ʙᴀʀ✧ ❱━➣
┣⪼Fɪʟᴇ sɪᴢᴇ 🗂️ : {1} | {2}
┣⪼Dᴜʀᴀᴛɪᴏɴ ⏳️ : {0}%
┣⪼Sᴘᴇᴇᴅ   🚀 : {3}/s
┣⪼Tɪᴍᴇ ʟᴇғᴛ ⏱️ : {4}
╰━━━━━━━━━━━━━━━✧✧✧✧➣ """

    ABOUT_TXT = """
╭───────────✧✧✧✧✧✧⍟
├🤖 ᴍʏ ɴᴀᴍᴇ :  <b>{}</b>
├🔮 ᴏᴛʜᴇʀ ʙᴏᴛS : <a href=https://t.me/robo_glitch>〘 **Cʟɪᴄᴋ ʜᴇʀᴇ** 〙</a> 
├👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/the_glitchs>〘 **Cʟɪᴄᴋ ʜᴇʀᴇ** 〙</a>
├🍂 Sᴜᴘᴘᴏʀᴛ : <a href=https://t.me/hddubhub4uhelp>〘 **Cʟɪᴄᴋ ʜᴇʀᴇ** 〙</a>
├📽 Mᴏᴠɪᴇɢʀᴏᴜᴘ : <a href=https://t.me/dubbedweb>〘 **Cʟɪᴄᴋ ʜᴇʀᴇ** 〙</a>
├📢 ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/hddubhub4u>〘 **Cʟɪᴄᴋ ʜᴇʀᴇ** 〙</a>
├📈 Bᴏᴛs Sᴛᴀᴛᴜs : <a href=https://t.me/futurebackups/754>〘 **Cʟɪᴄᴋ ʜᴇʀᴇ** 〙</a>
├📊 Pʏʀo ᴠᴇʀsɪᴏɴ : v3.6.8 [ ᗷᗴTᗩ ]              
╰──────────────✧✧✧✧⍟
                                """
    HELP_TXT = """
🌌 <b><u>✧HOW TO SET THUMBNILE✧</u></b>
  
•➤ /start ᴀ ʙᴏᴛ ᴀɴᴅ sᴇɴᴅ ᴀɴʏ ᴘɪᴄᴛᴜʀᴇ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ sᴇᴛ ᴛʜᴜᴍʙɴɪʟᴇ 🎞
•➤ /delthumb ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴏʟᴅ ᴛʜᴜᴍʙɴɪʟᴇ 🗑
•➤ /viewthumb ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴɪʟᴇ 👀

📑 <b><u>✧HOW TO SET CAPTION✧</u></b>
•> /set_caption - sᴇᴛ ᴀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ 💞
•> /see_caption - sᴇᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ 👀
•> /del_caption - ᴅᴇʟᴇᴛᴇ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ 🗑

Example:- /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}

✏️ <b><u>✧HOW TO RENAME A FILE✧</u></b>
•> Sᴇɴᴅ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ᴄʟɪᴄᴋ ʀᴇɴᴀᴍᴇ ᴏᴘᴛɪᴏɴ ᴀɴᴅ ᴛʏᴘᴇ ɴᴇᴡ ғɪʟᴇ ɴᴀᴍᴇ ᴀɴᴅ \n sᴇɴᴅ sᴇʟᴇᴄᴛ [document, video, audio] 
\n💌 ɴᴇᴇᴅ ᴀɴʏ ᴏᴛʜᴇʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ :- <a href=https://t.me/hddubhub4uhelp>🍂 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 👥</a>
"""

#⚠️ don't remove our credits 
    DEV_TXT = """
<b><u>🎭 ᴅᴇᴠʟᴏᴘᴇʀ sʜᴏʀᴛ ɴᴏᴛᴇ 🎭 </b></u> 

➤ 💌 **ᴄᴏɴᴛᴀᴄᴛ** :-\n<a href=https://t.me/GlitchAssistantBot>**『**ᴀssɪsᴛᴀɴᴛ**』****</a>|<a href=https://t.me/the_glitchs>『**ᴛʜᴇ_ɢʟɪᴛᴄʜs**』</a>
\n➤ Hᴇʏ ʙᴜᴅᴅʏ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ᴡɪᴛʜ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ & Sᴄʀɪᴘᴛ ʟɪᴋᴇ ᴛʜɪS ᴏʀ ᴀɴʏ ᴏᴛʜᴇʀ ʙᴏᴛ ᴏʀ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ ʀᴇɢᴀʀᴅɪɴɢ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ᴏғ ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛs ᴏʀ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴜs ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ᴄᴏɴᴛᴀᴄᴛ
 \nɪғ ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ ᴅᴇᴀᴅ ⚰ ᴛʜᴇɴ ᴍsɢ ᴏɴ ᴛʜᴇ ɢʟɪᴛᴄʜs ᴍᴇɴᴛɪᴏɴᴇᴅ ᴀʙᴏᴠᴇ 📍
  """
