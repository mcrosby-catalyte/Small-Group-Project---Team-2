class EspressOCustomer(): 

    def __init__(self, customer_name: str, email: str, phone: str, lifetime_spent: float): 

        self.customer_name = customer_name
        self.email = email
        self.phone = phone
        self.lifetime_spent = lifetime_spent

    def to_dict(self): 
        """Return a dictionary representation of the customer."""

        return {

            "customer_name": self.customer_name, 
            "email": self.email,
            "phone": self.phone,
            "lifetime_spent": self.lifetime_spent 
        }

    def __repr__(self):
        return f"EspressOCustomer(customer_name='{self.customer_name}', email='{self.email}', phone='{self.phone}', lifetime_spent={self.lifetime_spent})"


customers = [
    
    EspressOCustomer("Zephyr Smith", "zephyr.smith01@example.com", "773-123-3456", 120.50),
    EspressOCustomer("Luna Johnson", "luna.johnson42@example.com", "312-312-3124", 75.00),
    EspressOCustomer("Orion Brown", "orion.brown77@example.com", "312-890-0003", 200.25),
    EspressOCustomer("Indigo Davis", "indigo.davis88@example.com", "708-333-0001", 50.75),
    EspressOCustomer("Echo Miller", "echo.miller99@example.com", "708-000-1111", 300.00),
    EspressOCustomer("Nova Wilson", "nova.wilson@example.com", "708-870-3333", 15.50),
    EspressOCustomer("Jett Moore", "jett.moore@example.com", "773-213-0023", 180.20),
    EspressOCustomer("Phoenix Taylor", "phoenix.taylor@example.com", "312-111-2222", 90.10),
    EspressOCustomer("Sage Anderson", "sage.anderson@example.com", "312-455-9898", 250.00),
    EspressOCustomer("Atlas Thomas", "atlas.thomas@example.com", "872-900-8000", 60.00),
    EspressOCustomer("Indie Martin", "kawaii.indie@example.com", "785-235-1212", 145.75),
    EspressOCustomer("Arrow White", "ninja.arrow@example.com", "630-455-7823", 80.40),
    EspressOCustomer("Orla King", "senpai.orla@example.com","630-233-8755", 220.90),
    EspressOCustomer("Rogue Scott", "shinigami.rogue@example.com", "331-777-0983", 135.60),
    EspressOCustomer("Lyric Reed", "otaku.lyric@example.com", "773-800-8888", 170.25),

]


