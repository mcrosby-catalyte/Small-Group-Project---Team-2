#I want to create a loyalty program that send promotions via email and msm. 
#The customer gains 10 points per $1.00 spent and tracked by the customers phone number 
#Will need to import customers.py file to use customer instances and data. 

import customers


class loyalty_program(): 

    def __init__(self, phone, email, lifetime_spent): 
        