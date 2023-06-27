from abc import ABC, abstractmethod
from typing import Dict

class UserFinder(ABC):

    @abstractmethod
    def find(self, first_name: str) -> Dict: pass
