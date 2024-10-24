class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make.upper() > rhs.make.upper():
            return True
        elif self.make.upper() == rhs.make.upper():
            if self.model.upper() > rhs.model.upper():
                return True
            elif self.model.upper() == rhs.model.upper():
                if self.year > rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price > rhs.price:
                        return True
        return False
        
    def __lt__(self, rhs):
        if self.make.upper() < rhs.make.upper():
            return True
        elif self.make.upper() == rhs.make.upper():
            if self.model.upper() < rhs.model.upper():
                return True
            elif self.model.upper() == rhs.model.upper():
                if self.year < rhs.year:
                    return True
                elif self.year == rhs.year:
                    if self.price < rhs.price:
                        return True
        return False

    def __eq__(self, rhs):
        if rhs is None:
            return False
        elif self.make.upper() == rhs.make.upper() and \
           self.model.upper() == rhs.model.upper() and self.year == \
           rhs.year and self.price == rhs.price:
            return True
        else:
            return False

    def __str__(self):
        return "Make: {}, Model: {}, Year: {}, Price: ${}".format(self.make, \
                                             self.model, self.year, self.price)

