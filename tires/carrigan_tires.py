from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_data):
        self.tire_data = tire_data

    def needs_service(self):
        for i in self.tire_data:
            if i >= 0.9:
                return False
        return True
