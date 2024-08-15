import calendar
from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime, TehranTimezone
calendar.setfirstweekday(5)
class Calendar:
    def __init__(self):
        raise NotImplementedError
    
    def change_time(tarikh_shamsi: str) -> date:
        year, month, day = tarikh_shamsi.split("/")
        changed_time = JalaliDate(year, month, day).todate()
        return changed_time