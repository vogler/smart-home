#!/bin/sh
# use sh! printing \n is different between shells: bash requires $''; echo -e does not work with zsh

cec() {
  echo "$1" | cec-client RPI -d 1 $2
}

i=0

case $1 in
  on)  cec "on $i" "-s";;
  off) cec "standby $i" "-s";;
  pc)  cec "pa 10 00\nas\nq\n";; # this sets hdmi 1 as the active source
  tv)  cec "pa 10 00\nas\nis\nq\n";; # this sets hdmi 1 as inactive, which makes the tv switch back to the last active source (which should be live tv)
  st*) cec "pow $i" "-s" | grep status;;
  *)   echo "commands: on, off, pc, tv, st[atus]";;
esac
