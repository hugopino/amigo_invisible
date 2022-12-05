import random
import sys
import smtplib
from email.mime.text import MIMEText
import time

emails = {
    "Jose": "jose@example.com",
    "Carlos": "carlos@example.com",
    "María": "maria@example.com",
    "Laura": "laura@example.com",
}
array = list(emails.keys())
regalos = []
send = True
def start():
    array2 = array.copy()
    persona = random.choice(array2)
    for nombre in array:
        persona = random.choice(array2)
        while(nombre == persona):
            persona = random.choice(array2)
            if(persona == nombre and len(array2) == 1):
                print("Error, hay que repetir el proceso")
                send = False
                sys.exit()
        regalos.append(persona)
        array2.remove(persona)

def send_emails():
    print("Enviando emails...")
    port = 465  # For SSL
    password = "pon_aqui_tu_contraseña"
    sender_email = "amigoinvisible@ejemplo.com"
    for i in range(0, len(array)):
        nombre = array[i]
        amigo_invisible = regalos[i]
        receiver_email = emails[nombre]
        message = MIMEText(f"Hola {nombre}. Tu amigo invisible es: {amigo_invisible}.")
        message['Subject'] = f"{nombre} este es tu amigo invisible..."
        message['From'] = sender_email
        message['To'] = emails[nombre]

        server = smtplib.SMTP_SSL("mail.ejemplo.com", port)
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email], message.as_string())
        server.quit()
        print(f"Email ({i+1}/{len(array)})")
        time.sleep(5)

start()
if(send):
   send_emails()
   
