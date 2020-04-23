from django.shortcuts import render
from .models import User, Passions
from django.http import HttpResponse
from django.template import loader


def index(request):
	#tests = Test.objects.count()
	template = loader.get_template('index.html')
	#user=User.objects.all()
	#passion=Passions.objects.all()
	context = {'user': 'joakim'}
	#context = {
	#    'user': user, 
	#    'passion': passion,
	#}
	#print(user[0])
	#for p in user:
	#	print(p.passions_set.all())
	return HttpResponse(template.render(context, request))

def test_view_2(request):

	template = loader.get_template('test_view_2.html')
	context = {}
	
	return HttpResponse(template.render(context, request))


def test_view(request):
    #tests = Test.objects.count()
    tests = 0
    return HttpResponse("Det finns {} tests.".format(tests))
# Create your views here.
