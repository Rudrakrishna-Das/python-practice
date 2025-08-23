from models.full_time_employe import FullTimeEmployee as FTE
from utility import bonus,leave,tax

b = bonus.Bonus()
l = leave.Leave()
t = tax.Tax()

utilities={
    "leave":l,
    "tax":t,
    'bonus':b
}

ram = FTE('Ram','Engineer',240000)
utilities['bonus'].set_bonus("d673a5f0-f90f-4970-a750-bcd46b80cd91",2025,8,10000)
utilities['bonus'].set_bonus("d673a5f0-f90f-4970-a750-bcd46b80cd91",2025,8,10000)
utilities['leave'].add_leave("d673a5f0-f90f-4970-a750-bcd46b80cd91",2025,8,2)

utilities['bonus'].set_bonus("d673a5f0-f90f-4970-a750-bcd46b80cd91",2025,9,20000)
utilities['leave'].add_leave("d673a5f0-f90f-4970-a750-bcd46b80cd91",2025,9,5)
 
print(ram.calculate_monthly_salay(8,2025,utilities))
print(ram.calculate_monthly_salay(9,2025,utilities))