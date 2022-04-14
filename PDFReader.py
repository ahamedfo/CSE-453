import pdfplumber
import csv
from CustomerOrder import CustomerOrder
from TrackEachOrder import Track

endStatement = "the seller's name under the appropriate product. Then, in the \"Further Information\" section, click \"Contact the Seller.\""

headers = ['OrderNumber', 'FullName', "Address", "Pet Names", "SKU", "Color", "Line1",
           "line2", "line3", "line4", "line5"]


class PDFReader:
    def __init__(self, fd, cvs_name):
        self.fd = fd
        self.cvs_name = cvs_name

    def open_pdf(self):
        # Open pds
        count = 0
        with pdfplumber.open(self.fd) as pdf:
            # This will hold all the details of each order
            order = []
            # Holds each customer order
            all_customers = []

            for i in range(len(pdf.pages)):

                # Extract each of the pages
                content = pdf.pages[i].extract_text().split('\n')
                # Checks if the end of the page has been reach, if not then add the next page to the order
                if content[len(content) - 2] == endStatement:
                    # ignore the first and end statement
                    order.extend(content[1:-1])

                    init_details = self.parse(order)
                    total_order_list = self.find_total_order(order)
                    order_details = self.subOrder(total_order_list)
                    order_details.parse_each_order()

                    customer = CustomerOrder(init_details, order_details.pet_name, order_details.sku,
                                             order_details.line1, order_details.line2,
                                             order_details.line3, order_details.line4, order_details.line5,
                                             order_details.color)
                    all_customers.append(customer)
                    print(customer)
                    # now that a customer has been stored and we reached the final order, we must reset order
                    order = []
                    count += 1
                else:
                    order.extend(content[1:-1])
        print(count)
        self.write_to_csv(all_customers)

    def write_to_csv(self, customers):
        with open(self.cvs_name, 'w', newline="", encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for i in customers:
                writer.writerow(i.finalOrder)
        f.close()

    def find_total_order(self, array):
        total_order_list = []
        for i in range(0, len(array)):
            if "Grand total:" in array[i]:
                return total_order_list
            else:
                total_order_list.append(array[i])
        return total_order_list

    def subOrder(self, array):
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
        return Track(order_list)

    def parse(self, array):
        temp = []
        for i in array:
            if "Thank you" in i:
                break
            else:
                temp.append(i)

        name = temp[1].strip()
        full_address = "".join(temp[2:len(temp) - 2]).strip()
        order = temp[len(temp) - 1].split(' ')[2]

        return [order, name, full_address]