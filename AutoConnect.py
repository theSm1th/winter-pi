from subprocess import check_output
from os import system

from time import sleep

BT_ID = "60:F4:45:XX:XX:XX"

while True:
    data = check_output(["sudo", "bluetoothctl", "info", BT_ID])
    for line in data.splitlines():
        nLine = line.strip()
        if nLine.startswith("Connected:"):
            if nLine[11:] == "yes":
                connected = True
            elif nLine[11:] == "no":
                connected = False
            else:
                with open("log.log", "w") as fileIO:
                    fileIO.writeline("AUTO CONNECT: Anomaly detected - expected yes or no but got {}.".format(nLine[11:]))
            break
    if connected == False:
        system("sudo bluetoothctl connect {}".format(BT_ID))
        with open("log.log", "w") as fileIO:
            fileIO.writelines("Attempting to connect to device... ")
    sleep(1)
