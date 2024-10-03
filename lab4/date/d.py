#4.Calculate two date differences in seconds:
from datetime import datetime

# Define two dates
date1 = datetime(2024, 10, 1, 10, 0, 0)
date2 = datetime(2024, 9, 25, 8, 0, 0)

# Difference between the two dates
time_difference = date1 - date2

# Convert difference to seconds
difference_in_seconds = time_difference.total_seconds()

print("Difference in seconds:", difference_in_seconds)
