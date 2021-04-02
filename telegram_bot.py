# pip install telepot
import time
import telepot
from covid19 import get_data
from telepot.loop import MessageLoop

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	data = get_data()
	print(data)
	if content_type == 'text':
		user_text = msg['text']
	if user_text == "start":
		covid_text = 'Corona virus statistikasini bilishni istaysizmi ?'
		bot.sendMessage(chat_id, covid_text)
	if user_text == "ha":
		bot.sendMessage(chat_id, f"Aniqlanganlar - {data[0]},\n \
		Sog'ayganlar - {data[1]}, \n O'lganlar - {data[2]} \n \
		Davolanishda - {data[3]}")
		
TOKEN = '1720356473:AAHPCnX2ukbcteThhYO2eVNv2WxO74jQ2Bs'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)