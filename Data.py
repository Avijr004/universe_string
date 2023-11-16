from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton(" sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ ", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text=" ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ ", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                " ᴏᴜʀ ᴏᴛʜᴇʀ ʙᴏᴛs ᴀɴᴅ sᴛᴀᴛᴜs ", url="https://t.me/we_are_universee"
            )
        ],
        [
            InlineKeyboardButton(" ʜᴏᴡ ᴛᴏ ᴜsᴇ ", callback_data="help"),
            InlineKeyboardButton(" ᴀʙᴏᴜᴛ ", callback_data="about"),
        ],
        [InlineKeyboardButton(" ᴏᴛʜᴇʀ ʙᴏᴛs ", url="https://t.me/we_are_universee")],
    ]

    START = """
ʜᴇʏ {}
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}
ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ, 
1) sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ
sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. ᴜsᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !
ʙʏ @we_are_universee
    """

    HELP = """
 **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** 

/about - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/help - ᴛʜɪs ᴍᴇssᴀɢᴇ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/repo - ɢᴇᴛ ʀᴇᴘᴏ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
/restart - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇss
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 

ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @we_are_universee

sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://telegra.ph/file/b2357a4250403e0a96c98.jpg)
ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)
ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)
ᴏᴡɴᴇʀ : @lochakpochak
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
𝘼 𝙋𝙊𝙒𝙀𝙍𝙁𝙐𝙇𝙇 𝘽𝙊𝙏
𝙊𝙁 𝙐𝙉𝙄𝙑𝙀𝙍𝙎𝙀
━━━━━━━━━━━━━━━━━
ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ғᴏʀ ᴛɢ...
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝘾𝙍𝙀𝘼𝙏𝙀𝙍 [𝙊𝙒𝙉𝙀𝙍](https://t.me/lochakpochak)
┣★ 𝙑𝙋𝙎 𝙎𝙀𝙇𝙇  [𝙑𝙋𝙎](https://t.me/we_are_universee)
┣★ 𝘽𝙊𝙏 𝙐𝙋𝘿𝘼𝙏𝙀𝙎 [𝙊𝙐𝙍 𝘽𝙊𝙏𝙎](https://t.me/universe_we_are)
┣★ 𝙎𝙊𝙐𝙍𝘾𝙀 𝘾𝙊𝘿𝙀 : [𝘾𝙇𝙄𝘾𝙆 𝙃𝙀𝙍𝙀](https://telegra.ph/file/b2357a4250403e0a96c98.jpg)
┣★ 𝙉𝙀𝙏𝙒𝙊𝙍𝙆 [𝙐𝙉𝙄𝙑𝙀𝙍𝙎𝙀](https://t.me/universe_we_are)
┗━━━━━━━━━━━━━━━━━┛
💞 
IF HAVE ANY QUESTION THEN CONTACT » TO » MY » [𝙉𝙀𝙏𝙒𝙊𝙍𝙆] @lochakpochak
   """
