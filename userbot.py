print("Запускаем бота....")
try:
    from pyrogram import Client, filters
    import random
except:
    from os import system

    system("pip install pyrogram")
    system("pip install tgcrypto")
    from pyrogram import Client, filters
try:
    from pendulum import now
except:
    from os import system

    system("pip install pendulum")
    from pendulum import now
from threading import Thread

try:
    from speedtest import Speedtest
except:
    from os import system
    system("pip install speedtest-cli")
    from speedtest import Speedtest
from asyncio import gather
with open("privetdict.txt", "w+", encoding="utf-8") as file:
    try:
        privetdict = dict(eval(file.read()))
    except Exception as e:
        privetdict = {}
bot = Client("bot", api_id=14998650, api_hash="fb31c538a8c3bf049b0c13f56dceb53b")
st = Speedtest()


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
    elif message.reply_to_message.video:
        await message.edit(message.reply_to_message.video.file_id)
    elif message.reply_to_message.voice:
        await message.edit(message.reply_to_message.voice.file_id)   
    elif message.reply_to_message.video_note:
        await message.edit(message.reply_to_message.video_note.file_id)             
    else:
        await message.edit("Не обнаружено гиф или изображение или стикер или видео!")



@bot.on_message(filters.me & filters.command(["спам", "spam"], [".", "/"]))
async def spam(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    text = " ".join(res)
    for _ in range(counts):
        await message.reply(text)



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

@bot.on_message(filters.me & filters.command(["спамвидео", "spamvideo"], ["/", "."]))
async def spamvideo(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    for i in range(counts):
        await message.reply_video(fileid, False)


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


@bot.on_message(filters.me & filters.command(["пинг", "ping"], ["/", "."]))
async def internet(_, message):
    await message.edit("Загрузка....")
    mb = round(st.download() / 1000000, 2)
    st.get_best_server()
    ping = round(st.results.ping, 2)
    await message.edit(f"Скорость: {mb} мегабайт в секунду\nПинг: {ping}")

@bot.on_message(filters.me & filters.command(["ультраспам", "ultraspam"], [".", "/"]))
async def ultraspam(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    text = " ".join(res)
    gather(*[message.reply(text) for i in range(counts)])


@bot.on_message(filters.me & filters.command(["ультраспамгиф", "ultraspamgif"], ["/", "."]))
async def ultraspamgif(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    gather(*[message.reply_animation(fileid, False) for i in range(counts)])


@bot.on_message(filters.me & filters.command(["ультраспамфото", "ultraspamphoto"], ["/", "."]))
async def ultraspamphoto(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    gather(*[message.reply_photo(fileid, False) for i in range(counts)])


@bot.on_message(filters.me & filters.command(["ультраспамстикер", "ultraspamsticker"], ["/", "."]))
async def ultraspamsticker(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    gather(*[message.reply_sticker(fileid, False) for i in range(counts)])

@bot.on_message(filters.me & filters.command(["ультраспамвидео", "ultraspamvideo"], ["/", "."]))
async def ultraspamsticker(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    gather(*[message.reply_video(fileid, False) for i in range(counts)])

@bot.on_message(filters.me & filters.command(["спамгео", "spamgeo"], [".", "/"]))
async def spamgeo(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    text = " ".join(res)
    for _ in range(counts):
        await message.reply_venue(random.randint(-90, 90), random.randint(-180, 180), text, '')

@bot.on_message(filters.me & filters.command(["ультраспамгс", "ultraspamgs"], ["/", "."]))
async def ultravoice(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    gather(*[message.reply_voice(fileid, False) for i in range(counts)])

@bot.on_message(filters.me & filters.command(["спамгс", "спамгс"], ["/", "."]))
async def spamgs(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    for i in range(counts):
        await message.reply_voice(fileid, False)

@bot.on_message(filters.me & filters.command(["ультраспамкруг", "ultspamkrug"], ["/", "."]))
async def ultrar(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    gather(*[message.reply_video_note(fileid, False) for i in range(counts)])

@bot.on_message(filters.me & filters.command(["спамкруг", "spamkrug"], ["/", "."]))
async def spamkr(_, message):
    await message.delete()
    res = message.command
    res.remove(res[0])
    counts = int(res.pop(0))
    fileid = res[0]
    for i in range(counts):
        await message.reply_video_note(fileid, False)

print("Бот запущен!")
bot.run()
