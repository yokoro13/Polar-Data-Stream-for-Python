import asyncio
from bleak import BleakClient
import time
import numpy as np
from polar_utils import decode_ppg, convert_complement_from_bytearray, calc_samples_by_deltas
import csv

######## Change here ##########
address = "a0:9e:1a:a8:a5:99"
path = "ppg_output.csv"
TIME = 60.0
###############################


PMD_CONTROL = "FB005C81-02E7-F387-1CAD-8ACD2D8DF0C8"
PMD_DATA = "FB005C82-02E7-F387-1CAD-8ACD2D8DF0C8"

PPG_WRITE = bytearray([0x02, 0x01, 0x00, 0x01, 0x87, 0x00, 0x01, 0x01, 0x16, 0x00, 0x04, 0x01, 0x04])
PPG_SETTING = bytearray([0x01, 0x01])  # type PPG

global ppg0_samples
global ppg1_samples
global ppg2_samples
global ambient0_samples

global times
global time_start


def notification_handler(sender, data: bytearray):
    global ppg0_samples
    global ppg1_samples
    global ppg2_samples
    global ambient0_samples
    global times
    global time_start

    if len(times) == 0:
        time_start = time.perf_counter()
        times = [time_start]

    ppg0_sample0 = convert_complement_from_bytearray(data[10:13])
    ppg1_sample0 = convert_complement_from_bytearray(data[13:16])
    ppg2_sample0 = convert_complement_from_bytearray(data[16:19])
    ambient0_sample0 = convert_complement_from_bytearray(data[19:22])

    ppg0_deltas, ppg1_deltas, ppg2_deltas, ambient0_deltas = decode_ppg(data[24:len(data)],
                                                                        int.from_bytes(data[22:23], "little"))

    ppg0_calc_samples = calc_samples_by_deltas(ppg0_sample0, ppg0_deltas)
    ppg1_calc_samples = calc_samples_by_deltas(ppg1_sample0, ppg1_deltas)
    ppg2_calc_samples = calc_samples_by_deltas(ppg2_sample0, ppg2_deltas)
    ambient0_calc_samples = calc_samples_by_deltas(ambient0_sample0, ambient0_deltas)

    ppg0_samples += ppg0_calc_samples
    ppg1_samples += ppg1_calc_samples
    ppg2_samples += ppg2_calc_samples
    ambient0_samples += ambient0_calc_samples

    now = time.perf_counter()
    times += np.linspace(times[-1], now, len(ppg0_calc_samples)).tolist()


async def main(address):
    global ppg0_samples
    global ppg1_samples
    global ppg2_samples
    global ambient0_samples
    global times

    ppg0_samples = []
    ppg1_samples = []
    ppg2_samples = []
    ambient0_samples = []
    times = []

    async with BleakClient(address) as client:
        await client.write_gatt_char(PMD_CONTROL, PPG_SETTING, response=True)
        await client.write_gatt_char(PMD_CONTROL, PPG_WRITE, response=True)

        await client.start_notify(PMD_DATA, notification_handler)
        await asyncio.sleep(TIME)
        await client.stop_notify(PMD_DATA)


asyncio.run(main(address))

with open(path, mode='w', newline="") as f:
    writer = csv.writer(f)
    r = ["time", "ppg0", "ppg1", "ppg2", "ambient0"]
    writer.writerow(r)
    for i in range(2, len(ppg0_samples)):
        r = [times[i], ppg0_samples[i], ppg1_samples[i], ppg2_samples[i], ambient0_samples[i]]
        writer.writerow(r)
