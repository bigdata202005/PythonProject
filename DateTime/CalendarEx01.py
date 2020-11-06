import calendar

# 1년 달력 인쇄
calendar.prcal(2020)
print("-" * 80)

# 월 달력 인쇄
calendar.prmonth(2020,9)
print("-" * 80)

# 처음의 위치를 일요일로 만든다.
calendar.TextCalendar(calendar.SUNDAY).prmonth(2020, 9)
print("-" * 80)
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2020, 9)
print("-" * 80)

# HTML달력
c = calendar.HTMLCalendar(calendar.SUNDAY)
print(c.formatmonth(2020, 9))
