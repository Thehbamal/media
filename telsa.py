

import pyrogram
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from human import humanbytes
from human import TimeFormatter
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup)
from datetime import datetime
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
from io import BytesIO
from utlis import extract_user
import tgcrypto
HB= Client("Echo-bot", 
            api_id = 
            5257936,
            api_hash = "45e59f574d6c0574a6cb26f82689c349",
            bot_token = "1869097232:AAHJPKELP7brFuXqq0vpmDCrZ8pA_wPTgeM"
)


START_TEXT = """**HI {},
I AM A SIMPLE MEDIA INFO BOT 
MADE BY @TELSABOTS**
"""
HELP_TEXT = """**
SENT ANY MEDIAS.......

👇🏻CURRENTLY ONLY SUPPORTS👇🏻

(AUDIO,VIDEO,FILE,VOICE MSG,GIF,STICKER,PHOTO)

AND THEN SEE THE MAGIC 🥳

ADDING MORE FEATURES 😜

MADE BY @TELSABOTS**
"""
ABOUT_TEXT = """
 🤖<b>BOT :MEDIA INFO 🤖</b>

📢<b>CHANNEL :</b> ❤️ <a href='https://t.me/telsabots'>TELSA BOTS❤️</a>

🧑🏼‍💻DEV🧑🏼‍💻: @ALLUADDICT

"""

