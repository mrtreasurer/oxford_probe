import csv
import pathlib
import serial
import time

from datetime import datetime


if __name__ == "__main__":
    data_path = pathlib.Path(__file__).parent / "data"
    if not data_path.exists():
        data_path.mkdir()

    ports = ["COM7"]

    arduinos = list()
    files = list()
    data_lists = list()

    for p in ports:
        arduino = serial.Serial(port=p, baudrate=57600, timeout=1)
        arduinos.append(arduino)

        data_lists.append(list())
        
        filename_time = datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")
        filename = data_path / f"{filename_time}_{p}.csv"
        
        files.append(filename)

        arduino.flush()
        arduino.readline()

    t0 = time.time()
    t_run = 60
    t_end = t0 + t_run
    
    try:
        while time.time() < t_end:
            for arduino, data_list in zip(arduinos, data_lists):
                line = arduino.readline()
                # print(line)

                try:
                    line = line.decode().strip()
                    lst = [int(b.split(":")[1]) for b in line.split("\t")]
                    # lst = [time.time()] + lst
                    lst = lst[-1:] + lst[:-1]

                except ValueError:
                    print(line)
                    raise

                else:
                    data_list.append(lst)

    except KeyboardInterrupt:
        pass

    for fl, data_list in zip(files, data_lists):
        with open(fl, "w", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(data_list)
