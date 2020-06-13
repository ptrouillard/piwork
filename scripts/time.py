import datetime

date = datetime.datetime.now()

date.hour

print date.hour,":",date.minute

if date.hour == 19:
	print "test"

if date.hour == 21 and date.minute == 0:
	print "Fermeture automatique de la porte du poulailler. Veuillez verifier que les poules sont bien rentrees."

if date.hour == 7 and date.minute == 0:
	print "Ouverture du poulailler. Les poules vont etre liberees."



