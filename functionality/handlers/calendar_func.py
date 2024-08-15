import calendar
from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime, TehranTimezone
from typing import Tuple, Optional

class Calendar:
    def __init__(self):
        calendar.setfirstweekday(5)
    
    def __split_tarikh(tarikh: str) -> Tuple[int, int, int]:
        year, month, day = tarikh.split("/")
        return map(int, (year, month, day))
    
    def convert_calendar(self, tarikh_shamsi: str) -> date:
        year, month, day = self.__split_tarikh(tarikh_shamsi)
        converted_time = JalaliDate(year, month, day).todate()
        return converted_time
    
    def get_weekday(self, tarikh: str) -> int:
        year, month, day = self.__split_tarikh(tarikh)
        weekday = date(year, month, day).weekday()
        return weekday
    
    def set_event(self, event: str, weekday: date, start_date: Optional[date] = datetime.now(), end_date: Optional[date] = datetime.now(), event_time: Optional[date] = None):
        raise NotImplementedError
    
    def get_event(tarikh):
        raise NotImplementedError
    
    