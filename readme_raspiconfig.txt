A faire après création de la SDcard:

premier login : pi / rqspberry (clavier en anglais donc le a est un q)

 sudo raspi-config
 
 * Localisation options : installer les locales FR (iso8859 et utf-8)
 * Changer la langue du clavier : passer en FR
 * network options : connecter au wifi et choisir un hostname facile à identifier sur le réseau (exemple : pi3, pi2)
 * boot options : démarrer en mode console avec login automatique (en cas de problème de clavier, de mot de passe oublié on peut quand même accéder au rasbperry)
 * change user password : choisir un nouveau mot de passe
 * update : lancer la mise à jour de l'outil raspi-config
 
 sudo reboot (proposé en sortant de raspi-config)
 sudo apt-get install git
 
 mkdir github
 cd github
 git clone https://github.com/ptrouillard/piwork.git
 
 
