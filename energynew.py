import json
import datetime
import os
import os.path
import socket
import time
import uuid
from time import gmtime, strftime
import psutil
import json
import argparse
import re
import sys
import pulsar
from pulsar.schema import *
from pulsar.schema import AvroSchema
from pulsar.schema import JsonSchema
from pulsar import Client, AuthenticationOauth2
import asyncio
import kasa
from kasa import Discover
from kasa import SmartPlug

### Schema Object
# https://pulsar.apache.org/docs/en/client-libraries-python/
# https://pulsar.apache.org/api/python/2.10.1/pulsar/schema/schema.html#Schema.schema_info

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

# Get MAC address of a local interfaces
def psutil_iface(iface):
    # type: (str) -> Optional[str]
    import psutil
    nics = psutil.net_if_addrs()
    if iface in nics:
        nic = nics[iface]
        for i in nic:
            if i.family == psutil.AF_LINK:
                return i.address

async def main(): 
    # running on Mac M2, Python 3.10
    #parse arguments
    parse = argparse.ArgumentParser(prog='energy.py')
    parse.add_argument('-su', '--service-url', dest='service_url', type=str, required=True,
                       help='The pulsar service you want to connect to')
    parse.add_argument('-t', '--topic', dest='topic', type=str, required=True,
                       help='The topic you want to produce to')
    parse.add_argument('--auth-params', dest='auth_params', type=str, default="",
                       help='The auth params which you need to configure the client')
    args = parse.parse_args()

    print("Pulsar Connection")
    print(args.service_url)
    print(args.topic)
    print(args.auth_params)

    # connect to pulsar
    if (len(args.auth_params) == 0 ):
       client = pulsar.Client(args.service_url)
    else:
       client = pulsar.Client(args.service_url, authentication=AuthenticationOauth2(args.auth_params))

    producer = client.create_producer(topic=args.topic,schema=JsonSchema(electric),properties={"producer-name": "energy-py-sensor","producer-id": "energy-sensor" })

    devices = await Discover.discover()

    for addr, dev in devices.items():
        await dev.update()
        print(f"{addr} >> {dev}")
        plugOne = addr

    plug = SmartPlug(plugOne)
    await plug.update()

    try:
        while True:
                now = datetime.datetime.now()
                row = {}
                year = now.year
                month = now.month
                start = time.time()
                sysinfo = await plug.get_sys_info()
                uuid2 = '{0}-{1}'.format(strftime("%Y%m%d%H%M%S", gmtime()), uuid.uuid4())

                electricRec = electric()

                emeterrealtime = await plug.get_emeter_realtime()

                for k, v in emeterrealtime.items():
                    electricRec.__setattr__("%s" % k, float(v))

                for k, v in sysinfo.items():
                    electricRec.__setattr__("%s" % k, v)

                emeterdaily = await plug.get_emeter_daily(year=year, month=month)
                for k, v in emeterdaily.items():
                    electricRec.__setattr__("day%s" % k, float(v))

                hwinfo = plug.hw_info

                for k, v in hwinfo.items():
                    electricRec.__setattr__("%s" % k, v)

                timezone = plug.timezone

                for k, v in timezone.items():
                    if k != 'err_code':
                        electricRec.__setattr__("%s" % k, v)

                emetermonthly = await plug.get_emeter_monthly(year=year)

                for k, v in emetermonthly.items():
                    electricRec.__setattr__("month%s" % k, float(v))

                electricRec.host = str(dev.host)
                electricRec.current_consumption = float(await plug.current_consumption())
                electricRec.alias = plug.alias
                electricRec.devicetime = plug.time.strftime('%m/%d/%Y %H:%M:%S')
                electricRec.ledon = plug.led
                end = time.time()
                electricRec.end = '{0}'.format(str(end))
                electricRec.te = '{0}'.format(str(end - start))
                electricRec.systemtime = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
                electricRec.cpu = psutil.cpu_percent(interval=1)
                electricRec.memory = psutil.virtual_memory().percent
                usage = psutil.disk_usage("/")
                electricRec.diskusage = "{:.1f}".format(float(usage.free) / 1024 / 1024)
                electricRec.uuid = str(uuid2)
                electricRec.macaddress = psutil_iface('en0')
                producer.send(electricRec,partition_key=str(uuid2))
                print(electricRec)

    except KeyboardInterrupt:
        pass

    client.close()

if __name__ == '__main__':
    asyncio.run(main())
