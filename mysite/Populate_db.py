from test_2.models import *
from datetime import datetime
import random
from collections import Counter
import csv

# Base path where we have the files
base_path = '/Users/jo/Documents/Our-Connected-Future/mysite/'

def read_csv(file):
	full_path = base_path + file
	with open(file) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0

	    lines = [row[0] for row in csv_reader]
	    return lines


def read_file(file):
	full_path = base_path + file
	with open(full_path) as f:
		lines = [line.rstrip() for line in f]
	return lines

def populate_skills(skills):
	skills_db = Skills.objects.all().values_list('skill', flat=True)

	for skill in skills:
		if skill not in skills_db:
			Skills.objects.create(skill=skill)

def populate_users(N, first_names, last_names, cities, ratio_match):

	# Check newly added emails
	checked_emails = {}

	# Check existing emails
	emails = User.objects.all().values_list('email', flat=True)

	for i in range(0, N):

		get_name = 1

		city = cities[random.randint(0,len(cities)-1)]

		# maximum float that will us the correct ratio of matches
		max_rand = (0.5*ratio_match+0.5)
		want_to_be_matched = round(random.uniform(0,max_rand))
		passwrd = 1234

		while(get_name):
			first_name = first_names[random.randint(0,len(first_names)-1)]
			last_name = last_names[random.randint(0,len(last_names)-1)]
			full_name = first_name+last_name

			email = full_name + str(random.randint(0,999999)) + '@gmail.com'

			if email not in checked_emails and email not in emails:
				checked_emails[email] = 1
				get_name = 0

		User.objects.create(email = email, password = passwrd, first_name = first_name, last_name = last_name, city = city, want_to_be_matched = want_to_be_matched)

def populate_Passions(M):
	users = User.objects.filter(want_to_be_matched = 1, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.passions_set.all()) < random.randint(1, M)):
			passion = skills_db[random.randint(0,len(skills_db)-1)]
			Passions.objects.create(user=usr, passion=passion)

def populate_Assigned_Skills(M):
	users = User.objects.filter(want_to_be_matched = 1, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.assigned_skills_set.all()) < random.randint(1, M)):
			Assigned_Skill = skills_db[random.randint(0,len(skills_db)-1)]
			Assigned_Skills.objects.create(user=usr, assigned_skill=Assigned_Skill)

def populate_Business_Experience(M):
	users = User.objects.filter(want_to_be_matched = 1, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.business_experience_set.all()) < random.randint(1, M)):
			experience = skills_db[random.randint(0,len(skills_db)-1)]
			Business_Experience.objects.create(user=usr, experience=experience)

def populate_Up_For(M):
	users = User.objects.filter(want_to_be_matched = 1, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.up_for_set.all()) < random.randint(1, M)):
			interest = skills_db[random.randint(0,len(skills_db)-1)]
			Up_For.objects.create(user=usr, interest=interest)


def populate_Collaboration(C, ratio_colabs, cities):
	users = User.objects.filter(want_to_be_matched = 0, is_staff = False)

	checked_users = {}

	# max users who will be colabs
	max_users = ratio_colabs*len(users)

	colab_users = []

	for ind in range(0, max_users):
		temp_usr = users[random.randint(0,len(users))]
		checked_users[temp_usr] = 1

		colab_users.append(temp_usr)
	
	#for usr in colab_users:

		#Collaboration.objects.create(user = usr, )

		


def populate():

	skills = read_file('skills_new.txt')
	first_names = read_file('first_names.all.txt')
	last_names = read_file('last_names.all.txt')
	cities = read_csv('world-cities.csv')
		
	# First check so all skills are in db.
	
	populate_skills(skills)

	# Number of candidates to generate
	N = 100
	
	# max number of skills, passions etc allowed for users.
	M = 10

	# Ratio of skilled people that want to be matched
	ratio_match = 0.9

	# ratio idea makers/idle users that leaves us with (around 0.08 that will be idea makers and 0.02 aren't active of the total users)
	ratio_colabs = 0.8

	# Create N users
	populate_users(N, first_names, last_names, cities, ratio_match)

	# populate all the data needed from people who want to be matched
	populate_Passions(M)
	populate_Assigned_Skills(M)
	populate_Business_Experience(M)
	populate_Up_For(M)

	# Create collaborations
	#populate_Collaboration(ratio_colabs, cities)

	# populate all the data needed from collaborations to be matched

	# Number of collaborations to generate
	#C = 5
	#for i in range(0, N):
	#	Collaboration.objects.create(user = usr, title =)
		
		
	
	'''
		passwrd = 1234
		User.objects.create(email = email, password = passwrd, first_name = person)
		usr = User.objects.get(email = email)
		ind=random.randint(0,len(skills))
		passion_temp=skills[ind]
		Passions.objects.create(user=usr, passion=passion_temp)


	for i, person in enumerate(ppl):
		email = 'hej{}@mail.com'.format(datetime.now())
		passwrd = 1234
		User.objects.create(email = email, password = passwrd, first_name = person)
		usr = User.objects.get(email = email)
		ind=random.randint(0,len(skills))
		passion_temp=skills[ind]
		Passions.objects.create(user=usr, passion=passion_temp)
	
	'''
	#User.objects.all()
	#User.objects.filter()
	#
	#Passions.objects.filter(user=usr)
	#Collaboration = Collaboration.objects.get(id=2)
	#Collaboration.colab_passions_set.all()
	#+usr = User.objects.get(name = 'bengt')
	#print(Passions.objects.filter(user__first_name = 'bengt'))
	#print(User.objects.filter(user__first_name = 'bengt'))
	#Collaboration.object()
	#Collaborations.objects.filter()





		#matches[names]=


	#thisdict = {
 # "brand": "Ford",
 # "model": "Mustang",
 # "year": 1964
#}
#thisdict["color"] = "red"
#print(thisdict)

	#print(set(matched_users))
	
	
	


