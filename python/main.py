import csv
import pathlib
import serial
import time

from datetime import datetime


if __name__ == "__main__":
    arduino = serial.Serial(port='COM5', baudrate=57600, timeout=.1)

    filename_time = datetime.strftime(datetime.now(), "%Y%m%d-%H%M")
    name = "probe1"

    data_path = pathlib.Path(__file__).parent / "data"
    if not data_path.exists():
        data_path.mkdir()

    with open(f"data/{filename_time}_{name}.csv" , "w", newline="") as f:
        csv_writer = csv.writer(f)
        arduino.flush()
        arduino.readline()

        try:
            while True:
                line = arduino.readline().decode()
                lst = [time.time()] + [int(b) for b in line.split(",")]
                csv_writer.writerow(lst)

        except KeyboardInterrupt:
            pass
