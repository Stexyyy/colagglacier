import csv

# Variables
file = 'wgi_glacier_data.csv'
name_index = 0
form_index = 1
latitude_index = 2
area_index = 3

# Step 1: csv_reader(file)
def csv_reader(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        return [row for row in reader]

# Test csv_reader
#print("TESTING", len(csv_reader(file)))

# Step 2: longest_glacier_name(glacier_list)
def longest_glacier_name(glacier_list):
    names = [row[name_index] for row in glacier_list]
    return max(names, key=len)

# Test longest_glacier_name
test_list = [['one','AT','4','short','0','0','0','0','0','0'],
             ['two','US','2','longest name','0','0','0','2','0','0']]
#print("TESTING", longest_glacier_name(test_list))
#print("TESTING", longest_glacier_name(csv_reader(file)))

# Step 3: most_common_glacier_form(glacier_list)
def most_common_glacier_form(glacier_list):
    forms = [row[form_index] for row in glacier_list]
    form_counts = {form: forms.count(form) for form in set(forms)}
    return max(form_counts, key=form_counts.get)

# Test most_common_glacier_form
test_list = [['one','AT','4','short','0','0','0','0','0','0'],
             ['two','US','2','longest name','0','0','0','2','0','0'],
             ['three','US','2','median','0','0','0','0','0','0']]
#print("TESTING", most_common_glacier_form(test_list))
#print("TESTING", most_common_glacier_form(csv_reader(file)))

# Step 4: highest_latitude(glacial_list)
def highest_latitude(glacier_list):
    max_latitude = max(glacier_list, key=lambda x: float(x[latitude_index]))
    return max_latitude[name_index]

# Test highest_latitude
# Add latitude values to your test_list
test_list = [['one','AT','4','short','0','0','0','0','0','0', '60.5'],
             ['two','US','2','longest name','0','0','0','2','0','0', '70.3']]
#print("TESTING", highest_latitude(test_list))
#print("TESTING", highest_latitude(csv_reader(file)))

def average_area(glacier_list):
    areas = []
    valid_count = 0  # Track the number of valid areas
    max_warnings = 5  # Set a maximum number of warnings to print

    for row in glacier_list:
        area_value = row[area_index]

        # Check if the area value is a valid number
        try:
            if area_value != '' and area_value.replace('.', '', 1).isdigit():
                areas.append(float(area_value))
                valid_count += 1
        except Exception as e:
            print(f"Error processing area value for glacier {row[name_index]} - {e}")

    if max_warnings == 0:
        print("Additional warnings omitted.")

    return sum(areas) / valid_count if valid_count > 0 else 0

# Step 6: main()
def main():
    glacier_list = csv_reader(file)

    avg_area = average_area(glacier_list)
    highest_lat_name = highest_latitude(glacier_list)
    common_form = most_common_glacier_form(glacier_list)
    longest_name = longest_glacier_name(glacier_list)

    print(f"Average Area: {avg_area:.2f}")
    print(f"Highest Latitude Name: {highest_lat_name}")
    print(f"Most Common Glacier Form: {common_form}")
    print(f"Longest Glacier Name: {longest_name}")

# Uncomment the following line on submission
if __name__ == '__main__':
    main()
