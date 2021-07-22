import time
import rainbowhat as microcontroller

def display_countdown():
  microcontroller.display.print_str('AHOY')
  microcontroller.display.show()
  time.sleep(1)
  for i in range(10):
    microcontroller.display.clear()
    microcontroller.display.print_str(10 - i)
    microcontroller.display.show()
    time.sleep(1)
    if(10 - i < 5):
      microcontroller.buzzer.midi_note(60, 1)
      microcontroller.display.print_str(10 - i)
      microcontroller.display.show()
      microcontroller.rainbow.clear()
      microcontroller.rainbow.set_pixel(i - 4, 255, 0, 0)
      time.sleep(1)
    if(i == 10):
      microcontroller.display.print_str('GO!')
      microcontroller.display.show()
      microcontroller.rainbow.show()
      microcontroller.rainbow.set_pixel(1, 0, 128, 0)
      microcontroller.rainbow.set_pixel(2, 0, 128, 0)
      microcontroller.rainbow.set_pixel(3, 0, 128, 0)
      microcontroller.rainbow.set_pixel(4, 0, 128, 0)
      microcontroller.rainbow.set_pixel(5, 0, 128, 0)
      microcontroller.rainbow.show()
      time.sleep(10)

display_countdown()
