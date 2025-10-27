import sys
import heroku3
from config import X1, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from os import execl, getenv
from telethon import events
from datetime import datetime


# 🏓 Ping command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply("» __𝐒𝐇𝐎𝐍𝐀𝐐𝐔𝐄𝐄𝐍__")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(
            f"__🤖 ᴘɪɴɢ__\n» `αиσиумσυѕ ραρα нєяє αв кιѕкι gαи∂ мαяυ {mp} ᴍꜱ`"
        )


# 🔁 Reboot command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        execl(sys.executable, sys.executable, *sys.argv)


# 🧑‍💻 Add sudo command
@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply("» __ᴄʜᴀʟ ᴛᴜᴊʜᴇ ᴀɴᴏɴʏᴍᴏᴜs ᴘᴀᴘᴀ ɴᴇ sᴜᴅᴏ ᴅᴇ ᴅɪʏᴀ ᴀꜱ...__")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]: Please setup your HEROKU_APP_NAME`")
            return
        heroku_var = app.config()

        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
            return

        if str(target) in sudousers:
            await ok.edit("» ᴀʙᴇ ᴛᴜ ᴘʜᴇʟᴇ sᴇ sᴜᴅᴏ ᴍᴇ ʜᴀɪ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
            heroku_var["SUDO_USERS"] = newsudo

    elif event.sender_id in SUDO_USERS:
        await event.reply("» ꜱᴏʀʀʏ, ʏᴇ ᴄᴏᴍᴍᴀɴᴅ ʙᴀss ᴛᴇʀᴀ ᴀɴᴏɴʏᴍᴏᴜs ʙᴀᴀᴘ ᴅᴇ sᴋᴛᴀ ʜᴀɪ.")

