import telebot, os, random

TOKEN=os.getenv("TOKEN")
bot=telebot.TeleBot(TOKEN)

PACKS=[500,1000,4000]

def file(p): return f"codes_{p}.txt"

def gen():
    return "SVI"+''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",k=13))

@bot.message_handler(commands=["refill"])
def refill(m):
    for p in PACKS:
        with open(file(p),"a") as f:
            for _ in range(20):
                f.write(gen()+"\n")
    bot.send_message(m.chat.id,"✅ Codes generated & added")

bot.infinity_polling()
