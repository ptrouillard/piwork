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

def sauvegarde (date, temperature1, temperature2, emplacement) :
    fichierSauvegarde = open(emplacement, "a")
    fichierSauvegarde.write(str(date)+";")
    fichierSauvegarde.write(str(temperature1)+";")
    fichierSauvegarde.write(str(temperature2)+"\r\n");
    fichierSauvegarde.close()
    
while True :
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    contenuFich2 = lireFichier("/sys/bus/w1/devices/28-021091776496/w1_slave")
    contenuFich1 = lireFichier("/sys/bus/w1/devices/28-020f917745e2/w1_slave")
    temperature2 = recupTemp(contenuFich2)
    temperature1 = recupTemp(contenuFich1)
    sauvegarde(date, temperature1, temperature2,"Temperature.csv")
    time.sleep(60)
