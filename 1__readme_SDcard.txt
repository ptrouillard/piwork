Création de la carte mémoire sous MAC :

Eventuellement formatter la carte avec SDFormatter avant.

 df -h
 diskutil umount /dev/disk2s1
 sudo dd bs=1m if=2018-10-09-raspbian-stretch-lite.img of=/dev/rdisk2
 diskutil eject /dev/rdisk2

