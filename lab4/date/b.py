#2.Print yesterday, today, and tomorrow:
from datetime import datetime, timedelta

# Current date (today)
today = datetime.now()

# Yesterday
yesterday = today - timedelta(days=1)

# Tomorrow
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
