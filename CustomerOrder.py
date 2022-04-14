sep = " --- "


# This class puts all order details into one list to be written in the cvs file

class CustomerOrder:
    def __init__(self, init_details, pet_name, sku, line1, line2, line3, line4, line5, color):
        self.finalOrder = []
        self.finalOrder.extend(init_details)
        self.finalOrder.append(sep.join(pet_name))
        self.finalOrder.append(sep.join(sku))
        self.finalOrder.append(sep.join(color))
        self.finalOrder.append(sep.join(line1))
        self.finalOrder.append(sep.join(line2))
        self.finalOrder.append(sep.join(line3))
        self.finalOrder.append(sep.join(line4))
        self.finalOrder.append(sep.join(line5))