import telepot, Adafruit_DHT, subprocess    
from time import sleep

def on_chat_message(msg):
        chat_id = msg['chat']['id'] #prelevo id del mittente
        command = msg['text'] #prelevo testo del messaggio
        username = msg['chat']['username'] #prelevo username del mittente

        def temperatura():
                sensor = Adafruit_DHT.DHT11
                pin=4
                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
                if humidity is not None and temperature is not None:
                        bot.sendMessage(chat_id, ("Temperatura: {0:0.1f}*C\nUmidita': {1:0.1f}%".format(temperature, humidity)))

        #da usare con if command.startswith('/COMANDO')
        def comando_shell(): #funzione che invia un messaggio contenente l'output di un comando lanciato
                proc = subprocess.Popen([command[1:]],stdout=subprocess.PIPE, shell=True)
                (out, err) = proc.communicate()
                bot.sendMessage(chat_id, out)

        #Log su shell
        print 'Ricevuto comando: %s' % command,"da:", username

        if username == "SOSTITUIRE COL PROPRIO USERNAME SENZA @":
                if command == '/temp':
                        temperatura()
                else:
                        bot.sendMessage(chat_id, ("Comando non valido."))
        else:
                bot.sendMessage(chat_id, ("E tu chi cazzo sei? Non sei autorizzato ad eseguire comandi."))

TOKEN = "SOSTITUIRE COL PROPRIO TOKEN" #token del bot preso da BotFather
bot = telepot.Bot(TOKEN)
print 'Bot avviato!'
bot.message_loop({'chat': on_chat_message}, run_forever=True)
