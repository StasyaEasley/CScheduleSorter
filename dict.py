from bs4 import BeautifulSoup

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
for h2 in all_hs:
    this_text = h2.text
    h2_list.append(this_text.split(":"))

description_list = []
career_list = []
grade_basis_list = []
course_comp_list = []
for sublist in h2_list:
    if sublist[0] == 'Description':
        description_list.append(sublist[1])
    elif sublist[0] == 'Career':
        career_list.append(sublist[1])
    elif sublist[0] == 'Grading basis':
        grade_basis_list.append(sublist[1])
    elif sublist[0] == 'Course Components':
        course_comp_list.append(sublist[1])
csc_list = []
for sublist in ps_list:
    if 'CSC' in sublist[0]:
        csc_list.append(sublist[0])

description_file = open("description.tsv", "w")
for i in range(len(description_list)):
    description_file.write(csc_list[i])
    description_file.write("\t")
    description_file.write(description_list[i])
    description_file.write("\t")
    description_file.write(career_list[i])
    description_file.write("\t")
    description_file.write(course_comp_list[i])
    description_file.write("\n")
    """description_file.write(grade_basis_list[i])
        description_file.write("\t")"""

description_file.close()

ps3_list = []
all_ps3 = soup.find_all("p", class_="s3")
for p in all_ps3:
    this_text = p.text
    ps3_list.append(this_text.split(":"))

new_file = open("course_info.tsv", "w")
for sublist in ps3_list:
    new_file.write("\t".join(sublist) + "\n")
new_file.close()

"""res = list(map(lambda x: x if x != [''] else None, ps_list))
res = [x for x in res if x != None]
print(str(res))"""

"""
Need: Course Name & Title (p)
Description (h2)
Units (p)
Career level (h2)
Grading (h2)
course components (h2)
enrollment req (h2)
course typically offered (p)
"""
