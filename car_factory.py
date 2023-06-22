from abc import ABC, abstractmethod

class CarFactory:

    @abstractmethod
    def create_calliope(self,current_date, last_service_date, current_mileage, last_service_mileage): 
        pass

    @abstractmethod
    def create_glissade(self,current_date, last_service_date, current_mileage, last_service_mileage): 
        pass

    @abstractmethod
    def create_palindrome(self,current_date, last_service_date, warning_light_on): 
        pass
    
    @abstractmethod
    def create_rorschach(self,current_date, last_service_date, current_mileage, last_service_mileage):
        pass 
    
    @abstractmethod
    def create_thovexe(self,current_date, last_service_date, current_mileage, last_service_mileage):
        pass 
    
