import csv
import pathlib
import serial
import time

from datetime import datetime


if __name__ == "__main__":
    data_path = pathlib.Path(__file__).parent / "data"
    if not data_path.exists():
        data_path.mkdir()

    ports = ["COM5"]
    names = ["probe1"]

    arduinos = list()
    files = list()
    writers = list()

    for p, n in zip(ports, names):
        arduino = serial.Serial(port=p, baudrate=57600, timeout=.1)
        arduinos.append(arduino)
        
        filename_time = datetime.strftime(datetime.now(), "%Y%m%d-%H%M")
        filename = data_path / f"{filename_time}_{n}.csv"
        
        f = open(filename, "w", newline="")

        files.append(f)
        writers.append(csv.writer(f))

        arduino.flush()
        arduino.readline()

    try:
        while True:
            for arduino, csv_writer in zip(arduinos, writers):
                line = arduino.readline()
                print(line)
                line = line.decode()
                lst = [time.time()] + [int(b) for b in line.split(",")]
                csv_writer.writerow(lst)

    except KeyboardInterrupt:
        for f in files:
            f.close()
