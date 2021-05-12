
def convert_kelvintocelcius(kelvin):
    return str(float(kelvin) - 273.15)


def convertsecondstoutc(timezone):
    return "UTC+" + str(float(timezone)/3600)
