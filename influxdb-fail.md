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
rpi $ sudo mv /var/lib/influxdb influxdb-rpi
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

Chronograf said that InfluxDB was down on 2019-11-22 when I checked at 9:34. Did the copy-to-MBP-and-back procedure above and was running again at 10:40. Noticed afterwards that last data in DB before is from 2019-11-18 1:40, i.e., lost data from Mo-Fr despite Chronograf displaying data normally during that time.

---

#### 2022-01-13
Was running fine without errors for a long time after changing to 64 bit kernel (`arm_64bit=1` in `/boot/config.txt`).
Only now noticed constant >50% CPU load due to InfluxDB failing the compaction again. But this time it kept running instead of crashing.
Used date picker in Chronograf and found that CPU usage was already 30% after 2021-10-17 and then constantly >50% after 2021-10-30.
Didn't change anything in that time, just did some 3D printing -> maybe too many metrics via MQTT from new OctoPrint plugin?

~~~console
mac $ influxd version
InfluxDB 2.1.1 (git: 657e1839de) build_date: 2021-11-08T18:37:04Z
rpi $ influxd version
InfluxDB v1.8.10 (git: 1.8 688e697c51fd)

# rpi:
$ sudo journalctl -u influxdb.service > infldb
$ grep 'cannot allocate memory' infldb | wc -l
124056
$ grep -o 'db_shard_id=.*"cannot allocate memory"' infldb | sort | uniq
db_shard_id=957 error="cannot allocate memory"
db_shard_id=963 error="cannot allocate memory"
db_shard_id=964 error="cannot allocate memory"
db_shard_id=966 error="cannot allocate memory"
db_shard_id=967 error="cannot allocate memory"
db_shard_id=968 error="cannot allocate memory"
db_shard_id=969 error="cannot allocate memory"

$ sudo du -h -d1 /var/lib/influxdb
8.2M    /var/lib/influxdb/wal
16K     /var/lib/influxdb/meta
5.5G    /var/lib/influxdb/data
5.5G    /var/lib/influxdb
~~~

`/etc/influxdb/influxdb.conf`:
Tried `max-concurrent-compactions = 1` # avoid running multiple compactions at once ([comment](https://github.com/influxdata/influxdb/pull/12362#issuecomment-824086930)) but did not help.
Tried to disable in-memory by switching the sharding method to `index-version = "tsi1"` ([comment](https://github.com/influxdata/influxdb/issues/11339#issuecomment-757575790)), but did also not help - old shards still seem to use the in-memory setting...
Did the whole dance of letting it do the compaction on the old MBP:
~~~console
rpi $ sudo systemctl stop chronograf telegraf influxdb
mac $ ./rpi-sync.sh rpi4 var/lib/influxdb`
mac $ brew services stop influxdb@1
# rest see above
~~~
Afterwards no failing compaction and low CPU usage again.
Kept `max-concurrent-compactions = 1` and `index-version = "tsi1"` to hopefully avoid it in the future.
