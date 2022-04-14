file = ""
f = "shipping label.pdf"
import pdfplumber
import csv

endStatement = "the seller's name under the appropriate product. Then, in the \"Further Information\" section, click \"Contact the Seller.\""

headers = ['OrderNumber', 'FullName', "Address", "Pet Names", "SKU", "Color", "Line1",
           "line2", "line3", "line4", "line5"]

sep = " --- "
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
        print(self.finalOrder)


class Track:

    def __init__(self, order_list):
        self.order_list = order_list
        self.pet_name = []
        self.order_items = []
        self.sku = []
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []
        self.line5 = []
        self.color = []
        self.order_id = []

    def parse_each_order(self):
        for orders in self.order_list:
            sku = "SKU: "
            for order in range(len(orders)):
                if order == 0:
                    self.order_items.append(orders[order])
                elif sku in orders[order]:
                    self.sku.append(orders[order].split(" Tax")[0].split("SKU: ")[1])
                elif "Order Item ID:" in orders[order]:
                    self.order_id.append(orders[order].split("Order Item ID: ")[1])
                elif "Font Color:" in orders[order]:
                    self.color.append(orders[order].split("Font Color: ")[1].split(" (")[0])
                elif "Pet Name:" in orders[order]:
                    self.pet_name.append(orders[order].split("Pet Name: ")[1])
                elif "Line 1:" in orders[order]:
                    self.line1.append(orders[order].split("Line 1: ")[1])
                elif "Line 2:" in orders[order]:
                    self.line2.append(orders[order].split("Line 2: ")[1])
                elif "Line 3:" in orders[order]:
                    self.line3.append(orders[order].split("Line 3: ")[1])
                elif "Line 4:" in orders[order]:
                    self.line4.append(orders[order].split("Line 4: ")[1])
                elif "Line 5:" in orders[order]:
                    self.line5.append(orders[order].split("Line 5: ")[1])
                else:
                    continue

    def print_order(self):
        for i in self.order_list:
            print(i)

    def printAll(self):
        print(self.pet_name)
        print(self.sku)
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.color)
        print(self.order_id)


def open_pdf(fd):
    with pdfplumber.open(fd) as pdf:
        order = []
        # 12 14
        all_customers = []
        num = 0
        # 16,17
        for i in range(len(pdf.pages)):
            content = pdf.pages[i].extract_text().split('\n')
            num += 1
            if content[len(content) - 2] == endStatement:
                order.extend(content[1:-1])
                init_details = parse(order)
                total_order_list = find_total_order(order)
                order_details = subOrder(total_order_list)
                order_details.parse_each_order()
                # fill_with_Nonez()
                # order_details.printAll()

                customer = CustomerOrder(init_details, order_details.pet_name, order_details.sku, order_details.line1,
                                         order_details.line2,
                                         order_details.line3, order_details.line4, order_details.line5,
                                         order_details.color)
                all_customers.append(customer)
                order = []
            else:
                order.extend(content[1:-1])

    writeToCSV(all_customers)


def writeToCSV(customers):
    with open('order.csv', 'w', newline="", encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in customers:
            writer.writerow(i.finalOrder)
    f.close()


def find_total_order(array):
    total_order_list = []
    for i in range(0, len(array)):
        if "Grand total:" in array[i]:
            return total_order_list
        else:
            total_order_list.append(array[i])
    return total_order_list


def subOrder(array):
    order_list = []
    temp = []
    line = False
    for i in array:
        # case when there is another order
        if line and "Line " not in i:
            order_list.append(temp)
            line = False
            temp = [i]

        # Case for the first line
        elif not line and "Line " in i:
            line = True
            temp.append(i)
        else:
            temp.append(i)
    order_list.append(temp)
    # for i in order_list:
    #     print(i)
    return Track(order_list)


def parse(array):
    temp = []
    for i in array:
        if "Thank you" in i:
            break
        else:
            temp.append(i)

    name = temp[1].strip()
    fullAddess = "".join(temp[2:len(temp) - 2]).strip()
    order = temp[len(temp) - 1].split(' ')[2]

    return [order, name, fullAddess]


if __name__ == '__main__':
    open_pdf(fd="Amazon.pdf")