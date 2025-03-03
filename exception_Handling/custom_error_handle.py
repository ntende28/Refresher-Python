instrument_familes = {
  'Strings': ['Guitar', 'Banjo', 'Sitar'],
  'Percussion': ['Conga', 'Cymbal', 'Cajon'],
  'woodwinds': ['Flute', 'Oboe', 'Clarinet']
}

class InstrumentExistsError(Exception):
  def __init__(self, family):
    self.family = family

  def __str__(self):
    return 'The ' + str(self.family) + ' family of intruments does not exists!'

def print_instrument_families(instrument_family):
  # Normalize input to match dictionary keys (capitalize first letter only)
  instrument_family = instrument_family.capitalize()  

  if instrument_family in instrument_familes: 
    print(f"Some instruments in the {instrument_family} family are {', '.join(instrument_familes[instrument_family])}")
  else:
    raise InstrumentExistsError(instrument_family)

try:
    print_instrument_families('percussion')  # Incorrect input (should be 'Percussion')
except InstrumentExistsError as e:
    print(e)