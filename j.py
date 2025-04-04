from datetime import datetime, timedelta

today = datetime.now()
new_date = today + timedelta(days=5)

print(today.strftime("%Y-%m-%d"))
print(new_date.strftime("%Y-%m-%d"))