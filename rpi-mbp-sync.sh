# run to sync home to MBP
# https://unix.stackexchange.com/questions/61586/how-to-tell-rsync-to-preserve-time-stamp-on-files-when-source-tree-has-a-mounted
# -a implies -t for times, macOS rsync also has option -N/--crtimes to 'preserve create times (newnewss)' but that leads to an error of unknown option when rsyncing from rpi b/c its rsync doesn't have that option (despite being the same version)
# -a archive mode; equals -rlptgoD (no -H,-A,-X)
# -v verbose
# -z compress file data during transfer
# -P --partial (keep partially transferred files) --progress (show progress)
# with -a `stat dash.log` shows 'Change' (ctime of inode?) as time of copy, but also has a field 'Birth' which shows the original create time
# https://unix.stackexchange.com/questions/2464/timestamp-modification-time-and-created-time-of-a-file
dir=${1-"home/pi"}
target=rpi/$dir/
mkdir -p $target
rsync -avzP pi@rpi3.local:/$dir/ $target