SOURCE_TEXT = """</b>PRESS SOURCE BUTTON FOR SOURCE
AND WATCH TOTOURIAL VIDEO IF YOU WANT ANY HELP</b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ot_buttons = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🤗ABOUT🤗', callback_data='about'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('📢CHANNEL📢', url='https://telegram.me/TELSABOTS'),
        InlineKeyboardButton('🧑🏼‍💻DEV🧑🏼‍💻', url='https://telegram.me/alluaddict')
        ],[
        InlineKeyboardButton('🏡HOME🏡', callback_data='home'),
        InlineKeyboardButton('🆘HELP🆘', callback_data='help'),
        InlineKeyboardButton('🔐CLOSE🔐', callback_data='close')
        ]]
    )

SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤩SOURCE🤩', url='https://hbamal.blogspot.com/2021/08/how-to-make-your-own-discussion-unpin_4.html'),
        InlineKeyboardButton('💟TOTOURIAL💟', url='https://www.youtube.com/watch?v=sXTg5CB9dy8')
        ],[
        InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]]
    )

@HB.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()

@HB.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["help"]))
async def help_message(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["about"]))
async def about_message(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@HB.on_message(filters.command(["Source", "s"]))
async def Source_message(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

    
@HB.on_message((filters.group | filters.private) & filters.command(["json"]))
async def group(bot, update):
    await reply_file(bot, update.reply_to_message)


async def reply_file(bot, update):
    with BytesIO(str.encode(str(update))) as file:
        file.name = "JSON.txt"
        await update.reply_document(
            document=file,
            quote=True,
            reply_markup=ot_buttons
        )
        try:
            os.remove(file)
        except:
            pass



@HB.on_inline_query()
async def answer(client, inline_query):
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="MOVIES CHANNEL",
                input_message_content=InputTextMessageContent(
                    "**NEW MOVIES CHANNEL**"
                ),
                
                description="OUR CHANNEL TO DOWNLOAD NEW MOVIES",
                thumb_url="https://telegra.ph/file/e8a39b06fabbfac6bce8f.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "📢CHANNEL📢",
                            url="https://t.me/+UZzc1ZqHvYXaLeNf"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="GROUP",
                input_message_content=InputTextMessageContent(
                    "**<i>MOVIE REQUESTING GROUP</i>**"
                ),
                
                description="A GROUP TO REQUEST ALL MOVIES ",
                thumb_url="https://telegra.ph/file/e8a39b06fabbfac6bce8f.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "GROUP",
                            url="https://t.me/+UZzc1ZqHvYXaLeNf"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
    )


@HB.on_message(filters.photo & filters.private)
async def stickers(bot, update):    
    if update.photo:
        await update.reply(f"**🏋️‍♂️ SIZE : {humanbytes(update.photo.file_size)}**\n\n **🆔  ID** `{update.photo.file_id}`\n\n **🆔 UNIQUE ID** : `{update.photo.file_unique_id}` \n\n**📅 DATE : {update.photo.date}**\n\n**📐 WIDTH** : {update.photo.width}\n\n**📏 HEIGHT** :{update.photo.height} \n\n**🔗JOIN @TELSABOTS**", quote=True)
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)

@HB.on_message(filters.animation & filters.private)
async def stickers(bot, update):    
    if update.animation:
        await update.reply(f"**🌀 ANIMATION NAME: {update.animation.file_name}**\n\n **🏋️‍♂️ SIZE : {humanbytes(update.animation.file_size)}**\n\n **⏰ DURATION : {TimeFormatter(update.animation.duration* 1000)}**\n\n**🔖 MIME TYPE : {update.animation.mime_type}**\n\n**🆔  ID** `{update.animation.file_id}`\n\n **🆔 UNIQUE ID** : `{update.animation.file_unique_id}` \n\n**📅 DATE : {update.animation.date}**\n\n**📐 WIDTH** : {update.animation.width}\n\n**📏 HEIGHT** :{update.animation.height} \n\n**🔗JOIN @TELSABOTS**", quote=True)
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)
    

@HB.on_message(filters.video & filters.private)
async def stickers(bot, update):    
    if update.video:
        await update.reply(f"**📰 VIDEO NAME : {update.video.file_name}**\n\n**🏋️‍♂️ SIZE : {humanbytes(update.video.file_size)}**\n\n **⏰ DURATION : {TimeFormatter(update.video.duration* 1000)}** \n\n**🔖 MIME TYPE : {update.video.mime_type}**\n\n **🆔 VIDEO ID** `{update.video.file_id}`\n\n **🆔 UNIQUE ID** : `{update.video.file_unique_id}` \n\n **🎨 STREAMING** : {update.video.supports_streaming}**\n\n**📅 DATE : {update.video.date}**\n\n**📐 WIDTH** : {update.video.width}\n\n**📏 HEIGHT** :{update.video.height} \n\n**🔗JOIN @TELSABOTS**", quote=True)
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)
    

@HB.on_message(filters.document & filters.private)
async def stickers(bot, update):    
    if update.document:
        await update.reply(f"** FILE NAME : {update.document.file_name}**\n\n**🏋️‍♂️ SIZE : {humanbytes(update.document.file_size)}**\n\n**🔖 MIME TYPE : {update.document.mime_type}**\n\n **🆔 FILE ID** `{update.document.file_id}`\n\n **🆔 UNIQUE ID** : `{update.document.file_unique_id}`** \n\n**📅 DATE : {update.document.date}**\n\n**🔗JOIN @TELSABOTS**", quote=True)
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)
    

@HB.on_message(filters.audio & filters.private)
async def stickers(bot, update):    
    if update.audio:
        await update.reply(f"**🎧 SONG : {update.audio.title}**\n\n**🎤 SINGER : {update.audio.performer}**\n\n** 📰 AUDIO NAME  : {update.audio.file_name}**\n\n**🏋️‍♂️ SIZE : {humanbytes(update.audio.file_size)}**\n\n **⏰ DURATION : {TimeFormatter(update.audio.duration* 1000)}** \n\n**🔖 MIME TYPE : {update.audio.mime_type}**\n\n **🆔 FILE ID** `{update.audio.file_id}`\n\n **🆔 UNIQUE ID** : `{update.audio.file_unique_id}`** \n\n**📅 DATE : {update.audio.date}**\n\n**🔗JOIN @TELSABOTS**", quote=True)
    
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)

@HB.on_message(filters.voice & filters.private)
async def stickers(bot, update):    
    if update.voice:
        await update.reply(f"**🏋️‍♂️ SIZE : {humanbytes(update.voice.file_size)}**\n\n **⏰ DURATION : {TimeFormatter(update.voice.duration* 1000)}** \n\n**🔖 MIME TYPE : {update.voice.mime_type}**\n\n **🆔 FILE ID** `{update.voice.file_id}`\n\n **🆔 UNIQUE ID** : `{update.voice.file_unique_id}`** \n\n**📅 DATE : {update.voice.date}**\n\n**🔗JOIN @TELSABOTS**", quote=True)
    
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)
        


@HB.on_message(filters.document & filters.private)
async def stickers(bot, update):    
    if update.document:
        await update.reply(f"**📰 FILE : {update.document.file_name}**\n\n**🏋️‍♂️ SIZE : {humanbytes(update.document.file_size)}**\n\n**🔖 MIME TYPE : {update.document.mime_type}**\n\n **🆔 FILE ID** `{update.document.file_id}`\n\n **🆔 UNIQUE ID** : `{update.document.file_unique_id}`** \n\n**📅 DATE : {update.document.date}**\n\n**🔗JOIN @TELSABOTS**", quote=True)
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)
    


@HB.on_message(filters.sticker & filters.private)
async def stickers(bot, update):    
    if update.sticker:
        await update.reply(f"**🏷 PACK : {update.sticker.set_name}**\n\n**📰 STICKER NAME : {update.sticker.file_name}**\n\n**🏋️‍♂️ SIZE : {humanbytes(update.sticker.file_size)}**\n\n **🧸 EMOJI : {update.sticker.emoji}** \n\n**🔖 MIME TYPE : {update.sticker.mime_type}**\n\n **🆔 STICKER ID** `{update.sticker.file_id}`\n\n **🆔 UNIQUE ID** : `{update.sticker.file_unique_id}` \n\n **🎨 ANIMATED** : {update.sticker.is_animated}**\n\n**📅 DATE : {update.sticker.date}**\n\n**📐 WIDTH** : {update.sticker.width}\n\n**📏 HEIGHT** :{update.sticker.height} \n\n**🔗JOIN @TELSABOTS**", quote=True)
    else:
        await update.reply_photo(photo="https://telegra.ph/file/a3937c3ddc19bb3300d89.jpg", caption=START_TEXT.format(update.from_user.first_name, update.from_user.id), reply_markup=START_BUTTONS)
    

#welcome

GROUP = "iwantmytg"
WELCONE_MSG = "<b>HELLO {},\n\n WELCOME TO HB GROUP\n JOIN OUR CHANNELS</b>"

WELCOME_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton('📢CHANNEL📢', url="https://t.me/+UZzc1ZqHvYXaLeNf"),
        InlineKeyboardButton('📢NEW MOVIES📢', url="https://t.me/+b31QfnWFdmcwYzVl")
        ],[
            InlineKeyboardButton('🧑‍💻DEV🧑‍💻', url="https://t.me/alluaddict"),
            InlineKeyboardButton('🔐CLOSE 🔐', callback_data='close')
        ]
]

@HB.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, update):
    text=WELCONE_MSG.format(update.from_user.mention)
    reply_markup = InlineKeyboardMarkup(WELCOME_MESSAGE_BUTTONS)
    update.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )




@HB.on_message(filters.channel & filters.text | filters.media )
async def tag(client, message):
 await message.copy(message.chat.id)
 
@HB.on_message(filters.command(["ping"]))
async def ping(client, message):
    start = datetime.now()
    tauk = await message.reply('....!')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await tauk.edit(f'**⚡️PONG: `{m_s} ms`**')

REPLY_MESSAGE_BUTTONS = [
    [
        ("😉START😉"),
        ("🆘HELP🆘"),
        ("🥳ABOUT🥳")
        
    ]
]
button_text = "CHOOSE ANY BUTTON BELOW"
@HB.on_message(filters.command('Kbuttons'))
def greet(bot, message):
    text = button_text
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True) 
    message.reply(
        text=text,
        reply_markup=reply_markup
    )

START_TEX ="HI  I AM A SIMPLE MEDIA INFO BOT \n\n BUT I CAN DO MORE"

@HB.on_message(filters.regex("START"))
def reply_to_START(bot,message):
    text=START_TEX
    reply_markup = START_BUTTONS
    message.reply_text(
    text=text,
    reply_markup=reply_markup
    )
@HB.on_message(filters.regex("HELP"))
def reply_to_HELP(bot,message):
    text= HELP_TEXT
    reply_markup = HELP_BUTTONS
    message.reply_text(
    text=text,
    reply_markup=reply_markup
    )
@HB.on_message(filters.regex("ABOUT"))
def reply_to_ABOUT(bot,message):
    text= ABOUT_TEXT
    reply_markup = ABOUT_BUTTONS
    message.reply_text(
    text=text,
    reply_markup=reply_markup
    )




@HB.on_message(filters.command(["info"]))
async def who_is(client, message):
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "`Fetching user info...`"
    )
    await status_message.edit(
        "`Processing user info...`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        return await status_message.edit("no valid user_id / message specified")
    message_out_str = ""
    message_out_str += f"<b>➲First Name:</b> {from_user.first_name}\n"
    last_name = from_user.last_name or "<b>None</b>"
    message_out_str += f"<b>➲Last Name:</b> {last_name}\n"
    message_out_str += f"<b>➲Telegram ID:</b> <code>{from_user.id}</code>\n"
    username = from_user.username or "<b>None</b>"
    dc_id = from_user.dc_id or "[User Doesn't Have A Valid DP]"
    message_out_str += f"<b>➲Data Centre:</b> <code>{dc_id}</code>\n"
    message_out_str += f"<b>➲User Name:</b> @{username}\n"
    message_out_str += f"<b>➲User 𝖫𝗂𝗇𝗄:</b> <a href='tg://user?id={from_user.id}'><b>Click Here</b></a>\n"
    if message.chat.type in (("supergroup", "channel")):
        try:
            chat_member_p = await message.chat.get_member(from_user.id)
            joined_date = datetime.fromtimestamp(
                chat_member_p.joined_date or time.time()
            ).strftime("%Y.%m.%d %H:%M:%S")
            message_out_str += (
                "<b>➲Joined this Chat on:</b> <code>"
                f"{joined_date}"
                "</code>\n"
            )
        except UserNotParticipant:
            pass
    chat_photo = from_user.photo
    if chat_photo:
        local_user_photo = await client.download_media(
            message=chat_photo.big_file_id
        )
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=local_user_photo,
            quote=True,
            reply_markup=reply_markup,
            caption=message_out_str,
            parse_mode="html",
            disable_notification=True
        )
        os.remove(local_user_photo)
    else:
        buttons = [[
            InlineKeyboardButton('🔐 Close', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=message_out_str,
            reply_markup=reply_markup,
            quote=True,
            parse_mode="html",
            disable_notification=True
        )
    await status_message.delete()


print("HB")
HB.run()
