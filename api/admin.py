from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Category, User, Skill, Lender, Has, Qualification, Applicant, Offer, Postulation])