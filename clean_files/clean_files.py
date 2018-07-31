import glob 
import csv 

def check_major(row):
	row = row.strip()
	new_row = row 
	if row == "Chemical Engineering and Biological" or row == "Chemical Engineering and Biological Engineering" or row == "Chemical and Biological Engineering Department":
		new_row = "CE"
	elif row == "Chemistry and Geochemistry" or row == "Chemistry and Geochemistry Department":
		new_row = "CH"
	elif row == "Computer Science" or row == "Computer Science Division":
		new_row = "CS"
	elif row == "Electrical Engineering" or row == "Electrical Engineering Division":
		new_row = "EE"
	elif row == "Economics and Business" or row == "Economics and Business Division":
		new_row = "EB"
	elif row == "Civil and Environmental Engineering" or row == "Civil and Environmental Engineering Department" or row == "Civil & Environmental Engineering":
		new_row = "CEE"
	elif row == "Geology and Geological Engineering" or row == "Geology and Geological Engineering Department":
		new_row = "GE"
	elif row == "Geophysics" or row == "Geophysics Department":
		new_row = "GP"
	elif row == "Mechanical Engineering" or row == "Mechanical Engineering Department": 
		new_row = "ME"
	elif row == "Mathematics and Statistics" or row == "Mathematics & Statistics" or row == "Applied Mathematics and Statistics Department": 
		new_row = "AMS"
	elif row == "Metallurgical and Materials Science" or row == "Metallurgical and Materials Engineering Department":
		new_row = "MME"
	elif row == "Mining Engineering" or row == "Mining" or row == "Mining Engineering Department":
		new_row = "MN"
	elif row == "Petroleum Engineering" or row == "Petroleum" or row == "Petroleum Engineering Department":
		new_row = "PE"
	elif row == "Physics" or row == "Physics Department":
		new_row = "PH"
	elif row == "Any Major" or row == "any major" or row == "Humanities, Arts and Social Sciences Division":
		new_row = "ANY"
	return new_row

def names(full_name):
	names_arr = []
	full_name_split = full_name.split(' ')
	#TODO: handle not two names people 
	last = full_name_split[-1]
	first = full_name_split[0]
	return last, first

def check_year(year):
	year = year.strip()
	num_year = year
	if year == "Freshman":
		num_year = 1
	elif year == "Sophomore":
		num_year = 2
	elif year == "Junior":
		num_year = 3
	elif year == "Senior":
		num_year = 4
	elif year == "Graduate Student" or year == "Grad Student":
		num_year = 5

	return num_year 	

