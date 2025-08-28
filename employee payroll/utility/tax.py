class Tax:
    def __init__(self):
        self.rules = {
            'FullTimeEmployee':.2,
            'Contract':.15,
            'Intern':.05
        }


    def calculate_tax (self,gross_salary,employee):
        tax_rate = self.rules.get(employee.__class__.__name__,.15) #This __class__.__name__ gives the name of the class
        return int(float(tax_rate) * float(gross_salary))