import csv
import pathlib
import serial

from datetime import datetime


if __name__ == "__main__":
    arduino = serial.Serial(port='COM5', baudrate=57600, timeout=1)

    now = datetime.strftime(datetime.now(), "%Y%m%d-%H%M")
    name = "probe1"

    data_path = pathlib.Path(__file__).parent / "data"
    if not data_path.exists():
        data_path.mkdir()

    with open(f"data/{now}_{name}" , "w", newline="") as f:
        csv_writer = csv.writer(f)
        arduino.flush()
        arduino.readline()

        try:
            while True:
                line = arduino.readline().decode()
                lst = [int(b) for b in line.split(",")]
                csv_writer.writerow(lst)

        except KeyboardInterrupt:
            pass
