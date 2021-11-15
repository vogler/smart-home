# tracks 'Under-voltage detected!' -> no more a problem with official power supply
log=under-voltage.log
dmesg -T | grep oltage | tee -a $log # append reports since boot to log
awk '!seen[$0]++' $log > tmp && mv tmp $log # remove duplicate lines: https://unix.stackexchange.com/questions/30173/how-to-remove-duplicate-lines-inside-a-text-file, awk has no -i: https://stackoverflow.com/questions/16529716/save-modifications-in-place-with-awk

# $ cat under-voltage.log
# [Sat Sep 12 18:52:25 2020] Voltage normalised (0x00000000)
# [Sat Sep 12 18:52:27 2020] Under-voltage detected! (0x00050005)
# ...
# [Thu Sep 17 18:29:38 2020] Voltage normalised (0x00000000)
# [Thu Sep 17 18:29:40 2020] Under-voltage detected! (0x00050005)

# $ ag detected under-voltage.log | wc -l
# 1049

# 17.09.2020 19:20 shutdown and replaced 3 port 18W QC power supply from AliExpress (https://trade.aliexpress.com/order_detail.htm?orderId=100211600442588, https://lygte-info.dk/review/USBpower%20MLLSE%20Universal%2018W%20Quick%20Charger%20AR-QC-03%20UK.html) with official Raspberry Pi 5.1V 3A 1.5m 18AWG power supply (arrived today) ordered yesterday on Amazon for 7.78€ (https://www.amazon.de/gp/css/summary/edit.html/?orderID=028-8213604-7907512)
# -> No more complaints :)
