# rsync directories from rpi

# notes on preserving creation time:
  # https://unix.stackexchange.com/questions/61586/how-to-tell-rsync-to-preserve-time-stamp-on-files-when-source-tree-has-a-mounted
  # -a implies -t for times, macOS rsync also has option -N/--crtimes to 'preserve create times (newnewss)' but that leads to an error of unknown option when rsyncing from rpi b/c its rsync doesn't have that option (despite being the same version)
  # with `rsync -a`, `stat dash.log` shows 'Change' (ctime of inode?) as time of copy, but also has a field 'Birth' which shows the original create time
  # https://unix.stackexchange.com/questions/2464/timestamp-modification-time-and-created-time-of-a-file

# --delete truly sync target instead of just adding files
# -a archive mode; equals -rlptgoD (no -H,-A,-X)
  # skip -H (--hard-links) because it's expensive, can use fdupes to hard-link duplicates, see https://news.ycombinator.com/item?id=8305545
  # skip -X (extended attributes, see https://en.wikipedia.org/wiki/Chattr#Attributes)
# -v verbose
# -h output numbers in a human-readable format
# -z compress file data during transfer
# -P --partial (keep partially transferred files) --progress (show progress)
# --stats file-transfer stats
# --rsync-path need sudo for some directories and don't want to login as root

host=${1-"rpi3"}
dir=${2-"home/pi"}
target=$host/$dir/
mkdir -p $target
rsync --delete -avhzP --stats --rsync-path="sudo rsync" pi@$host:/$dir/ $target
