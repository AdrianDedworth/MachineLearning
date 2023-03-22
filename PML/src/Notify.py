from src.connect_database import connection
from sms_api.altiria_client import *
import time

def Notify():
    time.sleep(2)
    cursorGetPhoneNum = connection.cursor()
    pCode = '51'
    msg = "ALERTA\nSe ha detectado un intruso en tu hogar.\nRevisa las camaras:\nhttp://localhost:5000/camera"

    GetPNum = "CALL SP_GetPhoneNumber"
    cursorGetPhoneNum.execute(GetPNum)

    usrToNotify = cursorGetPhoneNum.fetchall()

    for pNumber in usrToNotify:
        try:
            client = AltiriaClient('max12_0@hotmail.com', 'eb9s6day')
            textMessage = AltiriaModelTextMessage(pCode + str(pNumber), msg) #(numero_para_enviar, texto)
            jsonText = client.sendSms(textMessage)
            print('¡Mensaje enviado!')
        except AltiriaGwException as ae:
            print('Mensaje no aceptado:'+ae.message)
            print('Código de error:'+ae.status)
        except JsonException as je:
            print('Error en la petición:'+je.message)
        except ConnectionException as ce:
            if "RESPONSE_TIMEOUT" in ce.message:
                print('Tiempo de respuesta agotado:'+ce.message)
            else:
                print('Tiempo de conexión agotado:'+ce.message)
#Notify()

# # from urllib import response
# from connect_database import connection
# # from datetime import datetime
# # import pywhatkit
# import requests
# import json
# # from flask import Response

# def Notify():
#     cursorGetPhoneNum = connection.cursor()
#     product = "whatsapp"
#     pCode = "51"
#     contador = 0
#     # msg = "Se ha detectado un intruso, revisa las camaras."

#     GetPNum = "CALL SP_GetPhoneNumber"
#     cursorGetPhoneNum.execute(GetPNum)

#     usrToNotify = cursorGetPhoneNum.fetchall()

#     # hora = datetime.now()
#     for pNumber in usrToNotify:
#         payload = {"messaging_product" : product, "to" : pCode+str(pNumber[contador])}
#         contador += 1
#         # headers = {
#         #     "Authorization": "Bearer EAAFu62igLoQBAPuNfEDZAFq7T2p4aMb4yskNlwXeTfBm2w83Klf6xKFn8CaP7EmfKlUG2iJZBdkpM9MMLhrKsoK9LzjEA2eTH7WZAyQvrYId9abZCPl1lb1gHAfRen6sqkY3ZB1VVZArXZCErI0V643z0O3JwJBml05jcGLVUpKsAtUHOyZAFO66DAZCbjRSqC1MjRNQuYDllrgZDZD",
#         #     "Content-Type": "application/json"
#         #     }
#         # req = requests.Request("GET", "https://graph.facebook.com/v13.0/108545071893777/messages", data=payload)
#         # r = req.prepare()

#         # s = requests.Session()
#         # s.send(r)
#         # print(req)
#         # print(req.reason)
#     #     pywhatkit.sendwhatmsg(pCode + str(pNumber), msg, hora.hour, hora.minute)


# Notify()