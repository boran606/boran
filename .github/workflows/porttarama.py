#!/usr/bin/env python
#-*-coding:utf-8-*-
import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear', shell=True)
try:
    print ("""
[+]=========BORAN-PORT-TARAYICI========[+]
=========================================
[+]=========NO NMAP====================[+]
[+]=================PYTHON-BORAN======[+]
""")

    remoteServer    = raw_input("web adresi veya ip adresi giriniz: ")# Girdi Al
    remoteServerIP  = socket.gethostbyname(remoteServer)

    print "_" * 60
    print "ADRES TARANIYOR AMK AZ BEKLE SABIR ET ÇIKMA ANANI SİKERİM", remoteServerIP
    print "_" * 60


    t1 = datetime.now()



    try:
        for port in range(1,1024):#Portları 1-1023'e kadar tarıyoruz..
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	Şaaaaaaaaaaaaak AL SANA PORT AÇIĞI -efe aydal".format(port)
            sock.close()
    #Bu exceptleri koymamızın sebebi programın kırılmasını önlüyoruz.
    except KeyboardInterrupt:
        print "ŞİMDİ ANANI LACİVERDE BOYADIM"
        sys.exit()

    except socket.error:
        print "Servera bağlanılamıyor amk discord gel sorunu çözelim aslan Firevenom#0001"
        sys.exit()
    t2 = datetime.now()
    total =  t2 - t1
    print ("Port Taraması:{} sürede tamamlandı h.o knk".format(total))
except socket.gaierror:
    sys.stderr.write("Girilen Değer {} uygun formatta değil ki amk\n".format(remoteServer))
