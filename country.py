input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8') as country_file:
    for row in country_file:
        data = row.strip('\n').split('|')
        print(data)
