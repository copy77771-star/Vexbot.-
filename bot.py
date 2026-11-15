import telebot, time, threading
bot = telebot.TeleBot("9066558788:AAHv3_v90JuF-GhkTKLFsa2eaQv5MlYEmf4")
C = ["Ты красивая 😍", "Ты милая 🌸", "Ты умная ✨", "Ты стильная 🎨", "Ты чудо 💫"]
m = {}
ci = 0

def au(cid):
    time.sleep(600)
    if cid in m: m.pop(cid)

@bot.business_message_handler(content_types=['text'])
def h(msg):
    global ci
    if not msg.text: return
    t = msg.text.lower(); cid = msg.chat.id; con = msg.business_connection_id
    if cid in m:
        if t == '.unmute':
            m.pop(cid); bot.send_message(cid, "Мут снят", business_connection_id=con)
        else:
            try: bot.delete_message(cid, msg.message_id)
            except: pass
        return
    if t.startswith('.flirt'):
        bot.send_message(cid, C[ci % len(C)], business_connection_id=con); ci += 1
    elif t.startswith('.spam'):
        p = t.split()
        if len(p) >= 3:
            for _ in range(min(int(p[-1]), 20)):
                bot.send_message(cid, " ".join(p[1:-1]), business_connection_id=con); time.sleep(0.5)
    elif t.startswith('.mute'):
        m[cid] = True; bot.send_message(cid, "Мут 10 мин", business_connection_id=con)
        threading.Thread(target=au, args=(cid,), daemon=True).start()

print("БОТ ЗАПУЩЕН!")
bot.polling(none_stop=True)
