from datetime import datetime
import zoneinfo
zone = zoneinfo.ZoneInfo("Europe/Moscow")

offset = datetime.now(zone).utcoffset().total_seconds()//(60*60)
print(offset) # 3 / 4 - This depends on daylight saving time
print(f"UTC+{int(offset)}") # UTC+3 / UTC+4