def main():
	students = glob.glob("../../test_files/students*.csv")

	#Students 
	if len(students) > 1:
		print ("Please have only one student file")
		return -1

	if len(students) < 1:
		print ("Please have more than one student file")
		return -1

	new_student_rows = []
	with open(students[0], 'rb') as csvfile:
		student_reader = csv.reader(csvfile)
		for row in student_reader:
			temp_row = []
			temp_row.append(row[3]) #last name
			temp_row.append(row[2]) #first name
			temp_row.append(check_year(row[6])) #year in school
			temp_row.append(check_major(row[10])) #1st preference
			temp_row.append(check_major(row[11])) #2nd preference
			temp_row.append(check_major(row[12])) #3rd preference 
			new_student_rows.append(temp_row)

	#Officers
	student_len = len(new_student_rows)
	officers = glob.glob("../../test_files/officers*.csv")

	if len(officers) > 1:
		print ("Please have only one officers file")
		return -1

	if len(officers) < 1:
		print ("Please have more than one officer file")
		return -1

	with open(officers[0], 'rb') as csvfile:
		officer_reader = csv.reader(csvfile)
		for row in officer_reader:
			temp_row = []
			temp_row.append(row[1]) #last name
			temp_row.append(row[2]) #first name
			temp_row.append(check_year(row[10])) #year in school 
			temp_row.append(check_major(row[11])) #1st preference 
			temp_row.append(check_major(row[12])) #2nd preference 
			temp_row.append(check_major(row[13])) #3rd preference 
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
	new_rec_rows = []
	rec = glob.glob("../../test_files/recruiter*.csv")
	
	if len(rec) > 1:
		print ("Please have only one recruiters file")
		return -1

	if len(rec) < 1:
		print ("Please have more than one recruiters file")
		return -1

	with open(rec[0], 'rb') as csvfile:
		rec_reader = csv.reader(csvfile)
		for row in rec_reader:
			company = row[10] #company
			major_1 = check_major(row[16]) #preference 1
			major_2 = check_major(row[17]) #preference 2
			major_3 = check_major(row[18]) #preference 3
			num_reps = row[21][0].strip()
			if num_reps != 'N':
				num_to_go_to = int(num_reps)*3 + 23
				curr_num = 23
				while curr_num <= num_to_go_to:
					temp_row = []
					last,first = names(row[curr_num])
					temp_row.append(last) #last name 
					temp_row.append(first) #first name 
					temp_row.append(row[curr_num+1]) #title 
					temp_row.append(company) #company 
					temp_row.append(major_1) #preference 1
					temp_row.append(major_2) #preference 2
					temp_row.append(major_3) #preference 3
					curr_num += 4
					new_rec_rows.append(temp_row)
					

	del new_rec_rows[0]
	with open('recruiters.csv', 'wb') as csvfile:
		recruiter_writer = csv.writer(csvfile, delimiter=',')
		for row in new_rec_rows:
			if row[0] != '' or row[1] != '':
				recruiter_writer.writerow(row)


	#Faculty
	new_faculty_rows = []
	fac = glob.glob("../../test_files/faculty*.csv")
	
	if len(fac) > 1:
		print ("Please have only one faculty file")
		return -1

	if len(fac) < 1:
		print ("Please have more than one faculty file")
		return -1

	with open(fac[0], 'rb') as csvfile:
		fac_reader = csv.reader(csvfile)
		for row in fac_reader:
			temp_row = []
			temp_major = check_major(row[8])
			num_reps = row[9][0].strip()
			if num_reps != 'N':
				num_to_go_to = int(num_reps)*3 + 10
				curr_num = 10
				while curr_num < num_to_go_to:
					temp_row = []
					last,first = names(row[curr_num])
					temp_row.append(last) #last name 
					temp_row.append(first) #first name 
					temp_row.append(row[curr_num+1]) #title 
					temp_row.append(check_major(temp_major)) #major 
					curr_num += 3
					new_faculty_rows.append(temp_row)
	
	fac_len = len(new_faculty_rows)

	#Vips
 	vips = glob.glob("../../test_files/vip*.csv")

	if len(vips) > 1:
		print ("Please have only one VIPs file")
		return -1

	if len(vips) < 1:
		print ("Please have more than one VIPs file")
		return -1

	with open(vips[0], 'rb') as csvfile:
		vips_reader = csv.reader(csvfile)
		for row in vips_reader:
			temp_row = []
			if row[0] == 'Yes':
				temp_row.append(row[5]) #last name 
				temp_row.append(row[3] + ' ' + row[4]) #title + first name
				temp_row.append(row[6]) #postion 
				temp_row.append(check_major(row[7])) #deparment
				new_faculty_rows.append(temp_row)
	
	vips_len = len(new_faculty_rows)
	#DHs
 	dhs = glob.glob("../../test_files/dh*.csv")

	if len(dhs) > 1:
		print ("Please have only one DHs file")
		return -1

	if len(dhs) < 1:
		print ("Please have more than one DHs file")
		return -1

	with open(dhs[0], 'rb') as csvfile:
		dhs_reader = csv.reader(csvfile)
		for row in dhs_reader:
			if row[0] == 'Yes':
				temp_row = []
				temp_row.append(row[2]) #last name 
				temp_row.append(row[1] + ' ' + row[3]) #title + first name 
				temp_row.append(row[5]) #position
				temp_row.append(check_major(row[6])) #department 
				new_faculty_rows.append(temp_row)

	#Write them all out 
	del new_faculty_rows[0]
	del new_faculty_rows[vips_len]
	with open('faculty.csv', 'wb') as csvfile:
		faculty_writer = csv.writer(csvfile, delimiter=',')
		for row in new_faculty_rows:
			if row[0] != '' or row[1] != '':
				faculty_writer.writerow(row)

if __name__ == "__main__":
	main()
