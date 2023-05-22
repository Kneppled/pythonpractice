from xml.etree import ElementTree
import csv

fromFile = input('Input a XML file name to be converted:')
tree = ElementTree.parse(fromFile)
root = tree.getroot()

header = 0
header_list = []
info_list = []    

toFile = input('Enter a name for the new CSV:')
with open(toFile,'w', newline='') as csvFile:
    csvWriter = csv.writer(csvFile)

    for transaction in root:
        if header == 0:
            date = transaction.find('Date').tag
            header_list.append(date)
            agent = transaction.find('Agent').tag
            header_list.append(agent)
            commodity = transaction.find('Commodity').tag
            header_list.append(commodity)
            amount = transaction.find('Amount').tag
            header_list.append(amount)
            csvWriter.writerow(header_list)
            header +=1
        
        first = transaction.find('Date').text
        info_list.append(first)
        second = transaction.find('Agent').text
        info_list.append(second)
        third = transaction.find('Commodity').text
        info_list.append(third)
        fourth = transaction.find('Amount').text
        info_list.append(fourth)
        csvWriter.writerow(info_list)
        info_list.clear()





    
    

