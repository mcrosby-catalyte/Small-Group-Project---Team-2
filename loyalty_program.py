import customers


class LoyaltyProgram:
    points_per_dollar = 10  

    def __init__(self, customer): 
        """Initialize loyalty program with a customer instance."""
        self.customer = customer
        self.points = int(customer.lifetime_spent * self.points_per_dollar)

    def add_purchase(self, amount: float):
        """Update customer's spending and add points."""
        self.customer.lifetime_spent += amount
        self.points += int(amount * self.points_per_dollar)

    def send_email_promo(self, message: str): 
        """ 
        sends customers promotional emails

        """
        print(f"Email sent to {self.customer.email}: {message}")

    def send_sms_promo(self, message: str): 
        """
        sends customers promtotional text messages

        """
        print(f"SMS sent to {self.customer.phone}: {message}")



#CRUD FUNCTIONALITY  


all_customers = []  


def create_loyalty_member(name, email, phone, lifetime_spent=0):
    """
    Create a new customer and loyalty program instance if lifetime spent is $1 or more.
    """
    if lifetime_spent >= 1:  # only create if spent >= $1
        # Create a new customer object
        new_customer = customers.Customer(
            name=name, email=email, phone=phone, lifetime_spent=lifetime_spent
        )

        # Add the customer to our 'database'
        all_customers.append(new_customer)

        # Create a LoyaltyProgram instance for this customer
        loyalty_member = LoyaltyProgram(new_customer)

        return f"{name} is now a loyalty member!", loyalty_member
    else:
        return "Customer must spend at least $1 to join the loyalty program."


def retrieve_loyalty_member_information():
    """
    Retrieve all loyalty members whose names start with A-H.
    """
    results = []

    for customer in customers:
        first_letter = customer.name[0].upper()  
        if "A" <= first_letter <= "H":  
            results.append(
                {
                    "name": customer.name,
                    "email": customer.email,
                    "phone": customer.phone,
                }
            )

    if results:
        return results
    else:
        return "I said NO NO NOOOOO Customer name starts with the letters A-H."
    

