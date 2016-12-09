import telepot, Adafruit_DHT
from time import sleep

def handle(msg):
        chat_id = msg['chat']['id'] #prelevo id del mittente
        command = msg['text'] #prelevo testo del messaggio
        username = msg['chat']['username'] #prelevo username del mittente

        #Log su shell
        print 'Ricevuto comando: %s' % command,"da:", username
        if username == "SOSTITUIRE COL PROPRIO USERNAME SENZA @":
                if command == '/temp':
                        sensor = Adafruit_DHT.DHT11 #imposto il tipo di sensore
                        pin=4 #prelevo i dati dalla GPIO4
                        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) #salvo i valori di umidita' e temperatura
                        if humidity is not None and temperature is not None: #se i dati sono validi li stampo con tipo float
                                bot.sendMessage(chat_id, ("Temperatura: {0:0.1f}*C\nUmidita': {1:0.1f}%\n".format(temperature, humidity)))
        else:
                bot.sendMessage(chat_id, ("E tu chi cazzo sei? Non sei autorizzato ad eseguire comandi."))

TOKEN = "SOSTITUIRE COL PROPRIO TOKEN" #token del bot preso da BotFather
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Bot avviato!')

while 1:
        sleep(10)
