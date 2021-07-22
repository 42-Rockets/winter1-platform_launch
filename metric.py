import requests
import rainbowhat as microcontroller
import time

from datetime import datetime

def send_statistics(stats):
  r = requests.post('http://192.168.68.106:8080/v1/telemetry/winter1', data=stats)
  print(r.text)
  return r

while True:
  now = datetime.now()
  date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
  t = microcontroller.weather.temperature()
  microcontroller.display.clear()
  microcontroller.display.print_float(t)
  send_statistics({
    "timestamp":  datetime.timestamp(now),
    "value": str(t),
    "key": "temperature",
    "commponent": "launchPad"
  })
  print("date=", date_time, "temperature=", t)
  microcontroller.display.show()
  time.sleep(0.5)


