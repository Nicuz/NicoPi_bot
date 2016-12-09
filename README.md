# NicoPi_bot
Semplice Bot casalingo per conoscere la temperatura e l'umidità di un ambiente interno con l'utilizzo di un sensore DHT11.

![alt tag](https://github.com/Nicuz/NicoPi_bot/blob/master/nicopibot.png)

**Cablaggio:**
```
+ > 3.3V
- > GND
data > GPIO4
```

**Requisiti:**
* Adafruit_DHT
* telepot

**Come avviarlo in background con systemd**

Creare il file di configurazione lanciando:
`sudo nano /lib/systemd/system/NOME.service`

Inserire all'interno del file:
```
[Unit]
Description=DESCRIZIONE DEL SERVIZIO
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/UTENTE/NOME_FILE.py

[Install]
WantedBy=multi-user.target
```
Dare i permessi al file:
`sudo chmod 644 /lib/systemd/system/NOME.service`

Ricarichiamo i demoni e abilitiamo quello appena creato:
```
sudo systemctl daemon-reload
sudo systemctl enable NOME.service
```
Avviamo il nostro demone:
`sudo systemctl start NOME.service`

Controlliamo lo stato:
`sudo systemctl status NOME.service`
