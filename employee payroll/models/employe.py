from abc import ABC, abstractmethod
from uuid import uuid4
from storage.storage import Storage
from helper.helper import Helper
class Employe(ABC):
    def __init__(self,name,role,email,id=None):
        self.id = id or str(uuid4())
        self.name = name
        self.role = role
        self.email = email

    @abstractmethod
    def calculate_monthly_salay(self):
        pass

    
            


    