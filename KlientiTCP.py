import socket
import time
import sys
teksti = input("A deshironi te vazhdoni me vlerat default te serverit? Shtypni po ose jo :")
if teksti == "jo" :
  EmriServerit = input("Shkruai ipaddressen e re :")
  PortiServerit = int(input("Shkruani portin e ri :"))
else :
  EmriServerit = 'localhost'
  PortiServerit = 13000
try:
     KlientiTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     KlientiTCP.connect((EmriServerit,PortiServerit))
except Exception :
         print("Nuk eshte realizuar lidhja mes klientit dhe serverit.")
         time.sleep(60)
print("===============================================================================")
print("                                KLIENTI TCP                                    ")
print("===============================================================================")

while True:
    print("Metodat: IPADDRESS, PORTI, GCF,\n\t GAME, REVERSE, COUNT, NUMBER, EVENODD,\n\t FACTORIEL, CONVERT,PALINDROME, TIME, SWAP")
    kerkesa = input("Shkruani kerkesen(nese nuk deshironi te vazhdoni shtypni mbylle): ")
    if kerkesa == "mbylle":
        KlientiTCP.send(str.encode(kerkesa))
        sys.exit()
    mesazhi = ''
    KlientiTCP.send(str.encode(kerkesa))
    tedhenat = KlientiTCP.recv(128)
    mesazhi += tedhenat.decode("utf-8")
    print('Te dhenat e pranuara nga serveri: ', mesazhi)
    print ("-------------------------------------------------------------------------")
KlientiTCP.close()
