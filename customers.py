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

    def __repr__(self):
        return f"EspressOCustomer(customer_name='{self.customer_name}', email='{self.email}', lifetime_spent={self.lifetime_spent})"


customers = [
    
    EspressOCustomer("Zephyr Smith", "zephyr.smith01@example.com", 120.50),
    EspressOCustomer("Luna Johnson", "luna.johnson42@example.com", 75.00),
    EspressOCustomer("Orion Brown", "orion.brown77@example.com", 200.25),
    EspressOCustomer("Indigo Davis", "indigo.davis88@example.com", 50.75),
    EspressOCustomer("Echo Miller", "echo.miller99@example.com", 300.00),
    EspressOCustomer("Nova Wilson", "nova.wilson@example.com", 15.50),
    EspressOCustomer("Jett Moore", "jett.moore@example.com", 180.20),
    EspressOCustomer("Phoenix Taylor", "phoenix.taylor@example.com", 90.10),
    EspressOCustomer("Sage Anderson", "sage.anderson@example.com", 250.00),
    EspressOCustomer("Atlas Thomas", "atlas.thomas@example.com", 60.00),
    EspressOCustomer("Indie Martin", "kawaii.indie@example.com", 145.75),
    EspressOCustomer("Arrow White", "ninja.arrow@example.com", 80.40),
    EspressOCustomer("Orla King", "senpai.orla@example.com", 220.90),
    EspressOCustomer("Rogue Scott", "shinigami.rogue@example.com", 135.60),
    EspressOCustomer("Lyric Reed", "otaku.lyric@example.com", 170.25),
]
