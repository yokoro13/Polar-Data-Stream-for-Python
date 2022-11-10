import asyncio
from bleak import BleakClient
import csv
import numpy as np
import time

######## Change here ##########
address = "a0:9e:1a:a8:a5:99"
path = "ppi_output.csv"
TIME = 60.0
###############################

PMD_CONTROL = "FB005C81-02E7-F387-1CAD-8ACD2D8DF0C8"
PMD_DATA = "FB005C82-02E7-F387-1CAD-8ACD2D8DF0C8"

PPI_WRITE = bytearray([0x02, 0x03])
PPI_SETTING = bytearray([0x01, 0x03])

global bpms
global peak_to_peak_mses
global errors

global times
global time_start


def notification_handler(sender, data: bytearray):
    global bpms
    global peak_to_peak_mses
    global errors
    global times
    global time_start

    measurement_type = data[0]
    timestamp = data[1:9]
    frame_type = data[9]

    ppi_data = []
    count = 0
    for d in range(len(data[10:]) // 6):
        slide = count * 6
        ppi_data.append(data[10 + slide:16 + slide + 1])
        count += 1

    if len(times) == 0:
        times = [0]

    for ppi in ppi_data:
        bpm = ppi[0]
        peak_to_peak_ms = int.from_bytes(ppi[1:3], "little")
        error = int.from_bytes(ppi[3:5], "little")
        flags = ppi[5]

        print("bpm: {}".format(bpm), "peak_to_peak_ms: {}".format(peak_to_peak_ms), "error: {}".format(error),
              "flags: {}".format(flags))

        times.append(times[-1] + peak_to_peak_ms)
        bpms.append(bpm)
        peak_to_peak_mses.append(peak_to_peak_ms)
        errors.append(error)


async def main(address):
    global bpms
    global peak_to_peak_mses
    global errors
    global times

    bpms = []
    peak_to_peak_mses = []
    errors = []
    times = []

    async with BleakClient(address) as client:
        await client.write_gatt_char(PMD_CONTROL, PPI_SETTING, response=True)
        await client.write_gatt_char(PMD_CONTROL, PPI_WRITE, response=True)

        await client.start_notify(PMD_DATA, notification_handler)
        await asyncio.sleep(TIME)
        await client.stop_notify(PMD_DATA)


asyncio.run(main(address))

with open(path, mode='w', newline="") as f:
    writer = csv.writer(f)
    r = ["time", "bpm", "peak_to_peak_ms", "error"]
    writer.writerow(r)
    for i in range(len(bpms)):
        r = [times[i], bpms[i], peak_to_peak_mses[i], errors[i]]
        writer.writerow(r)

print(sum(peak_to_peak_mses))