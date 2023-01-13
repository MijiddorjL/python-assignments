#1. Set a variable birthday = "1-May-12".
from datetime import datetime

birthday = "1-May-12"
date_format = "%d-%B-%y"

#2. Parse the date using datetime.datetime.strptime.
parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17

#3. Use strftime to output a date that looks like "5/1/2012".
print(date_str)