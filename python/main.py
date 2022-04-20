import csv
import pathlib
import serial
import time

from datetime import datetime


if __name__ == "__main__":
    data_path = pathlib.Path(__file__).parent / "data"
    if not data_path.exists():
        data_path.mkdir()

    ports = ["COM6"]

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

    try:
        while True:
            for arduino, data_list in zip(arduinos, data_lists):
                line = arduino.readline()
                # print(line)

                try:
                    line = line.decode()
                    lst = [time.time()] + [int(b) for b in line.split(",")]

                except ValueError:
                    print("blah")

                else:
                    data_list.append(lst)

    except KeyboardInterrupt:
        for fl, data_list in zip(files, data_lists):
            with open(fl, "w", newline="") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(data_list)
