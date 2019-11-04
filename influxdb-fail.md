How to deal with InfluxDB compaction error cycle by copying to MBP (64 bit OS), let compaction finish there and copy back to RPi (see [issue](https://github.com/influxdata/influxdb/issues/11339#issuecomment-525500034)).

~~~sh
rpi $ sudo systemctl stop chronograf telegraf influxdb
mac $ ./rpi-sync.sh var/lib/influxdb
mac $ brew services stop influxdb
mac $ mv /usr/local/var/influxdb/ influxdb-mbp
mac $ mv rpi/var/lib/influxdb /usr/local/var
mac $ brew services run influxdb
mac $ # check /usr/local/var/log/influxdb.log
mac $ brew services stop influxdb
mac $ rsync --delete -avhzP --stats --rsync-path="sudo rsync" /usr/local/var/influxdb/ pi@rpi3.local:/var/lib/influxdb/
rpi $ sudo chown -R influxdb:influxdb /var/lib/influxdb
rpi $ sudo systemctl start chronograf telegraf influxdb
~~~

Paths:
- config:
  - rpi: `/etc/influxdb/influxdb.conf` -> `/home/pi/smart-home/etc/influxdb/influxdb.conf`
  - mac: `/usr/local/etc/influxdb.conf`


## Log

Usually it would just fail to compact but still work (and crash the RPi after a couple of days?).
After a crash on 2019-10-23 it stopped working and was just restarted in a loop by systemd because it failed to allocate memory after reading `wal/`.

Sizes/permissions:
~~~sh
rpi $ du -h -d1 /var/lib/influxdb
1.7G    /var/lib/influxdb/data
8.0K    /var/lib/influxdb/meta
174M    /var/lib/influxdb/wal
1.9G    /var/lib/influxdb
rpi $  ll /var/lib/influxdb
total 12K
drwxr-xr-x 5 influxdb influxdb 4.0K Apr  5  2019 data
drwxr-xr-x 2 influxdb influxdb 4.0K Oct 21 01:34 meta
drwx------ 5 influxdb influxdb 4.0K Apr  5  2019 wal
~~~

Running on MBP it didn't fail (see below), but somehow lost data of the last 3 days, despite Chronograf displaying everything correctly yesterday.
~~~
ts=2019-10-23T23:23:55.932407Z lvl=info msg="Reading file" log_id=0Ifjmivl000 engine=tsm1 service=cacheloader path=/usr/local/var/influxdb/wal/telegraf/autogen/77/_00001.wal size=10489226
…
ts=2019-10-23T23:24:11.092601Z lvl=info msg="Reading file" log_id=0Ifjmivl000 engine=tsm1 service=cacheloader path=/usr/local/var/influxdb/wal/telegraf/autogen/77/_16508.wal size=59141
…
ts=2019-10-23T23:24:12.263059Z lvl=info msg="TSM compaction (start)" log_id=0Ifjmivl000 engine=tsm1 tsm1_level=1 tsm1_strategy=level trace_id=0IfjnvOG001 op_name=tsm1_compact_group op_event=start
ts=2019-10-23T23:24:12.263117Z lvl=info msg="Beginning compaction" log_id=0Ifjmivl000 engine=tsm1 tsm1_level=1 tsm1_strategy=level trace_id=0IfjnvOG001 op_name=tsm1_compact_group tsm1_files_n=8
ts=2019-10-23T23:24:12.263150Z lvl=info msg="Compacting file" log_id=0Ifjmivl000 engine=tsm1 tsm1_level=1 tsm1_strategy=level trace_id=0IfjnvOG001 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/75/000000001-000000001.tsm
…
ts=2019-10-23T23:24:16.349267Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjnvOW000 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/74/000000014-000000002.tsm.tmp
…
ts=2019-10-23T23:24:16.729098Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjnvOW001 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/62/000000014-000000002.tsm.tmp
…
ts=2019-10-23T23:24:17.169981Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjnvOG000 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/72/000000014-000000002.tsm.tmp
…
ts=2019-10-23T23:24:17.537161Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_level=1 tsm1_strategy=level trace_id=0IfjnvOG001 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/75/000000012-000000002.tsm.tmp
…
ts=2019-10-23T23:24:20.781380Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjoDw0001 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/60/000000016-000000002.tsm.tmp
…
ts=2019-10-23T23:24:22.026223Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjoDw0000 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/76/000000013-000000002.tsm.tmp
…
ts=2019-10-23T23:24:22.837299Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjoHrG001 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/71/000000054-000000002.tsm.tmp
…
ts=2019-10-23T23:24:24.305335Z lvl=info msg="Compacted file" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjoHrG000 op_name=tsm1_compact_group tsm1_index=0 tsm1_file=/usr/local/var/influxdb/data/telegraf/autogen/73/000000016-000000002.tsm.tmp
ts=2019-10-23T23:24:24.305424Z lvl=info msg="Finished compacting files" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjoHrG000 op_name=tsm1_compact_group tsm1_files_n=1
ts=2019-10-23T23:24:24.305449Z lvl=info msg="TSM compaction (end)" log_id=0Ifjmivl000 engine=tsm1 tsm1_strategy=full tsm1_optimize=false trace_id=0IfjoHrG000 op_name=tsm1_compact_group op_event=end op_elapsed=6040.604ms
ts=2019-10-23T23:24:25.276000Z lvl=info msg="Snapshot for path written" log_id=0Ifjmivl000 engine=tsm1 trace_id=0IfjnvPG000 op_name=tsm1_cache_snapshot path=/usr/local/var/influxdb/data/telegraf/autogen/77 duration=13014.679ms
~~~
