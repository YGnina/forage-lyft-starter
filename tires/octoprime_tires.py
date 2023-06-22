from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_data):
        self.tire_data = tire_data

    def needs_service(self):
        return sum(tire_data) >= 3
