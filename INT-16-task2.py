import json

input_file_path = "path_and_filename"
output_file_path = "path_and_filename"
report = {'vulnerabilities': []}

with open(input_file_path, "r") as file:
    dictionary = {}

    for line in file:
        if "\"name\"" in line:
            dictionary["name"] = line[line.find(':')+3:line.find(',')-1]
        elif "count" in line:
            dictionary["count"] = ''.join(char for char in line if char.isdigit())
        if "name" in dictionary and "count" in dictionary:
            report['vulnerabilities'].append(dictionary)
            dictionary = {}

with open(output_file_path, "w+") as file_2:
    file_2.write(json.dumps(report, indent=3))
