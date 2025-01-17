# from abc import ABC, abstractmethod
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:

    @staticmethod
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage,tire_data): 
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTires(tire_data)
        car = Car(engine,battery)
        return car

    @staticmethod
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage,tire_data): 
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = OctoprimeTires(tire_data)
        car = Car(engine,battery)
        return car

    @staticmethod
    def create_palindrome(self,current_date, last_service_date, warning_light_on, tire_data): 
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date,last_service_date)
        tires = CarriganTires(tire_data)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage,tire_data):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = OctoprimeTires(tire_data)
        car = Car(engine,battery)
        return car 
    
    @staticmethod
    def create_thovexe(self,current_date, last_service_date, current_mileage, last_service_mileage,tire_data):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tires = CarriganTires(tire_data)
        car = Car(engine,battery)
        return car 
    
