from datetime import datetime

_today = datetime.today()

# Stores previous used formats to improve detection loop
ts_sel_formats = []

# new validator coded with only build-in functions
# six variants of date processing
# for 2+ versionss
def validate_timestamp(_word, obfuscate = True):
    # Here you can add more datetime formats following your requirements
    ts_formats = [
                  "%b %d %Y %H:%M:%S",
                  "%b %d %H:%M:%S %Y",
                  "%Y-%m-%dT%H:%M:%S%z",
                  "%Y-%m-%dT%H:%M:%S.%fZ",
                  "%Y-%m-%d %H:%M:%S%z",
                  "%Y-%m-%d %H:%M:%S.%f",
                  "%Y-%m-%d %H:%M:%S.%f%z",
                  "%m-%d-%y %H:%M:%S",
                  "%m/%d/%y %H:%M:%S",
                  "%d/%b/%Y:%H:%M:%S",
                  "%d/%b/%Y %H:%M:%S",
                  "%d-%b-%Y %H:%M:%S",
                  "%d-%b-%Y %H:%M:%S.%f",
                  "%d %b %Y %H:%M:%S",
                  "%Y-%m-%dT%H:%M:%SZ",
                  "%Y-%m-%d",
                  "%Y/%m/%d",
                  "%y-%m-%d",
                  "%y/%m/%d"
                  ]

    for ts in ts_sel_formats + ts_formats:
        try:
            datetime.strptime(_word, ts)
            if ts not in ts_sel_formats:
                ts_sel_formats.append(ts)
            if obfuscate:
                return True, _word #_today.strftime(ts)
            else:
                return True, _word
        except ValueError:
            pass

    return False, _word