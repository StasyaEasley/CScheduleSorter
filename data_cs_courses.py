from bs4 import BeautifulSoup
import pandas as pd

html_file = open("jJ4fRq-UA_PCC_XML.html").read()
soup = BeautifulSoup(html_file, "html.parser")

ps_list = []
all_ps = soup.find_all("p")
for p in all_ps:
    this_text = p.text
    ps_list.append(this_text.split(":"))

ps_list.pop(153)

h2_list = []
all_hs = soup.find_all("h2")
current_description = None
description_lists = []

# this splits h2 into a bunch of sublists everytime it encounters a
# description string
for h2 in all_hs:
    this_text = h2.text
    split_text = this_text.split(":")
    if split_text[0] == 'Description':
        if current_description is not None:
            description_lists.append(current_description)
        current_description = [split_text[0], split_text[1].strip()]
    else:
        if current_description is not None:
            current_description.append(split_text[0])
            current_description.append(split_text[1].strip())

# Append the last description list
if current_description is not None:
    description_lists.append(current_description)

# Check and add "Enrollment requirement" and a fake requirement
for sublist in description_lists:
    if 'Description' in sublist:
        if 'Enrollment requirement' not in sublist:
            sublist.extend(['Enrollment requirement', 'None'])
        if 'Grading basis' not in sublist:
            sublist.extend(['Grading basis', 'None'])
        if "Equivalent to" not in sublist:
            sublist.extend(['Equivalent to', 'None'])


description_list = []
career_list = []
course_comp_list = []
grade_basis_list = []
enroll_req_list = []
equivalent_list = []

for sublist in description_lists:
    if sublist[0] == 'Description':
        description_list.append(sublist[1])
    if 'Description' in sublist:
        index = sublist.index('Enrollment requirement')
        enroll_req_list.append(sublist[index + 1])
    if 'Description' in sublist:
        index = sublist.index('Career')
        career_list.append(sublist[index + 1])
    if 'Description' in sublist:
        index = sublist.index('Grading basis')
        grade_basis_list.append(sublist[index + 1])
    if 'Description' in sublist:
        index = sublist.index('Course Components')
        course_comp_list.append(sublist[index + 1])
    if 'Description' in sublist:
        index = sublist.index('Equivalent to')
        equivalent_list.append(sublist[index + 1])

enroll_req_list[22] = "Completion of CSC 210 and CSC 252"
enroll_req_list[23] = ("Advanced Standing: Engineering. ECE 275 and MATH 243. "
                       "Students may not have completed or be enrolled in CSC"
                       " 345.")

csc_list = []
spring_fall_list = []
for sublist in ps_list:
    if 'CSC' in sublist[0]:
        csc_list.append(sublist[0])
    elif 'Main Campus' in sublist[0]:
        spring_fall_list.append(sublist[1])


description_file = open("description.tsv", "w")
for i in range(len(description_lists)):
    description_file.write(csc_list[i])
    description_file.write("\t")
    description_file.write(description_list[i])
    description_file.write("\t")
    description_file.write(enroll_req_list[i])
    description_file.write("\t")
    description_file.write(career_list[i])
    description_file.write("\t")
    description_file.write(spring_fall_list[i])
    description_file.write("\t")
    description_file.write(grade_basis_list[i])
    description_file.write("\t")
    description_file.write(course_comp_list[i])
    description_file.write("\t")
    description_file.write(equivalent_list[i])
    description_file.write("\n")

description_file.close()


ps3_list = []
class_name_list = []
all_ps3 = soup.find_all("p", class_="s3")
for p in all_ps3:
    this_text = p.text
    ps3_list.append(this_text.split(":"))
for sublist in ps3_list:
    class_name_list.append(sublist[1])

new_file = open("course_info.tsv", "w")
for sublist in ps3_list:
    new_file.write("\t".join(sublist) + "\n")
new_file.close()

team = pd.DataFrame(list(
    zip(csc_list, class_name_list, description_list, career_list,
        spring_fall_list,enroll_req_list, grade_basis_list, course_comp_list,
        equivalent_list)),
    columns=['Class', 'Class Name', 'Description', 'Career', 'Offered',
             'Enrollment Requirement','Grading Basis', 'Course Components',
             'Equivalent To'])

# combines tsv files
cour = pd.read_csv('course_info.tsv', sep='\t')
desc = pd.read_csv('description.tsv', sep='\t')
merged_data = pd.merge(cour, desc, on='CSC 101')
merged_data.to_csv('merged_data.tsv', sep='\t', index=True)

merged_file = open("merged_data.tsv", "w")
merged_file.write("\t".join(team.columns) + "\n")
for i in range(len(description_lists)):
    merged_file.write("\t".join(str(item) for item in team.iloc[i]) + "\n")
merged_file.close()
