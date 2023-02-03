"""Classes for melon orders."""
import random
import datetime

#date.weekday() Return the day of the week as an integer, where Monday is 0 and Sunday is 6
#date.isoweekday()
#Return the day of the week as an integer, 
# where Monday is 1 and Sunday is 7. For example, 
# date(2002, 12, 4).isoweekday() == 3, a Wednesday. See also weekday(), isocalendar().

#

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        
        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

# >>> now.time()
# datetime.time(15, 8, 24, 78915)
# >>> print(now.time())
# 15:08:24.789150

    def get_base_price(self):
        splurge_price = random.randint(5,9)

        current_date = datetime.date.today()
        is_weekday = datetime.date.isoweekday(current_date) 

        now = datetime.datetime.now()

        current_time = str(now.time()) #15:08:24.789150
        current_hour = current_time[:2]
        current_hour = int(current_hour)
    

        if is_weekday < 6 and current_hour <= 11 and current_hour >= 8 :
            splurge_price += 4

        return splurge_price


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class GovernmentMelonOrder(AbstractMelonOrder):
    
    tax = 0
    order_type = "government"
    
    
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    

    def mark_inspection(self, passed):

        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)          


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
        

    def get_total(self):
        total = super().get_total()
        if self.qty <10:
            total += 3
        else:
            total
        return total 

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
