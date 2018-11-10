Générer les clés SSH

ssh-keygen

cd /home/pi/github/piwork
mkdir sshkeys
cd sshkeys
cp /home/pi/.ssh/id_rsa.pub id_rsa_pi3.pub
git add .
git commit -m "Clé publique rsa"
git push origin master

