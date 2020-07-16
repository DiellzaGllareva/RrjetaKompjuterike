import socket
import random
import datetime
import threading

# Definimi i metodave
def IPADDRESS(a):
    return a[0]

def PORTI(a):
    return a[1]

def COUNT(a):
    zanoret = 0
    bashketingelloret = 0
    for z in a:
        if z in 'aeëiouyAEËIOUY':
            zanoret += 1
        elif z in "bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ":
            bashketingelloret += 1
    x = "Zanore :" + str(zanoret)
    y = "Bashketingellore : " + str(bashketingelloret)
    return [x, y]

def REVERSE(a):
    fjala = ""
    for i in a:
        fjala = i + fjala
    return fjala


def PALINDROME(a):
    if (a == a[:: - 1]):
        x = "Po teksti juaj eshte POLINDROM"
    else:
        x = "Jo teksti  juaj nuk eshte POLINDROM"
    y = str(x)
    return y


def TIME():
    from datetime import datetime
    x = datetime.now()
    y = "Koha aktuale te pc-ne tuaj eshte : " + str(x)
    return y


def GAME():
    x = random.sample(range(1, 35), 5)
    y = "Numra te cfaredoshem ne rangun [1,35] : " + str(x)
    return y


def GCF(a, b):
    if (b == 0):
        return a
    else:
        return GCF(b, a % b)


def CONVERT(a, b):
    if a == "CMTOFEET":
        x = 0.0328 * b
        y = "" + str(x) + "ft"
        return y
    elif a == "FEETTOCM":
        x = b / 0.032808
        y = "" + str(x) + "cm"
        return y
    elif a == "KMTOMILES":
        x = b * 0.62137
        y = "" + str(x) + "miles"
        return y
    elif a == "MILESTOKM":
        x = b / 0.62137
        y = "" + str(x) + "km"
        return y


def FACTORIEL(a):
    if a == 1:
        return 1
    else:
        return a * FACTORIEL(a - 1)


def EVENODD(a):
    x = a % 2
    if x == 0:
        y = "Numri eshte cift"
        return y
    else:
        y = "Numri eshte tek"
        return y


def NUMBER(a):
    if a > 0:
        y = "Numri i dhene eshte numer pozitiv"
        return y
    elif a == 0:
        y = "Numri i dhene eshte zero"
        return y
    else:
        y = "Numri i dhene eshte numer negativ"
        return y


def SWAP(a, b):
    x = a
    a = b
    b = x
    y = 'Vlera e parametrit te pare pas shkembimit eshte: {}'.format(a)
    z = 'Vlera e parametrit te dyte pas shkembimit eshte: {}'.format(b)
    return y, z

class ClientThread(threading.Thread):
    def __init__(self,AdresaKlientit,KlientSoketi):
        threading.Thread.__init__(self)
        self.ksocket = KlientSoketi
        print ("U shtua komunikimi me klientin: ", AdresaKlientit)
    def run(self):
        while True:
            kerkesa = self.ksocket.recv(128)
            kerkesa = kerkesa.decode()
            kerkesa = kerkesa.upper()
            teksti = kerkesa.split(" ")
            print('Kerkesa nga klienti:' + kerkesa)
            try:
                if teksti[0] == "IPADDRESS":
                    mesazhi = str(IPADDRESS(AdresaKlientit))
                elif teksti[0] == "PORTI":
                    mesazhi = str(PORTI(AdresaKlientit))
                elif teksti[0] == "COUNT":
                     mesazhi = str(COUNT(kerkesa[len(teksti[0]):len(kerkesa)]))
                elif teksti[0] == "REVERSE":
                    mesazhi = str(REVERSE(kerkesa[len(teksti[0]):len(kerkesa)]))
                elif teksti[0] == "PALINDROME":
                    mesazhi = str(PALINDROME(teksti[1]))
                elif teksti[0] == "TIME":
                    mesazhi = str(TIME())
                elif teksti[0] == "GAME":
                    mesazhi = str(GAME())
                elif teksti[0] == "GCF":
                    try:
                     mesazhi = str(GCF(int(teksti[1]), int(teksti[2])))
                    except Exception:
                     mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden gcf dhe dy numra per te realizuar metoden."
                elif teksti[0] == "CONVERT":
                    try:
                     mesazhi = str(CONVERT(teksti[1], int(teksti[2])))
                    except Exception :
                     mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden cmtofeet/feettocm/milestokm/kmtomiles dhe nje numer te plote."
                elif teksti[0] == "FACTORIEL":
                    try:
                     mesazhi = str(FACTORIEL(int(teksti[1])))
                    except Exception:
                     mesazhi= "Ka ndodhur nje gabim. Ju lutem shkruani metoden factoriel dhe nje numer te plote."
                elif teksti[0] == "EVENODD":
                    try:
                     mesazhi = str(EVENODD(int(teksti[1])))
                    except Exception :
                     mesazhi ="Ka ndodhur nje gabim. Ju lutem shkruani metoden evenodd dhe nje numer te plote."
                elif teksti[0] == "NUMBER":
                    try:
                     mesazhi = str(NUMBER(int(teksti[1])))
                    except Exception:
                     mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani emrin e metodes number dhe nje numer te plote."
                elif teksti[0] == "SWAP":
                    try:
                     mesazhi = str(SWAP(int(teksti[1]), int(teksti[2])))
                    except Exception :
                     mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani emrin e metodes swap dhe dy numra te plote."
                elif teksti[0]=="MBYLLE" :
                    mesazhi = "Klienti ka nderprere lidhjen me serverin"
                    break
                else:
                    mesazhi = str(dict[teksti[0]()](self.ksocket))
            except Exception:
                mesazhi = "Ka ndodhur nje gabim."
            finally:
                print("Mesazhi i derguar: " + mesazhi)
                self.ksocket.send(mesazhi.encode())
        print('Perfundoj komunikimi')
     
           
EmriServerit = 'localhost'
PortiServerit = 13000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((EmriServerit, PortiServerit))
print("===============================================================================")
print("                                SERVERI TCP                                    ")
print("===============================================================================")
print("Serveri eshte duke pritur kerkesen nga klienti ...")
while True:
    server.listen(5)
    KlientSoketi, AdresaKlientit = server.accept()
    newthread = ClientThread(AdresaKlientit, KlientSoketi)
    newthread.start()
