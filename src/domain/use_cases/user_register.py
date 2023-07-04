from abc import ABC, abstractmethod
from typing import Dict

class UserRegister(ABC):

    @abstractmethod
    def register(self, first_name: str, last_name: str, age: int) -> Dict: pass
