print("Запускаем бота....")
from pyrogram import Client, filters
from pendulum import now
with open("privetdict.txt", "r", encoding="utf-8") as file:
    try:
        privetdict = dict(eval(file.read()))
    except Exception as e:
        privetdict = {}
bot = Client("bot", api_id=20204392, api_hash="205301a174955988a8b1558551f111fa")
@bot.on_message(filters.me & filters.command(["инфо", "info"], ["/", "."]))
async def info(_, message):
    if message.reply_to_message:
        await message.edit(message.reply_to_message)
    else:
        await message.edit("Не обнаружен ответ на сообщение!")
@bot.on_message(filters.me & filters.command(["айди", "id"], [".", "/"]))
async def gifid(_, message):
    if not message.reply_to_message:
        await message.edit("Не обнаружен ответ на сообщение!")
    elif message.reply_to_message.animation:
        await message.edit(message.reply_to_message.animation.file_id)
    elif message.reply_to_message.photo:
        await message.edit(message.reply_to_message.photo.file_id)
    elif message.reply_to_message.sticker:
        await message.edit(message.reply_to_message.sticker.file_id)
    else:
        await message.edit("Не обнаружено гиф или изображение!")
@bot.on_message(filters.me & filters.command(["спам", "spam"], [".", "/"]))
async def spam(_, message):
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    text = " ".join(res)
    await message.delete()
    count = 0
    while count != counts:
        count += 1
        await message.reply_text(text)
@bot.on_message(filters.me & filters.command(["спамгиф", "spamgif"], ["/", "."]))
async def spamgif(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    for i in range(counts):
        await message.reply_animation(fileid, False)
@bot.on_message(filters.me & filters.command(["спамфото", "spamphoto"], ["/", "."]))
async def spamphoto(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    for i in range(counts):
        await message.reply_photo(fileid, False)
@bot.on_message(filters.me & filters.command(["спамстикер", "spamsticker"], ["/", "."]))
async def spamsticker(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    for i in range(counts):
        await message.reply_sticker(fileid, False)
@bot.on_message(filters.me & filters.command("приветствие", ["/", "."]))
async def privetnovokek(_, message):
    res = message.command
    res.pop(0)
    text = " ".join(res)
    privetdict[str(message.chat.id)] = text
    with open("privetdict.txt", "w", encoding="utf-8") as f:
        f.write(str(privetdict))
    await message.edit("Включено!")
@bot.on_message(filters.new_chat_members)
async def privetnovokek2(_, message):
    if str(message.chat.id) in list(privetdict):
        await message.reply(privetdict[str(message.chat.id)])
@bot.on_message(filters.me & filters.command("часы", [".", "/"]))
async def vremya(_, message):
    await message.edit("Включили!")
    oldTime = None
    while True:
        newTime = ":".join(str(now()).split("T")[1].split(":")[:2])
        if newTime != ":".join(str(now()).split("T")[1].split(":")[:2]):
            await bot.update_profile(newTime)
            oldTime = ":".join(str(now()).split("T")[1].split(":")[:2])
print("Бот запущен!")
bot.run()
