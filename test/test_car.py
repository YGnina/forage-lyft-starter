import unittest
# from datetime import datetime

# from engine.model.calliope import Calliope
# from engine.model.glissade import Glissade
# from engine.model.palindrome import Palindrome
# from engine.model.rorschach import Rorschach
# from engine.model.thovex import Thovex

# test engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

# test battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestCapuletEngine(unittest.TestCase):
    def test_serviced(self):
        current_mileage = 30003
        last_service_mileage = 2

        engine = Calliope(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_not_serviced(self):
        current_mileage = 199
        last_service_mileage = 2

        engine = Calliope(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_not_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_serviced(self):
        current_mileage = 60003
        last_service_mileage = 2

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_not_serviced(self):
        current_mileage = 199
        last_service_mileage = 2

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_not_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_battery_not_serviced(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
