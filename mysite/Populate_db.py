from test_2.models import City, User, Passions, Assigned_Skills, Business_Experience, Up_For, Collaboration, Colab_Passions, Colab_Assigned_Skills, Colab_Business_Experience, Colab_Up_For, Skills
from datetime import datetime
import random
from collections import Counter
import csv
import json

# Base path where we have the files
base_path = ''

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

		if want_to_be_matched==1:
			User.objects.create(email = email, password = passwrd, first_name = first_name, last_name = last_name, Collaborator = True)
		else:
			User.objects.create(email = email, password = passwrd, first_name = first_name, last_name = last_name, Ideamaker = True)


def populate_passions(M):
	users = User.objects.filter(Collaborator = True, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.passions_set.all()) < random.randint(1, M)):
			passion = skills_db[random.randint(0,len(skills_db)-1)]
			Passions.objects.create(user=usr, passion=passion)

def populate_assigned_skills(M):
	users = User.objects.filter(Collaborator = True, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.assigned_skills_set.all()) < random.randint(1, M)):
			Assigned_Skill = skills_db[random.randint(0,len(skills_db)-1)]
			Assigned_Skills.objects.create(user=usr, assigned_skill=Assigned_Skill)

def populate_business_experience(M):
	users = User.objects.filter(Collaborator = True, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.business_experience_set.all()) < random.randint(1, M)):
			experience = skills_db[random.randint(0,len(skills_db)-1)]
			Business_Experience.objects.create(user=usr, experience=experience)

def populate_up_for(M):
	users = User.objects.filter(Collaborator = True, is_staff = False)
	skills_db = Skills.objects.all()

	for usr in users:

		while (len(usr.up_for_set.all()) < random.randint(1, M)):
			interest = skills_db[random.randint(0,len(skills_db)-1)]
			Up_For.objects.create(user=usr, interest=interest)


# Fill data for collaborators
def populate_collaborator_fields(M):
	populate_passions(M)
	populate_assigned_skills(M)
	populate_business_experience(M)
	populate_up_for(M)

# create collaborations
def populate_mockup_collaboration(cities, colab_data):

	colab_users = User.objects.filter(Ideamaker = True, is_staff = False)

	colabs = [] 

	for ind in range(0, len(colab_data)):

		usr_not_checked = 1
		while(usr_not_checked):
			temp_usr = colab_users[random.randint(0,len(colab_users)-1)]

			if temp_usr not in colabs:
				colabs.append(temp_usr)
				usr_not_checked = 0

	for ind, usr in enumerate(colabs):
		title = list(colab_data.keys())[ind]
		description = colab_data[title]['description']
		city = cities[random.randint(0,len(cities)-1)]
		Collaboration.objects.create(user = usr, title = title, description = description, city = city)




def populate_fields_collaboration(M):
	populate_colab_assigned_skills(M)
	populate_colab_passions(M)
	populate_colab_business_experience(M)
	populate_colab_up_for(M)

# collaborations assigned skills
def populate_colab_assigned_skills(M):
	colabs = Collaboration.objects.all()
	skills_db = Skills.objects.all()

	for colab in colabs:
		while (len(colab.colab_assigned_skills_set.all()) < random.randint(1, M)):
			assigned_skill = skills_db[random.randint(0,len(skills_db)-1)]
			Colab_Assigned_Skills.objects.create(colab=colab, assigned_skill=assigned_skill)

# Collaboration passions
def populate_colab_passions(M):
	colabs = Collaboration.objects.all()
	skills_db = Skills.objects.all()

	for colab in colabs:
		while (len(colab.colab_passions_set.all()) < random.randint(1, M)):
			passion = skills_db[random.randint(0,len(skills_db)-1)]
			Colab_Passions.objects.create(colab=colab, passion=passion)

# collaborations business experience
def populate_colab_business_experience(M):
	colabs = Collaboration.objects.all()
	skills_db = Skills.objects.all()

	for colab in colabs:
		while (len(colab.colab_business_experience_set.all()) < random.randint(1, M)):
			experience = skills_db[random.randint(0,len(skills_db)-1)]
			Colab_Business_Experience.objects.create(colab=colab, experience=experience)

# collaborations business experience
def populate_colab_up_for(M):
	colabs = Collaboration.objects.all()
	skills_db = Skills.objects.all()

	for colab in colabs:
		while (len(colab.colab_up_for_set.all()) < random.randint(1, M)):
			interest = skills_db[random.randint(0,len(skills_db)-1)]
			Colab_Up_For.objects.create(colab=colab, interest=interest)






'''
def populate_Collaboration(C, ratio_colabs, cities, colab_data):

	colab_users = User.objects.filter(want_to_be_matched = 0, is_staff = False)

	checked_users = []

	# max users who will be colabs
	max_users = ratio_colabs*len(colab_users)

	for ind in range(0, max_users):

		usr_not_checked = 1
		while(usr_not_checked):
			temp_usr = colab_users[random.randint(0,len(colab_users))]

			if temp_usr not in checked_users:
				checked_users.append(temp_usr)
				usr_not_checked = 0

		
	
	for usr in checked_users:
		#title = 
		#Collaboration.objects.create(user = usr, )

'''	


def populate():

	skills = read_file('skills_test.txt')
	first_names = read_file('first_names.all.txt')
	last_names = read_file('last_names.all.txt')
	cities = read_csv('world-cities.csv')
	with open('titles.json') as f:
	    colab_data = json.load(f)
	colab_data = colab_data['titles']
	
	# First check so all skills are in db.
	#print("heeewyeyweyweywaeywyeaw")

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
	populate_collaborator_fields(M)

	# Create collaborations
	populate_mockup_collaboration(cities, colab_data)
	
	# populate all the data needed from collaborations to be matched
	populate_fields_collaboration(M)



	
	
	


		
		
	
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
	
	
	


