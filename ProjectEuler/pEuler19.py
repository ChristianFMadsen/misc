months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
          'September': 30, 'October': 31, 'November': 30, 'December': 31}

year = 1901
iterator = 2  # Jan 1 1901 = Tuesday
sundaysOnFirstOfMonth = 0

while year < 2001:
    for month, days in months.items():
        if month == 'February' and year % 4 == 0:
            days = 29

        for i in range(days):
            if i == 0 and iterator % 7 == 0:
                sundaysOnFirstOfMonth += 1
            iterator += 1

    year += 1

print(f'How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? '
      f'{sundaysOnFirstOfMonth}')
