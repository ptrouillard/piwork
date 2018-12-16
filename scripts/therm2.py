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

contenuFich1 = lireFichier("/sys/bus/w1/devices/28-020f917745e2/w1_slave")
contenuFich2 = lireFichier("/sys/bus/w1/devices/28-021091776496/w1_slave")

temperature1 = recupTemp (contenuFich1)
temperature2 = recupTemp (contenuFich2)

print "Temperature Capteur #1 : " ,
print temperature1
print "Temperature Capteur #2 : " ,
print temperature2
