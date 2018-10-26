#!/usr/bin/env python3
#colander function
def colander(grains_of_rice):
    from steamer import steamer
    kilos = 0
    tons = 0
    coal_reserves =0
    cubics = 0
    hoovers = 0
    empires = 0
    titanics = 0
    if grains_of_rice >= 50000:
        kilos = (grains_of_rice) / 50000
        kilos_out = ("That's " + str(kilos) + " kilograms of rice.")
        steamer(kilos_out)
    if kilos >= 1000:
        tons = kilos / 1000
        tons_out = (" - " + str(tons) + " tons of rice.")
        steamer(tons_out)
    if tons >= 1730000000:
        coal_reserves = tons / 1730000000
        coal_out = (" - " + str(coal_reserves) + " times the Chinese coal reserve.")
        steamer(coal_out)
    if tons >= 1000000000:
        cubics = tons / 1000000000
        cub_out = (" - " + str(cubics) + " cubic kilometres of starchy goodness.")
        steamer(cub_out)
    if tons >= 6600000:
        hoovers = tons / 6600000
        hoovers_out = (" - " + str(hoovers) + " Metric Hooverdamsworths.")
        steamer(hoovers_out)
    if tons >= 365000:
        empires = tons / 365000
        empires_out = (" - " + str(empires) + " Empire State buildings.")
        steamer(empires_out)
    if tons >= 52000:
        titanics = tons / 52000
        titanics_out = (" - " + str(titanics) + " RMS Rice-tanics.")
        steamer(titanics_out)