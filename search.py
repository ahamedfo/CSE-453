import csv

def search_helper(dictionary):
    row_num = [3,6,7,8,9,10]
    check_dict = {}
    for i, key in enumerate(dictionary.keys()):
        if dictionary[key] != '0':
            check_dict[row_num[i]] = dictionary[key]
    return check_dict

def search(dictionary):
    text_boxes = search_helper(dictionary)
    csv_file = csv.reader(open('order.csv', "r"), delimiter=",")
    next(csv_file)
    retRows = []
    for row in csv_file:
        Good_row = True
    #if current rows 2nd value is equal to input, print that row
        for row_num in text_boxes.keys():
            if text_boxes[row_num].lower() not in row[row_num].lower():
                Good_row = False
        if Good_row:
            retRows.append(row)
    return retRows, text_boxes