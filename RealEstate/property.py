# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:30:28 2020

@author: abiso
"""


class Property:
    valid_status = ("available", "purchased","rented")
    def __init__(self, square_feet ='', beds='',baths='',status='', **kwargs):
        
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths=baths
        self.status = status
      
        
    
    def display(self):
        
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()
        
    def prompt_init():
        
        return dict(square_feet=input("Enter the square feet: "), beds=input("Enter the number of bedroom: "),
                    baths=input("Enter the number of bathrooms: "), status=get_valid_input("what is the" 
                                "status of the property's occupancy?",Property.valid_status))
    prompt_init = staticmethod(prompt_init)
    

class Apartment(Property):
    
    valid_laundries = ("coin", "ensuite","none")
    valid_balconies = ("yes","no", "solarium")
    
    def __init__(self, balcony='',laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony= balcony
        self.laundry = laundry
        
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does"
            "the property have?", 
            Apartment.valid_laundries)
        balcony=get_valid_input(
            "Does the property have a balcony?",
            Apartment.valid_balconies)
        
        parent_init.update({
            "laundry": laundry,
            "balcony":balcony
        })
        
        return parent_init
    prompt_init = staticmethod(prompt_init)
     
class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories
    
    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))
        
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                    House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                    House.valid_garage)
        num_stories = input("How many stories? ")
        
        parent_init.update({
            "fenced": fenced,
            "garage": garage, 
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)
    
class Purchase:    
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes
        
    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimared taxeds: {}".format(self.taxes))
        
    def prompt_init():
        
        return dict(price= input("What is the selling price? "),
                    taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)
    
    
class Rental:
    
    def __init__(self, furnished='', utilities='',rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities
    
    def display(self):
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities:{}".format(self.utilities))
        print("furnished: {}".format(self.furnished))
        
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities = input(
                "What are the estimated utilites? "),
            furnished = get_valid_input(
                "Is the property furnished? ",
                    ("yes", "no")))
    prompt_init= staticmethod(prompt_init)
    

class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
    
    
def get_valid_input(input_string, valid_options):
    input_string+= " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response
        


class ApartmentRental(Rental,Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init 
    prompt_init = staticmethod(prompt_init)
    
class ApartmentPurchase(Purchase,Apartment):
    def prompt_init():
        init = Apartment.prompt_init()
        init.updata(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
    
class HousePurchase(Purchase,House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)
    
class Agent:
    
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
        }
    def __init__(self):
        self.property_list = []
        self.available_properties =[]
        self.unavailable_properties = []
        
        
    def display_properties(self):
        
        for property in self.property_list:
            property.display()
            
    def add_property(self):
        
       
        
        property_type = get_valid_input(
               "What type of property? ", 
               ("house", "apartment")).lower()
        
        payment_type = get_valid_input(
              "What payment type? ",
              ("purchase", "rental")).lower()
        
        PropertyClass = self.type_map[
             (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
        
        if init_args.status == "available":
            self.available_properties.append(init_args)
        else: 
            self.unavailable_properties.append(init_args)
          
        
    
    def search_property(self):
        
        property_type = get_valid_input(
               "What type of property? ", 
               ("house", "apartment")).lower()
        
        payment_type = get_valid_input(
              "What payment type? ",
              ("purchase", "rental")).lower()
        status_type = get_valid_input("What type of property? ", 
               ("available", "purchased","rented")).lower()
        
        PropertyClass = self.type_map[
            (property_type,payment_type)]
        for property in self.property_list:
            if isinstance(property, PropertyClass): 
                if property.status == status_type:
                    property.display()
                else: 
                    return ("This type of Property is not Availabls")
            else:
                return  ("This type of Property is not Available")
            
    def display_available_properties(self):
         
         for property in self.available_properties:
             property.display()
    def display_no_of_properties(self):
         
         return ("There are {}".format(len(no_property)))
    