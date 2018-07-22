import glob 
import csv 

def check_major(row):
	new_row = row.strip() 
	if row == "":
		new_row = "CE"
	return new_row

def main():
	students = glob.glob("students*.csv")

	#Students 
	if len(students) > 1:
		print ("Please have only one student file")
		return -1

	if len(students) < 1:
		print ("Please have more than one student file")
		return -1

	new_student_rows = []
	with open(students[0], 'rb') as csvfile:
		student_reader = csv.reader(csvfile, delimiter = ',', quotechar='|')
		for row in student_reader:
			temp_row = []
			temp_row.append(row[3]) #last name
			temp_row.append(row[2]) #first name
			temp_row.append(row[6]) #year in school
			temp_row.append(row[10]) #1st preference
			temp_row.append(row[11]) #2nd preference
			temp_row.append(row[12]) #3rd preference 
			new_student_rows.append(temp_row)

	#Officers
	student_len = len(new_student_rows)
	officers = glob.glob("officers*.csv")

	if len(officers) > 1:
		print ("Please have only one officers file")
		return -1

	if len(officers) < 1:
		print ("Please have more than one officer file")
		return -1

	with open(officers[0], 'rb') as csvfile:
		officer_reader = csv.reader(csvfile, delimiter = ',', quotechar='|')
		for row in officer_reader:
			temp_row = []
			temp_row.append(row[1]) #last name
			temp_row.append(row[2]) #first name
			temp_row.append(row[10]) #year in school 
			temp_row.append(row[11]) #1st preference 
			temp_row.append(row[12]) #2nd preference 
			temp_row.append(row[13]) #3rd preference 
			new_student_rows.append(temp_row)

	#Write them all out 
	del new_student_rows[0]
	del new_student_rows[student_len-1]
	with open('students.csv', 'wb') as csvfile:
		student_writer = csv.writer(csvfile, delimiter=',')
		for row in new_student_rows:
			if row[0] != '' or row[1] != '':
				student_writer.writerow(row)

	#Companies 

	#Faculty
	new_faculty_rows = []

	#Vips
 	vips = glob.glob("vip*.csv")

	if len(vips) > 1:
		print ("Please have only one VIPs file")
		return -1

	if len(vips) < 1:
		print ("Please have more than one VIPs file")
		return -1

	with open(vips[0], 'rb') as csvfile:
		vips_reader = csv.reader(csvfile, delimiter = ',', quotechar='|')
		for row in vips_reader:
			temp_row = []
			if row[0] == 'Yes':
				temp_row.append(row[5]) #last name 
				temp_row.append(row[3] + ' ' + row[4]) #title + first name
				temp_row.append(row[6]) #postion 
				temp_row.append(row[7]) #deparment
				new_faculty_rows.append(temp_row)
	
	vips_len = len(new_faculty_rows)
	#DHs
 	dhs = glob.glob("dh*.csv")

	if len(dhs) > 1:
		print ("Please have only one DHs file")
		return -1

	if len(dhs) < 1:
		print ("Please have more than one DHs file")
		return -1

	with open(dhs[0], 'rb') as csvfile:
		dhs_reader = csv.reader(csvfile, delimiter = ',', quotechar='|')
		for row in dhs_reader:
			temp_row = []
			temp_row.append(row[1]) #last name 
			temp_row.append(row[0] + ' ' + row[2]) #title + first name 
			temp_row.append(row[4]) #position
			temp_row.append(row[5]) #department 
			new_faculty_rows.append(temp_row)

	#Write them all out 
	#del new_faculty_rows[0]
	del new_faculty_rows[vips_len]
	with open('faculty.csv', 'wb') as csvfile:
		faculty_writer = csv.writer(csvfile, delimiter=',')
		for row in new_faculty_rows:
			if row[0] != '' or row[1] != '':
				faculty_writer.writerow(row)

if __name__ == "__main__":
	main()
