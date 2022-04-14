# This class Tracks each order
class Track:

    def __init__(self, order_list):
        self.order_list = order_list
        self.pet_name = []
        self.sku = []
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []
        self.line5 = []
        self.color = []
        self.order_id = []

    # This function parses each order and appends it to its specific self.var
    def parse_each_order(self):
        for orders in self.order_list:
            SKU = "SKU: "
            FONT = "Font Color: "
            PETNAME = "Pet Name:"
            LINE1 = "Line 1:"
            LINE2 = "Line 2:"
            LINE3 = "Line 3:"
            LINE4 = "Line 4:"
            LINE5 = "Line 5:"

            for order in range(len(orders)):
                if SKU in orders[order]:
                    self.sku.append(orders[order].split(" Tax")[0].split("SKU: ")[1])
                elif FONT in orders[order]:
                    self.color.append(orders[order].split("Font Color: ")[1].split(" (")[0])
                elif PETNAME in orders[order]:
                    self.pet_name.append(orders[order].split("Pet Name: ")[1])
                elif LINE1 in orders[order]:
                    self.line1.append(orders[order].split("Line 1: ")[1])
                elif LINE2 in orders[order]:
                    self.line2.append(orders[order].split("Line 2: ")[1])
                elif LINE3 in orders[order]:
                    self.line3.append(orders[order].split("Line 3: ")[1])
                elif LINE4 in orders[order]:
                    self.line4.append(orders[order].split("Line 4: ")[1])
                elif LINE5 in orders[order]:
                    self.line5.append(orders[order].split("Line 5: ")[1])
                else:
                    continue

    # This functions prints the all the variables in self
    def print_self(self):
        print(self.pet_name)
        print(self.sku)
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.color)
        print(self.order_id)