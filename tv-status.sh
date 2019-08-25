old_status="?"
while true
do
  status=$(./cec.sh status | sed 's/power status: //')
  if [ "$status" != "$old_status" ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S')\tTV changed from $old_status to $status"
    old_status=$status
  # else
  #   echo "Nothing changed"
  fi
  sleep 5
done
