from abc import ABC, abstractmethod

Class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass