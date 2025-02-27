# Checkpoint 1
instrument_catalog = {
    'Marimba': 1999,
    'Kora': 499,
    'Flute': 899
}

def print_instrument_price(instrument):
    # Checkpoint 2
    if instrument in instrument_catalog:
      print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    # Checkpoint 3
    else:
      raise KeyError(instrument + ' is not found in instrument catalog!')

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')
