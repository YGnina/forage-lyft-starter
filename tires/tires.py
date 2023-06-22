from serviceable import Serviceable

class Tires(ABC):
    @abstractmethod
    def needs_service(self):
        pass
