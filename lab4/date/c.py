#3.Drop microseconds from datetime:
from datetime import datetime

# Current date and time
current_datetime = datetime.now()

# Dropping microseconds
datetime_no_microseconds = current_datetime.replace(microsecond=0)

print("Current DateTime with microseconds:", current_datetime)
print("DateTime without microseconds:", datetime_no_microseconds)
