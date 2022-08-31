# FLiP-Py-Energy
HS110 Energy Monitoring


### Delete a topic (shell script)

````
echo "Delete topic $1"
bin/pulsar-admin schemas delete "$1"
bin/pulsar-admin topics delete "$1" --force
bin/pulsar-admin topics unload "$1"

bin/pulsar-admin schemas delete "$1-partition-0"
bin/pulsar-admin topics delete "$1-partition-0" --force
bin/pulsar-admin topics unload "$1-partition-0"
````

### Fields are dynamic depending on day of week, month, year

````
bin/pulsar-client consume "persistent://public/default/electric" -s electricavenue -n 0

----- got message -----
key:[20220831200138-4e54b5e0-7e49-49dc-be5e-8737dd6cd200], properties:[], content:{
 "current": 0.213546,
 "voltage": 119.661298,
 "power": 12.84688,
 "total": 12.782,
 "sw_ver": "1.2.5 Build 171206 Rel.085954",
 "hw_ver": "1.0",
 "type": "IOT.SMARTPLUGSWITCH",
 "model": "HS110(US)",
 "mac": "50:C7:BF:B1:95:D5",
 "deviceId": "8006ECB1D454C4428953CB2B34D9292D18A6DB0E",
 "hwId": "60FF6B258734EA6880E186F8C96DDC61",
 "fwId": "00000000000000000000000000000000",
 "oemId": "FFF22CFF774A0B89F7624BFC6F50D5DE",
 "alias": "Fan",
 "dev_name": "Wi-Fi Smart Plug With Energy Monitoring",
 "icon_hash": "",
 "relay_state": 1,
 "on_time": 7834591,
 "active_mode": "schedule",
 "feature": "TIM:ENE",
 "updating": 0,
 "rssi": -73,
 "led_off": 0,
 "latitude": 40.268272,
 "longitude": -74.529139,
 "day1": 0.374,
 "day2": 0.343,
 "day3": 0.153,
 "day4": 0.288,
 "day5": 0.193,
 "day6": 0.0,
 "day7": 0.0,
 "day8": 0.0,
 "day9": 0.0,
 "day10": 0.0,
 "day11": 0.0,
 "day12": 0.0,
 "day13": 0.014,
 "day14": 0.049,
 "day15": 0.049,
 "day16": 0.036,
 "day17": 0.0,
 "day18": 0.0,
 "day19": 0.0,
 "day20": 0.0,
 "day21": 0.017,
 "day22": 0.161,
 "day23": 0.245,
 "day24": 0.27,
 "day25": 0.289,
 "day26": 0.276,
 "day27": 0.241,
 "day28": 0.242,
 "day29": 0.232,
 "day30": 0.138,
 "day31": 0.212,
 "index": 18,
 "zone_str": "(UTC-05:00) Eastern Daylight Time (US & Canada)",
 "tz_str": "EST5EDT,M3.2.0,M11.1.0",
 "dst_offset": 60,
 "month1": 4.865,
 "month2": 6.115,
 "month3": 7.881,
 "month4": 3.126,
 "month5": 2.614,
 "month6": 3.72,
 "month7": 5.268,
 "month8": 3.822,
 "month9": 0.0,
 "month10": 0.0,
 "month11": 0.0,
 "month12": 0.0,
 "host": "192.168.1.95",
 "current_consumption": 12.84688,
 "devicetime": "08/31/2022 16:01:38",
 "ledon": true,
 "end": "1661976098.554444",
 "te": "0.25650906562805176",
 "systemtime": "08/31/2022 16:01:38",
 "cpu": 8.2,
 "memory": 63.9,
 "diskusage": "55978.0",
 "uuid": "20220831200138-4e54b5e0-7e49-49dc-be5e-8737dd6cd200",
 "macaddress": "bc:d0:74:54:88:ae"
}


````

# Schema 

````
class electric(Record):
    current = Float(default=0.0)
    voltage = Float(default=0.0)
    power = Float(default=0.0)
    total = Float(default=0.0)
    sw_ver = String()
    hw_ver = String()
    type = String()
    model = String()
    mac = String()
    deviceId = String()
    hwId = String()
    fwId = String()
    oemId = String()
    alias = String()
    dev_name = String()
    icon_hash = String()
    relay_state = Integer()
    on_time = Integer()
    active_mode = String()
    feature = String()
    updating = Integer()
    rssi = Integer()
    led_off = Integer()
    latitude = Float()
    longitude = Float()
    day1 = Float(default=0.0)
    day2 = Float(default=0.0)
    day3 = Float(default=0.0)
    day4 = Float(default=0.0)
    day5 = Float(default=0.0)
    day6 = Float(default=0.0)
    day7 = Float(default=0.0)
    day8 = Float(default=0.0)
    day9 = Float(default=0.0)
    day10 = Float(default=0.0)
    day11 = Float(default=0.0)
    day12 = Float(default=0.0)
    day13 = Float(default=0.0)
    day14 = Float(default=0.0)
    day15 = Float(default=0.0)
    day16 = Float(default=0.0)
    day17 = Float(default=0.0)
    day18 = Float(default=0.0)
    day19 = Float(default=0.0)
    day20 = Float(default=0.0)
    day21 = Float(default=0.0)
    day22 = Float(default=0.0)
    day23 = Float(default=0.0)
    day24 = Float(default=0.0)
    day25 = Float(default=0.0)
    day26 = Float(default=0.0)
    day27 = Float(default=0.0)
    day28 = Float(default=0.0)
    day29 = Float(default=0.0)
    day30 = Float(default=0.0)
    day31 = Float(default=0.0)
    index = Integer()
    zone_str = String()
    tz_str = String()
    dst_offset = Integer()
    month1 = Float(default=0.0)
    month2 = Float(default=0.0)
    month3 = Float(default=0.0)
    month4 = Float(default=0.0)
    month5 = Float(default=0.0)
    month6 = Float(default=0.0)
    month7 = Float(default=0.0)
    month8 = Float(default=0.0)
    month9 = Float(default=0.0)
    month10 = Float(default=0.0)
    month11 = Float(default=0.0)
    month12 = Float(default=0.0)
    host = String()
    current_consumption = Float(default=0.0)
    devicetime = String()
    ledon = Boolean()
    end = String()
    te = String()
    systemtime = String()
    cpu = Float(default=0.0)
    memory = Float(default=0.0)
    diskusage = String()
    uuid = String()
    macaddress = String()
````


# Reference

* https://github.com/tspannhw/pulsar-energy-function
* https://github.com/tspannhw/ApacheConAtHome2020/blob/main/schemas/energy.avsc
* https://github.com/tspannhw/FLiP-Energy
* https://github.com/tspannhw/FLiP-PulsarDevPython101
* https://github.com/tspannhw/flip-java-energy
* https://github.com/tspannhw/nifi-energy-monitoring
* https://github.com/tspannhw/nifi-smartplug
* https://dzone.com/articles/monitoring-energy-usage-utilizing-apache-nifi-pyth
* https://community.cloudera.com/t5/Community-Articles/Monitoring-Energy-Usage-Utilizing-Apache-NiFi-Python-Apache/ta-p/247525
