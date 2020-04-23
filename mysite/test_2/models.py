from django.db import models
#from django.contrib.gis.db import models as gis_models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import MyUserManager

class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'cities'
        

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True, null=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	location = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

	want_to_be_matched = models.IntegerField(default=0)

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this site.'),
	)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
		    'Designates whether this user should be treated as active. '
		    'Unselect this instead of deleting accounts.'
	),
	)
	USERNAME_FIELD = 'email'
	objects = MyUserManager()
	def __str__(self):
		return self.email
	def get_full_name(self):
		return self.email
	def get_short_name(self):
		return self.email


class Skills(models.Model):
	skill = models.CharField(max_length=200)
	group = models.CharField(max_length=200, default='None')


class Passions(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	passion = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	passion_free_text = models.CharField(max_length=200, default='None')
	
class Assigned_Skills(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	assigned_skill = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	assigned_skill_free_text = models.CharField(max_length=200, default='None')

class Business_Experience(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	experience = models.ForeignKey(Skills, on_delete=models.CASCADE)
	experience_free_text = models.CharField(max_length=200, default='None')

class Up_For(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	interest = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	interest_free_text = models.CharField(max_length=200, default='None')

class Collaboration(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	# Basic no limit
	description = models.TextField()
	city = models.CharField(max_length=200)
	#location = gis_models.PointField()

class Colab_Passions(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	passion = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	passion_free_text = models.CharField(max_length=200, default='None')
	
class Colab_Assigned_Skills(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	assigned_skill = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	assigned_skill_free_text = models.CharField(max_length=200, default='None')

class Colab_Business_Experience(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	experience = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	experience_free_text = models.CharField(max_length=200, default='None')

class Colab_Up_For(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	interest = models.ForeignKey(Skills, on_delete=models.CASCADE, default='None')
	interest_free_text = models.CharField(max_length=200, default='None')

class Matched(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)






