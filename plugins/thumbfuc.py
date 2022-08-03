from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
    thumb = find(int(message.chat.id))[0]
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("**💋 ʙᴀʙʏ Yᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴀɴʏ Tʜᴜᴍʙɴᴀɪʟ** ❌") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
    delthumb(int(message.chat.id))
    await message.reply_text("**💋 ʙᴀʙʏ ʏᴏᴜʀ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ** 🎉")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id , file_id)
    await message.reply_text("**💋 Bᴀʙʏ Yᴏᴜʀ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ** ✅")
	
