#from test_2.models import City, User, Passions, Assigned_Skills, Business_Experience, Up_For, Collaboration, Colab_Passions, Colab_Assigned_Skills, Colab_Business_Experience, Colab_Up_For, Skills
from test_2.models import *
from datetime import datetime
import random
from collections import Counter


# Score for passions
def passion_score(W, colabs, users):
	
	for colab in colabs:

		colab_passion_list = []		
		
		for colab_passion in colab.colab_passions_set.all():
			colab_passion_list.append(colab_passion.passion.skill)

		for usr in users:
			matched = 0

			for user_passion in usr.passions_set.all():

				if user_passion.passion.skill in colab_passion_list:
					matched+=1

			ratio_matched = matched/len(colab_passion_list)
			score = W*ratio_matched

			if not Passion_Matched.objects.filter(user=usr, colab=colab).exists():
				Passion_Matched.objects.create(user=usr, colab=colab, score=score, weight=W)

# Score for assigned_skills
def assigned_skills_score(W, colabs, users):

	for colab in colabs:

		colab_assigned_skills_list = []		
		
		for colab_assigned_skill in colab.colab_assigned_skills_set.all():
			colab_assigned_skills_list.append(colab_assigned_skill.assigned_skill.skill)

		for usr in users:
			matched = 0

			for user_assigned_skill in usr.assigned_skills_set.all():

				if user_assigned_skill.assigned_skill.skill in colab_assigned_skills_list:
					matched+=1

			ratio_matched = matched/len(colab_assigned_skills_list)
			score = W*ratio_matched

			if not Assigned_Skills_Matched.objects.filter(user=usr, colab=colab).exists():
				Assigned_Skills_Matched.objects.create(user=usr, colab=colab, score=score, weight=W)

# Score for business experience
def business_experience_score(W, colabs, users):

	for colab in colabs:

		colab_business_experience_list = []		
		
		for colab_business_experience in colab.colab_business_experience_set.all():
			colab_business_experience_list.append(colab_business_experience.experience.skill)

		for usr in users:
			matched = 0

			for user_business_experience in usr.business_experience_set.all():

				if user_business_experience.experience.skill in colab_business_experience_list:
					matched+=1

			ratio_matched = matched/len(colab_business_experience_list)
			score = W*ratio_matched
			if not Business_Experience_Matched.objects.filter(user=usr, colab=colab).exists():
				Business_Experience_Matched.objects.create(user=usr, colab=colab, score=score, weight=W)
		
# Score for business experience
def up_for_score(W, colabs, users):

	for colab in colabs:

		colab_up_for_list = []		
		
		for colab_up_for in colab.colab_up_for_set.all():
			colab_up_for_list.append(colab_up_for.interest.skill)

		for usr in users:
			matched = 0

			for user_up_for in usr.up_for_set.all():

				if user_up_for.interest.skill in colab_up_for_list:
					matched+=1

			ratio_matched = matched/len(colab_up_for_list)
			score = W*ratio_matched

			if not Up_For_Matched.objects.filter(user=usr, colab=colab).exists():
				Up_For_Matched.objects.create(user=usr, colab=colab, score=score, weight=W)

#def total_score(colabs):
#	for colab in colabs:


# Scoring mechanism for collaborations to users
def score():
	# Weights for the different fields. Ideally a user can adjust with slider in the future.
	W = {'Passion': 100, 'Assigned_Skills': 100, 'Business_Experience': 100, 'Up_For': 100}

	# Enables not running all colabs if we only want to run for some colabs.
	colabs = Collaboration.objects.all()

	# Same for users
	users = User.objects.filter(want_to_be_matched = 1, is_staff = False)


	passion_score(W['Passion'], colabs, users)
	assigned_skills_score(W['Assigned_Skills'], colabs, users)
	business_experience_score(W['Business_Experience'], colabs, users)
	up_for_score(W['Up_For'], colabs, users)

	# check all scores




