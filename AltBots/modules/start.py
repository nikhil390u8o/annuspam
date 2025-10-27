from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ASUR_SAMRAJY_NET"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/ASUR_SAMRAJY_NET")
    ],
    [
        Button.url("• ʀᴇᴘᴏ •", "https://t.me/REPO_679/2")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𓆩𝐀𝐒𓆪 ꭙ 𝐉𝐄𝐑𝐑𝐘 ⌯ 𝐊𝐈𝐍𝐆💀 #𝐅𝐔𝐂𝐊𝐄𝐑](tg://openmessage?user_id=7290768963)**\n\n"
        TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://files.catbox.moe/mg5jsu.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
