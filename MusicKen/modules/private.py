import logging
from MusicKen.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicKen.config import SOURCE_CODE, ASSISTANT_NAME, PROJECT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME, OWNER, KENKAN
from MusicKen.helpers.decorators import authorized_users_only

logging.basicConfig(level=logging.INFO)


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited 
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAFF-KFg-jaEvlhu_kNknYQjxsuyDvp--AACjAMAAtpWSVeocCICILIfRSAE")
    await message.reply_text(
        f"""ππ» Hallo, Nama saya [{PROJECT_NAME}](https://telegra.ph/file/ed136c19e7f6afddb4912.jpg)
Dikekolah oleh {OWNER}
γ»β¦β­β­β­β­β§β¦β¦β¦β§β­β­β­β­β¦ γ»
βοΈ Saya memiliki banyak fitur untuk anda yang suka lagu
π Memutar lagu di group 
π Memutar lagu di channel
π Mendownload lagu
π Mencari link youtube
γ»β¦β­β­β­β­β§β¦β¦β¦β§β­β­β­β­β¦ γ»
βοΈ Klik tombol bantuan untuk informasi lebih lanjut
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βοΈ ππππ", callback_data = f"help+1"),
                    InlineKeyboardButton(
                        "πππππ ππ πΏπΌππβ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "π₯ πππππ", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "πΎππΌππππ π£", url=f"https://t.me/{UPDATES_CHANNEL}")],
                [
                    InlineKeyboardButton("π πππΏπΌππ πππππ π", url=f"{SOURCE_CODE}"),
                    InlineKeyboardButton("π΅ ππΌππππ", url="https://t.me/abhinasroy")
                ]        
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption=f"""**π΄ {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = 'π΅ πππππ', url = f"t.me/{OWNER}")],
                    [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = 'πΎππΌππππ π£', url=f"https://t.me/{UPDATES_CHANNEL}")],
                    [InlineKeyboardButton("π πππΏπΌππ πππππ π", url=f"{SOURCE_CODE}"), InlineKeyboardButton("π΅ ππΌππππ", url="https://t.me/abhinasroy")]
                ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if pos==1:
        button = [
            [InlineKeyboardButton(text = 'β¬οΈ Sebelummya', callback_data = "help+5"),
             InlineKeyboardButton(text = 'Selanjutnya β‘οΈ', callback_data = "help+2")]
        ]
    elif pos==len(tr.HELP_MSG)-1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton(text = 'βοΈ ππππ', callback_data = f"help+1"),
             InlineKeyboardButton(text = 'πππππ ππ πΏπΌππβ', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
             InlineKeyboardButton(text = 'πΎππΌππππ π£', url=f"https://t.me/{UPDATES_CHANNEL}")],
            [InlineKeyboardButton("π πππΏπΌππ πππππ π", url=f"{SOURCE_CODE}"), InlineKeyboardButton("π΅ ππΌππππ", url="https://t.me/abhinasroy")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'β¬οΈ sα΄Κα΄Κα΄α΄Ι΄Κα΄', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'sα΄Κα΄Ι΄α΄α΄α΄Ι΄Κα΄ β‘οΈ', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
@authorized_users_only
async def admincache(client, message: Message):
    await message.reply_photo(
      photo=f"{KENKAN}",
      caption="β **Bot berhasil dimulai ulang!**\n\n **Daftar admin telah diperbarui**",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = 'π΅ πππππ', url = f"t.me/{OWNER}")],
                    [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = 'πΎππΌππππ π£', url=f"https://t.me/{UPDATES_CHANNEL}")],
                    [InlineKeyboardButton("π πππΏπΌππ ππππππ", url=f"{SOURCE_CODE}"), InlineKeyboardButton("π΅ ππΌππππ", url="https://t.me/abhinasroy")]
                ]
        ),
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """
**π° Perintah**
      
**=>> Memutar Lagu π§**
      
β’ /play (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
β’ /ytplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
β’ /yt (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
β’ /p (nama lagu) - Untuk Memutar lagu yang Anda minta melalui youtube
β’ /dplay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui deezer
β’ /splay (nama lagu) - Untuk Memutar lagu yang Anda minta melalui jio saavn
β’ /player: Buka menu Pengaturan pemain
β’ /skip: Melewati trek saat ini
β’ /pause: Jeda trek
β’ /resume: Melanjutkan trek yang dijeda
β’ /end: ββMenghentikan pemutaran media
β’ /current: Menampilkan trek yang sedang diputar
β’ /playlist: Menampilkan daftar putar
      
Semua Perintah Bisa Digunakan Kecuali Perintah /player /skip /pause /resume  /end Hanya Untuk Admin Grup
      
**==>>Download Lagu π₯**
      
β’ /song [nama lagu]: Unduh audio lagu dari youtube

**=>> Saluran Music Play π **
      
βͺοΈ Hanya untuk admin grup tertaut:
      
β’ /cplay (nama lagu) - putar lagu yang Anda minta
β’ /cdplay (nama lagu) - putar lagu yang Anda minta melalui deezer
β’ /csplay (nama lagu) - putar lagu yang Anda minta melalui jio saavn
β’ /cplaylist - Tampilkan daftar yang sedang diputar
β’ /cccurrent - Tampilkan sedang diputar
β’ /cplayer - buka panel pengaturan pemutar musik
β’ /cpause - jeda pemutaran lagu
β’ /cresume - melanjutkan pemutaran lagu
β’ /cskip - putar lagu berikutnya
β’ /cend - hentikan pemutaran musik
β’ /userbotjoinchannel - undang asisten ke obrolan Anda""",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = 'π΅ πππππ', url = f"t.me/{OWNER}")],
                    [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = 'πΎππΌππππ π£', url=f"https://t.me/{UPDATES_CHANNEL}")],
                    [InlineKeyboardButton("π πππΏπΌπππ", url=f"{SOURCE_CODE}"), InlineKeyboardButton("π΅ ππΌππππ", url="https://t.me/abhinasroy")]
                ]
        ),
    )


