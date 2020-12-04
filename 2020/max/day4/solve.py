import functools
from travel_document_part2 import TravelDocument

def parse():
    travel_documents = []

    travel_document = TravelDocument()
    
    with open('input') as input:
        for line in input:
            line = line.strip()
            if len(line) == 0:
                travel_documents.append(travel_document)
                travel_document = TravelDocument()
                next
            
            for kvp in line.split():
                key = kvp.split(':')[0]
                value = kvp.split(':')[1]

                if key == 'byr': travel_document.byr = value
                if key == 'iyr': travel_document.iyr = value
                if key == 'eyr': travel_document.eyr = value
                if key == 'hgt': travel_document.hgt = value
                if key == 'hcl': travel_document.hcl = value
                if key == 'ecl': travel_document.ecl = value
                if key == 'pid': travel_document.pid = value
                if key == 'cid': travel_document.cid = value
                
    return travel_documents

def count_valid(travel_documents):
    number_of_valid = 0
    for travel_document in travel_documents:
        if travel_document.is_valid():
            number_of_valid += 1
    return number_of_valid

travel_documents = parse()

print(f'Parsed input into {len(travel_documents)} travel documents')

number_of_valid = count_valid(travel_documents)

print(f'Found {number_of_valid} valid travel documents')
