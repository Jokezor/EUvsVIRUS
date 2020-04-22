from test_2.models import User, Passions
from datetime import datetime
import random
from collections import Counter




def get_unique_skill(passion_vec):
	passion_list=[]
	for passions in passion_vec:
		passion_list.append(passions.passion)
	passion_list=set(passion_list)

	return passion_list


def Passion_score(email):
	#Email should be used here but for now i will go with name, since users are unique by mail
	passion_vec = Collaboration.objects.filter(user__email = email)
	passion_vec=Passions.objects.filter(user__email = email)
	passion_list=get_unique_skill(passion_vec)
	matched_users=[]
	for passions in passion_list:
		matched_passions=Passions.objects.filter(passion=passions)
		for p in matched_passions:
			if p.user.email==email:
				pass
			else:
				matched_users.append(p.user.email)  #TODO: if it should be possible to weight scores..

	
	matches=Counter(matched_users)
	print(matches)

