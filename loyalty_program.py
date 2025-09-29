
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
        print(f"Email sent to {self.customer.email}: {message}")

    def send_sms_promo(self, message: str):
        print(f"SMS sent to {self.customer.phone}: {message}")
