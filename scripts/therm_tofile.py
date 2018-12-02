import time
import datetime

def lireFichier (emplacement) :
    fichTemp = open(emplacement)
    contenu = fichTemp.read()
    fichTemp.close()
    return contenu

def recupTemp (contenuFich) :
    secondeLigne = contenuFich.split("\n")[1]
    temperatureData = secondeLigne.split(" ")[9]
    temperature = float(temperatureData[2:])
    temperature = temperature / 1000
    return temperature

def sauvegarde (temperature, date, emplacement) :
    fichierSauvegarde = open(emplacement, "a")
    fichierSauvegarde.write(str(date)+"   ")
    fichierSauvegarde.write(str(temperature)+'\r\n')
    fichierSauvegarde.close()
    
while True :
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    contenuFich = lireFichier("/sys/bus/w1/devices/28-021091776496/w1_slave")
    temperature = recupTemp(contenuFich)
    sauvegarde(temperature, date, "Temperature.txt")
    time.sleep(60)
