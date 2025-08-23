from abc import ABC, abstractmethod
from uuid import uuid4
from storage.storage import Storage
class Employe(ABC):
    def __init__(self,name,role,id =None):
        self.id = str(uuid4()) if id is None else id
        self.name = name
        self.role = role

    @abstractmethod
    def calculate_monthly_salay(self):
        pass

    
            


    