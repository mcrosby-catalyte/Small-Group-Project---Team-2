class EspressOCustomer(): 

    def __init__(self, customer_name: str, email: str, lifetime_spent: float): 
        
        self.customer_name = customer_name
        self.email = email
        self.lifetime_spent = lifetime_spent

    def to_dict(self): 
          """Return a dictionary representation of the customer."""
          
          return {

            "customer_name": self.customer_name, 
            "email": self.email,
            "lifetime_spent": self.lifetime_spent 
        }
    
    