### FLiP-Py-Energy

HS110 Energy Monitoring

![image](https://user-images.githubusercontent.com/18673814/187780919-b0e0299f-c77e-4bea-85e8-023adb1e671d.png)

### Updated Software - python-kasa library with asynchio

See energynew.py.   It is a new library with support for more devices.

* https://github.com/python-kasa/python-kasa
* https://python-kasa.readthedocs.io/en/latest/
* pip install python-kasa


### Hardware

* HS-110 TP-Link Monitoring Device
* Power Mac M1 16GB RAM
* Python 3.10

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/hs110energymeter.jpg" width="200">


### Device Output Shown in iPhone Application


<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/energyscreen1.png" width="400">

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/energydeviceinfo.png" width="400">

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/energyruntime.png" width="400">

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/energyusage.png" width="400">

### Run the code

````

python3 energy.py -t persistent://public/default/electric -su pulsar://pulsar1:6650

````

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

#### Results of Consuming Data

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/consumeresults.png" width="600">


### Schema 

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

### To Retrieve Schema (see https://github.com/tspannhw/FLiP-Py-Energy/blob/main/electric.schema)

````
bin/pulsar-admin schemas get persistent://public/default/electric

````


### Flink SQL

````

CREATE CATALOG pulsar WITH (
   'type' = 'pulsar',
   'service-url' = 'pulsar://pulsar1:6650',
   'admin-url' = 'http://pulsar1:8080',
   'format' = 'json'
);

USE CATALOG pulsar;

SHOW TABLES;

Flink SQL> describe electric;
+---------------------+---------+------+-----+--------+-----------+
|                name |    type | null | key | extras | watermark |
+---------------------+---------+------+-----+--------+-----------+
|             current |   FLOAT | true |     |        |           |
|             voltage |   FLOAT | true |     |        |           |
|               power |   FLOAT | true |     |        |           |
|               total |   FLOAT | true |     |        |           |
|              sw_ver |  STRING | true |     |        |           |
|              hw_ver |  STRING | true |     |        |           |
|                type |  STRING | true |     |        |           |
|               model |  STRING | true |     |        |           |
|                 mac |  STRING | true |     |        |           |
|            deviceId |  STRING | true |     |        |           |
|                hwId |  STRING | true |     |        |           |
|                fwId |  STRING | true |     |        |           |
|               oemId |  STRING | true |     |        |           |
|               alias |  STRING | true |     |        |           |
|            dev_name |  STRING | true |     |        |           |
|           icon_hash |  STRING | true |     |        |           |
|         relay_state |     INT | true |     |        |           |
|             on_time |     INT | true |     |        |           |
|         active_mode |  STRING | true |     |        |           |
|             feature |  STRING | true |     |        |           |
|            updating |     INT | true |     |        |           |
|                rssi |     INT | true |     |        |           |
|             led_off |     INT | true |     |        |           |
|            latitude |   FLOAT | true |     |        |           |
|           longitude |   FLOAT | true |     |        |           |
|                day1 |   FLOAT | true |     |        |           |
|                day2 |   FLOAT | true |     |        |           |
|                day3 |   FLOAT | true |     |        |           |
|                day4 |   FLOAT | true |     |        |           |
|                day5 |   FLOAT | true |     |        |           |
|                day6 |   FLOAT | true |     |        |           |
|                day7 |   FLOAT | true |     |        |           |
|                day8 |   FLOAT | true |     |        |           |
|                day9 |   FLOAT | true |     |        |           |
|               day10 |   FLOAT | true |     |        |           |
|               day11 |   FLOAT | true |     |        |           |
|               day12 |   FLOAT | true |     |        |           |
|               day13 |   FLOAT | true |     |        |           |
|               day14 |   FLOAT | true |     |        |           |
|               day15 |   FLOAT | true |     |        |           |
|               day16 |   FLOAT | true |     |        |           |
|               day17 |   FLOAT | true |     |        |           |
|               day18 |   FLOAT | true |     |        |           |
|               day19 |   FLOAT | true |     |        |           |
|               day20 |   FLOAT | true |     |        |           |
|               day21 |   FLOAT | true |     |        |           |
|               day22 |   FLOAT | true |     |        |           |
|               day23 |   FLOAT | true |     |        |           |
|               day24 |   FLOAT | true |     |        |           |
|               day25 |   FLOAT | true |     |        |           |
|               day26 |   FLOAT | true |     |        |           |
|               day27 |   FLOAT | true |     |        |           |
|               day28 |   FLOAT | true |     |        |           |
|               day29 |   FLOAT | true |     |        |           |
|               day30 |   FLOAT | true |     |        |           |
|               day31 |   FLOAT | true |     |        |           |
|               index |     INT | true |     |        |           |
|            zone_str |  STRING | true |     |        |           |
|              tz_str |  STRING | true |     |        |           |
|          dst_offset |     INT | true |     |        |           |
|              month1 |   FLOAT | true |     |        |           |
|              month2 |   FLOAT | true |     |        |           |
|              month3 |   FLOAT | true |     |        |           |
|              month4 |   FLOAT | true |     |        |           |
|              month5 |   FLOAT | true |     |        |           |
|              month6 |   FLOAT | true |     |        |           |
|              month7 |   FLOAT | true |     |        |           |
|              month8 |   FLOAT | true |     |        |           |
|              month9 |   FLOAT | true |     |        |           |
|             month10 |   FLOAT | true |     |        |           |
|             month11 |   FLOAT | true |     |        |           |
|             month12 |   FLOAT | true |     |        |           |
|                host |  STRING | true |     |        |           |
| current_consumption |   FLOAT | true |     |        |           |
|          devicetime |  STRING | true |     |        |           |
|               ledon | BOOLEAN | true |     |        |           |
|                 end |  STRING | true |     |        |           |
|                  te |  STRING | true |     |        |           |
|          systemtime |  STRING | true |     |        |           |
|                 cpu |   FLOAT | true |     |        |           |
|              memory |   FLOAT | true |     |        |           |
|           diskusage |  STRING | true |     |        |           |
|                uuid |  STRING | true |     |        |           |
|          macaddress |  STRING | true |     |        |           |
+---------------------+---------+------+-----+--------+-----------+
84 rows in set

select `current` as Current, 
       voltage as Voltage,
       `power` as Power,
       current_consumption,
       `total` as Total,
       day31,
       month8,
       devicetime,
       model,
       systemtime
from electric;

select avg(`current`) as AvgCurrent, 
       max(voltage) as MaxVoltage,
       max(`power`) as MaxPower,
       model
from electric
group by model;

````

#### Flink SQL Results Row Summary

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/rowsummary.png" width="600">

#### Flink SQL Results - Standard Select

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/currentAndPower.png" width="600">

#### Flink SQL Results - Max

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/flinkeletricmax.png" width="600">

#### Flink SQL Dashboard - Average Metrics

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/flinksqlavgmetrics.png" width="600">

#### Flink SQL Dashboard - Group by Details

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/flinksqlgroupbydetail.png" width="600">


### Displaying The Topic in Pulsar Manager

<img src="https://github.com/tspannhw/FLiP-Py-Energy/raw/main/pmelectric.png" width="600">

* https://github.com/apache/pulsar-manager

### Reference

* https://github.com/tspannhw/pulsar-energy-function
* https://github.com/tspannhw/ApacheConAtHome2020/blob/main/schemas/energy.avsc
* https://github.com/tspannhw/FLiP-Energy
* https://github.com/tspannhw/FLiP-PulsarDevPython101
* https://github.com/tspannhw/flip-java-energy
* https://github.com/tspannhw/nifi-energy-monitoring
* https://github.com/tspannhw/nifi-smartplug
* https://dzone.com/articles/monitoring-energy-usage-utilizing-apache-nifi-pyth
* https://community.cloudera.com/t5/Community-Articles/Monitoring-Energy-Usage-Utilizing-Apache-NiFi-Python-Apache/ta-p/247525

#### Simple Dashboard in JQuery, HTML and Websockets

<img src="https://github.com/tspannhw/FLiP-Py-Energy/blob/main/dashboard.png" width="800">

* https://github.com/tspannhw/FLiP-Py-Energy/blob/main/electric.html



#### Join me at Current Event October 2022

<img src="https://raw.githubusercontent.com/tspannhw/FLiP-Py-Energy/main/Spann_Kjerrumgaard_-_Lets_Monitor_The_Conditions_at_the_Conference_342405.jpeg" width="800">
