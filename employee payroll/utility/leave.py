from collections import defaultdict
import calendar
from datetime import date
from storage.storage import Storage


class Leave:
    def __init__(self):
        self.leave_record = defaultdict(lambda : defaultdict(lambda:{'unpaid':0}))

    def add_leave(self,id,year,month,days,leave_type='unpaid'):
        self.leave_record[id][(year,month)][leave_type] += days
        data = Storage.find_employee(id)
        if data is not None:
            if str((year,month)) in data['data']['taken_leave']:
                data['data']['taken_leave'][str((year,month))] += days
            else:
                data['data']['taken_leave'][str((year,month))] = days
            Storage.save_to_json(data['data'],data['index'])
    
    def get_unpaid_leaves(self,id,year,month):
        return self.leave_record[id][(year,month)]['unpaid'] or 0
    
    def total_working_days(self,year,month):
        # Get total days of the month 
        _,total_days = calendar.monthrange(year,month) # first 1 is day of firstday of the month and 2nd is total days
        working_days = 0
        # Now we need a loop to check wether it is between monday(0) to friday(4)
        for day in range(1,total_days+1):
            work_day = date(year,month,day).weekday()
            if work_day < 5:
                working_days += 1
        
        return working_days
