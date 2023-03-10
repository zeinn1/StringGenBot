from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""๐ยฆุงููุง ุจูู ุนุฒููุฒู ๐ฌ {msg.from_user.mention},
โกยฆูููููู ุงุณุชูุฎูุฑุงุฌ ุงููุชูุงููู
โป๏ธยฆุชูุฑููููุณ ุชููุซูู ููุญุณูุงุจูุงุช๐
โป๏ธยฆุชูุฑููููุณ ุชููุซูู ููุจูุชููุงุช๐ค
๐งยฆุจุงููุฑูุฌูุฑุงู ููููุฒู ููุญุณุงุจุงุช๐๐ผโโ๏ธ
๐ฝยฆุจุงููุฑูุฌูุฑุงู ููููุฒู ุงุญุฏุซ ุงุตุฏุงุฑ๐
๐งยฆุจุงููุฑูุฌูุฑุงู ููููุฒู ููุจูุชุงุช๐ค
- ูุนููู ููุฐุง ุงูุจููุช ููุณุงุนุฏุชูู ุจุทุฑูููุฉ ุณูููู ููุญุตููู ุนูู ูููุฏ ุชูุฑูููุณ ูุชุดุบูู ุชูููุซูู ูุงูุจุงูุฑูุฌุฑุงู ูุชุดุบูู ุณููุฑุณ ุงุบููุงูู ุชู ุงูุดูุงุก ููุฐุง ุงูุจููุช ุจูุงุณุทูุฉ

ุจูุงุณุทูุฉ : [ูู๊ช.ููแูแฅฑแฅูู๊ช](tg://user?id=1355571767) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="๐ โ ุงุถุบุท ูุจุฏุง ุงุณุชุฎุฑุงุฌ ููุฏ โ๐", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("โ ุงูููุณูููููเขชุณู โ๏ธ", url="https://t.me/S_EG_P"),
                    InlineKeyboardButton("ีชแฅฑแฅ ฯแฅkแฅฑ๊ชแฅ๊ช", user_id=1355571767)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
