# importamos token
import os
from dotenv import load_dotenv
load_dotenv()
access_token = os.getenv('TELEGRAM_TOKEN')
access_id = os.getenv('MI_CHAT_ID')

import telebot # para manejar la API de telegram
import time
import threading
import random
import importlib
import Scrapingweb # importamos modulo scraping de trafico
import datetime






# instanciamos el bot de telegram
bot = telebot.TeleBot(access_token)
bot.set_webhook()

############################################# 
 
#Listener
 
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
 
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        fecha_y_hora_actual = datetime.datetime.now() # Capturamos la hora en el momento que el usuario pulse el comando para guardarla en log.txt

        fecha_y_hora_actual_formateada = fecha_y_hora_actual.strftime('%d/%m/%Y %H:%M:%S') # Formateamos la fecha con los datos necesarios
 
        cid = m.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
 
        if cid > 0:
 
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text + (" ") + (fecha_y_hora_actual_formateada)# Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
 
        else:
 
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text + (" ") + (fecha_y_hora_actual_formateada)# Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.
 
        f = open( './log.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
 
        f.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
 
        f.close() # Cerramos el fichero para que se guarde.
 
        print (mensaje) # Imprimimos el mensaje en la terminal, que nunca viene mal :) 
 
 
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

########################################################################

# responde al comando /start
@bot.message_handler(commands=["start", "ayuda", "help"])
def cmd_start(message):
    """Da la bienvenida al usuario del bot"""
    bot.reply_to(message, "👋🏻 Hola, este es un Bot que te ayudara a consultar las cámaras de trafico tanto en sentido ascendente como descendente de la carretera A5 desde el Km-0 al Km-60.🚗📹 \n \nTambien podras consultar las incidencias de trafico en tiempo real desde el Km-0 al Km-60.🚗🚕🚒🚓 \n \nPara ello tenemos 3 comandos que podras activar desde la casilla Menú que se encuentra junto a la caja de texto. \n⬇️")
    print(message.chat.id)

@bot.message_handler(commands=["camaras_a5_d"])
def cmd_Camaras(message):
    """muestras las camaras en sentido decreciente"""
    numero = random.randint(10000, 10000000) # Genera numero aleatorio para poner foto actualizada
    bot.send_message(message.chat.id, "⬇️🚗🎥CAMARAS EN SENTIDO DECRECIENTE🎥🚗⬇️"),
    bot.send_message(message.chat.id, "🎥 Valmojado 43.4 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/802.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Calypo 35.8 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/1157.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Navalcarnero 31.6 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/839.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Arroyomolinos 24,8 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/841.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Mostoles Xanadú 22,4 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/837.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Alcorcon 16.1 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/842.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 San José de Valderas 12.1 kM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/796.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Alto Extremadura 4.9 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/798.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Alto Extremadura 3.7 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/1125.jpg?t="+str(numero))
    time.sleep(3)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=["camaras_a5_c"])
def cmd_CamarasC(message):
    """muestras las camaras en sentido decreciente"""
    numero = random.randint(10000, 10000000) # Genera numero aleatorio para poner foto actualizada
    bot.send_message(message.chat.id, "⬇️🚗🎥CAMARAS EN SENTIDO CRECIENTE🎥🚗⬇️"),
    bot.send_message(message.chat.id, "🎥 Cerca Casa de Campo 5.9 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/797.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Campamento 6.4 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/788.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Campamento 6.8 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/790.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Campamento 7.9 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/795.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Antiguos cuarteles 8.9 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/791.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Cuatro Viento 9.6 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/792.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Alcorcón 12.6 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/789.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Alcorcón Centro 13.6 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/799.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Mostoles 18.8 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/843.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Navalcarnero 28 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/844.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Navalcarnero 29.6 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/838.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Navalcarnero Oeste 33.1 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/845.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 Urb. Calypo 37,5 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/803.jpg?t="+str(numero)),
    time.sleep(0.5)
    bot.send_message(message.chat.id, "🎥 A-5 48.8 KM 🎥"+" "+"http://infocar.dgt.es/etraffic/data/camaras/1452.jpg?t="+str(numero))
    time.sleep(3)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=["trafico_a5_d"])
def cmd_Trafico(message):
 #   """muestras trafico en A5"""
    importlib.reload(Scrapingweb)
    time.sleep(3)
    from Scrapingweb import code_html
    bot.send_message(message.chat.id, code_html, parse_mode="html")
    time.sleep(3)
    bot.delete_message(message.chat.id, message.message_id)


# responde a los mensajes de texto que no son comandos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    """Gestiona mensajes de texto recibidos """
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible")
    else:
        bot.send_message(message.chat.id, "No entiendo que me quieres decir")
        time.sleep(3)
        bot.delete_message(message.chat.id, message.message_id)

def recibir_mensajes():
    """Bucle infinito que comprueba si hay nuevos mensajes"""
    bot.infinity_polling()



# MAIN ####################################
if __name__ == '__main__':
    # Configuramos los comandos disponibles
    bot.set_my_commands([
        # telebot.types.BotCommand("/start", "main menu"),
        telebot.types.BotCommand("/camaras_a5_d", "Camaras en sentido Decreciente A5"),
        telebot.types.BotCommand("/camaras_a5_c", "Camaras en sentido Creciente A5"),
        telebot.types.BotCommand("/trafico_a5_d", "Incidencias de trafico en A5")
    ])

    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()   
    print('Bot iniciado')
    bot.send_message(access_id, "Bot iniciado!!")
