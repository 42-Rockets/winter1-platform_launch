try:
  import health
except ImportError:
  raise ImportError("Imports dont work, pleach check and try again!")
  
def checklist():
  print('Start checklist ...')
  health.current_temp()
  

checklist()
