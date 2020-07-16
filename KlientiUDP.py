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
     KlientiUDP= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     KlientiUDP.connect((EmriServerit,PortiServerit))
except Exception :
         print("Nuk eshte realizuar lidhja mes klientit dhe serverit.")
         time.sleep(60)

print("===============================================================================")
print("                                KLIENTI UDP                                    ")
print("===============================================================================")
while True:
    print("Metodat: IPADDRESS, PORTI, GCF,\n\t GAME, REVERSE, COUNT, NUMBER, EVENODD,\n\t FACTORIEL, CONVERT,PALINDROME, TIME, SWAP")
    teksti = input("Shkruani kerkesen(nese nuk deshironi te vazhdoni shtypni mbylle: ")
    if teksti == "mbylle":
        sys.exit()
    mesazhi = ''
    KlientiUDP.sendto(teksti.encode(),(EmriServerit,PortiServerit))
    TeDhenat, Adresa = KlientiUDP.recvfrom(128)
    mesazhi += TeDhenat.decode("utf-8")
    print('Te dhenat e pranuara nga serveri: ' + mesazhi)
    print ("-------------------------------------------------------------------------")

KlientiUDP.close()
