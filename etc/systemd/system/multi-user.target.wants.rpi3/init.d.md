https://unix.stackexchange.com/questions/233468/how-does-systemd-use-etc-init-d-scripts

~~~sh
$ ls -l  /run/systemd/generator.late/multi-user.target.wants
total 0
lrwxrwxrwx 1 root root 50 Aug 13 15:53 dphys-swapfile.service -> /run/systemd/generator.late/dphys-swapfile.service
lrwxrwxrwx 1 root root 45 Aug 13 15:53 mosquitto.service -> /run/systemd/generator.late/mosquitto.service
lrwxrwxrwx 1 root root 39 Aug 13 15:53 ntp.service -> /run/systemd/generator.late/ntp.service
lrwxrwxrwx 1 root root 48 Aug 13 15:53 raspi-config.service -> /run/systemd/generator.late/raspi-config.service
~~~

~~~sh
$ ls -l /etc/init.d
total 308
-rwxr-xr-x 1 root root 5336 Feb  1  2016 alsa-utils
-rwxr-xr-x 1 root root 1398 Jan 25  2017 atop
-rwxr-xr-x 1 root root 1786 Jan 25  2017 atopacct
-rwxr-xr-x 1 root root 2401 Apr 13  2015 avahi-daemon
-rwxr-xr-x 1 root root 2948 Aug 18  2014 bluetooth
-rwxr-xr-x 1 root root 1276 Apr  6  2015 bootlogs
-rwxr-xr-x 1 root root 1248 Apr  6  2015 bootmisc.sh
-rwxr-xr-x 1 root root 3807 Feb 12  2017 checkfs.sh
-rwxr-xr-x 1 root root 1072 Apr  6  2015 checkroot-bootclean.sh
-rwxr-xr-x 1 root root 9353 Feb 12  2017 checkroot.sh
-rwxr-xr-x 1 root root 1232 Apr  7  2017 console-setup.sh
-rwxr-xr-x 1 root root 3049 Sep  5  2015 cron
-rwxr-xr-x 1 root root 2813 Oct 10  2016 dbus
-rwxr-xr-x 1 root root 1901 Sep 14  2015 dhcpcd
-rwxr-xr-x 1 root root 2198 Oct  1  2013 dphys-swapfile
-rwxr-xr-x 1 root root 6754 Feb 10  2018 exim4
-rwxr-xr-x 1 root root 6697 Apr 17  2017 fail2ban
-rwxr-xr-x 1 root root  824 Sep  5  2014 fake-hwclock
-rwxr-xr-x 1 root root 2413 Mar  3  2016 grafana
-rwxr-xr-x 1 root root 1336 Apr  6  2015 halt
-rwxr-xr-x 1 root root 1423 Apr  6  2015 hostname.sh
-rwxr-xr-x 1 root root 3809 Mar  7  2018 hwclock.sh
-rwxr-xr-x 1 root root 3635 Oct 25  2016 influxdb
-rwxr-xr-x 1 root root 1479 May 19  2016 keyboard-setup.sh
-rwxr-xr-x 1 root root 1300 Apr  6  2015 killprocs
-rwxr-xr-x 1 root root 2044 Dec 26  2016 kmod
-rwxr-xr-x 1 root root 2610 Jul 25  2011 lightdm
-rwxr-xr-x 1 root root 3323 Nov  3  2016 mosquitto
-rwxr-xr-x 1 root root  995 Apr  6  2015 motd
-rwxr-xr-x 1 root root 2477 Mar 30  2014 motion
-rwxr-xr-x 1 root root  677 Apr  6  2015 mountall-bootclean.sh
-rwxr-xr-x 1 root root 2301 Feb 12  2017 mountall.sh
-rwxr-xr-x 1 root root 1461 Apr  6  2015 mountdevsubfs.sh
-rwxr-xr-x 1 root root 1564 Apr  6  2015 mountkernfs.sh
-rwxr-xr-x 1 root root  685 Apr  6  2015 mountnfs-bootclean.sh
-rwxr-xr-x 1 root root 2456 Apr  6  2015 mountnfs.sh
-rwxr-xr-x 1 root root 4597 Sep 16  2016 networking
-rwxr-xr-x 1 root root 5658 Aug 13  2014 nfs-common
-rwxr-xr-x 1 root root 1561 Feb 15  2018 ntp
-rwxr-xr-x 1 root root 1366 Nov 15  2015 plymouth
-rwxr-xr-x 1 root root  752 Nov 17  2014 plymouth-log
-rwxr-xr-x 1 root root 1191 Nov 22  2016 procps
-rwxr-xr-x 1 root root 1210 Jul  4  2017 raspi-config
-rwxr-xr-x 1 root root 6290 Feb 12  2017 rc
-rwxr-xr-x 1 root root  820 Apr  6  2015 rc.local
-rwxr-xr-x 1 root root  117 Feb 12  2017 rcS
-rw-r--r-- 1 root root 2427 Feb 12  2017 README
-rwxr-xr-x 1 root root  661 Apr  6  2015 reboot
-rwxr-xr-x 1 root root 1042 Apr  6  2015 rmnologin
-rwxr-xr-x 1 root root 2358 May  5  2017 rpcbind
-rwxr-xr-x 1 root root 4417 Mar 15  2019 rsync
-rwxr-xr-x 1 root root 2868 Jan 18  2017 rsyslog
-rwxr-xr-x 1 root root 3207 Apr  6  2015 sendsigs
-rwxr-xr-x 1 root root  597 Apr  6  2015 single
-rw-r--r-- 1 root root 1087 Feb 12  2017 skeleton
-rwxr-xr-x 1 root root 4033 Mar  1  2018 ssh
-rwxr-xr-x 1 root root  731 Jan  5  2016 sudo
-rwxr-xr-x 1 root root 5759 Sep 12  2019 telegraf
-rwxr-xr-x 1 root root 3217 Aug 30  2016 triggerhappy
-rwxr-xr-x 1 root root 6087 Dec  3  2017 udev
-rwxr-xr-x 1 root root 2748 Feb 12  2017 umountfs
-rwxr-xr-x 1 root root 2202 Apr  6  2015 umountnfs.sh
-rwxr-xr-x 1 root root 1234 Feb 12  2017 umountroot
-rwxr-xr-x 1 root root 1361 Dec  6  2013 unattended-upgrades
-rwxr-xr-x 1 root root 3111 Apr  6  2015 urandom
-rwxr-xr-x 1 root root 2757 Jul 14  2016 x11-common
~~~
