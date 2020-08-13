https://unix.stackexchange.com/questions/233468/how-does-systemd-use-etc-init-d-scripts

~~~sh
$ ls -l  /run/systemd/generator.late/multi-user.target.wants
total 0
lrwxrwxrwx 1 root root 23 Aug 12 23:39 raspi-config.service -> ../raspi-config.service
lrwxrwxrwx 1 root root 20 Aug 12 23:39 rng-tools.service -> ../rng-tools.service
~~~

~~~sh
$ ls -l /etc/init.d
total 164
-rwxr-xr-x 1 root root 5336 Mar 30  2019 alsa-utils
-rwxr-xr-x 1 root root 1400 Jan 25  2019 atop
-rwxr-xr-x 1 root root 1786 Jan 25  2019 atopacct
-rwxr-xr-x 1 root root 2401 Apr 27  2018 avahi-daemon
-rwxr-xr-x 1 root root 2948 Jul 29  2018 bluetooth
-rwxr-xr-x 1 root root 1232 Aug 15  2019 console-setup.sh
-rwxr-xr-x 1 root root 3059 Jun 23  2019 cron
-rwxr-xr-x 1 root root 2813 Jun  9  2019 dbus
-rwxr-xr-x 1 root root 1901 Sep 14  2015 dhcpcd
-rwxr-xr-x 1 root root 2198 Oct 24  2016 dphys-swapfile
-rwxr-xr-x 1 root root  824 Sep  5  2014 fake-hwclock
-rwxr-xr-x 1 root root  734 Nov 28  2018 fio
-rwxr-xr-x 1 root root 3458 Nov 14  2019 grafana-server
-rwxr-xr-x 1 root root 3809 Jan 10  2019 hwclock.sh
-rwxr-xr-x 1 root root 1479 Oct 10  2016 keyboard-setup.sh
-rwxr-xr-x 1 root root 2044 Feb  9  2019 kmod
-rwxr-xr-x 1 root root 2610 Feb 22  2019 lightdm
-rwxr-xr-x 1 root root  883 May 17  2016 lm-sensors
-rwxr-xr-x 1 root root 3323 Nov 16  2019 mosquitto
-rwxr-xr-x 1 root root 4445 Aug 25  2018 networking
-rwxr-xr-x 1 root root 5658 Apr  6  2019 nfs-common
-rwxr-xr-x 1 root root 2786 Dec 18  2014 paxctld
-rwxr-xr-x 1 root root 1366 Apr  8  2019 plymouth
-rwxr-xr-x 1 root root  752 Apr  8  2019 plymouth-log
-rwxr-xr-x 1 root root  924 May 31  2018 procps
-rwxr-xr-x 1 root root 1210 Aug 21  2019 raspi-config
-rwxr-xr-x 1 root root 2020 Jun 29  2011 rng-tools
-rwxr-xr-x 1 root root 2480 Oct 14  2018 rpcbind
-rwxr-xr-x 1 root root 4417 Mar 15  2019 rsync
-rwxr-xr-x 1 root root 2864 Feb 26  2019 rsyslog
-rwxr-xr-x 1 root root 3939 Apr  8  2019 ssh
-rwxr-xr-x 1 root root 1030 Jan 12  2019 sudo
-rwxr-xr-x 1 root root 3217 Aug 30  2016 triggerhappy
-rwxr-xr-x 1 root root 6872 Sep 10  2019 udev
-rwxr-xr-x 1 root root 1391 Jun  8  2019 unattended-upgrades
-rwxr-xr-x 1 root root 2757 Nov 23  2016 x11-common
~~~
