# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:05:50 2020

@author: abiso
"""

class ContactList(list):
    """ Extending a built-in class like "list" with a method search """
    def search(self, name):
        
        ''' return all contacts that contain the search values in their names'''
        
        matching_contacts =[]
        
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)                
        return matching_contacts


class Contact:
    
    all_contacts = ContactList()
    
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email= email
        self.all_contacts.append(self)
        

class Suppliers(Contact):
    def order(self, order):
        print("If this were a real system we would send ","{} order to {}".format(order, self.name))
        

class MailSender:
    
    def send_mail(self, message):
        print("Sending mail to" + self.email)
        # Add e-mail logic here 

class EmailableContact(Contact,MailSender):
    pass
    

class AddressHolder:
    def __init__(self, street, city, state, code, **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friends(Contact,AddressHolder):
    
    """Using the super() Extending attributes Address to the group friends which is a contact which wasn't a initially an 
    an attribute, the friends class can take arguments from both the Address and Contact Class and Vice-Versa
    any argument which isn't recognised in any class can be added to the next super class which might 
    be in need or use it before calling the base parent class """
    
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone 
    