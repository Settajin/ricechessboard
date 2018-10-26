#!/usr/bin/env python3
# Work out the Numbers
from steamer import steamer
from colander import colander
rice_buffer = 0
rice_grains = 1
total_rice = 0
while rice_buffer == 0:
    steamer("Square 1: " + str(rice_grains) + " grain.")
    rice_buffer = int(rice_buffer) + 1
    total_rice = int(rice_grains) + 1
    colander(rice_grains)
while rice_buffer <= 63:
    rice_grains = int(rice_grains) + int(rice_grains)
    rice_buffer = int(rice_buffer) + 1
    steamer("Square " + str(rice_buffer) + ": " + str(rice_grains) + " grains.")
    total_rice = int(rice_grains) + int(total_rice)
    colander(rice_grains)
print("You have " + str(int(total_rice) - 1 ) + " grains of rice in total.")


#function within loop called printNumGrain - also function to add colours to
#start and end of printed lines
