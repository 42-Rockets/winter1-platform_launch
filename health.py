import rainbowhat as microcontroller

def check_list():
  print('invoking checklist ...')
  
def current_temp(display=False):
  t = microcontroller.weather.temperature()
  if(display):
    microcontroller.display.clear()
    microcontroller.display.print_float(t)
    microcontroller.display.show()
  return t