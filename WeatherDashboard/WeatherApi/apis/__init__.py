
def convert_kelvintocelcius(kelvin):
    return str(round(float(kelvin) - 273.15, 2))


def convertsecondstoutc(timezone):
    convertime = float(float(timezone)/3600)
    hour = int(convertime)
    minute = (convertime * 60) % 60
    return f"UTC + {hour:02d}:{int(minute):02d}"
