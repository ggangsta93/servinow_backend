from django.db import models
from django.contrib.auth.models import  AbstractUser, Permission
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.

#tabla usuario
 
class User(AbstractUser):
    ID_CHOICES = (
        (1, _("CEDULA")),
        (2, _("CEDULA_EXTRANJERIA")),
        (3, _("TARJETA_IDENTIDAD")),
    )
    type_id = models.IntegerField(
    verbose_name='Tipo de ID', choices=ID_CHOICES, default=1)
    #first_name = models.CharField(max_length=30, blank=False, null=False)
    #last_name = models.CharField(max_length=30, blank=False, null=False)
    personal_id = models.CharField(verbose_name='Numero de ID', max_length=24)
    personal_code = models.CharField(verbose_name='Codigo ID', max_length=24)
    gender = models.CharField(max_length=30, blank=False, null=False)
    #photo = models.FileField(verbose_name='Foto', upload_to="d_accounts_app/users/%Y/%m/%d", default="/default/default_user.png")
    telephone = models.CharField(verbose_name='Telefono', max_length=24)
    address = models.CharField(verbose_name='Direccion', max_length=64)

    class Meta:
        indexes = [
            models.Index(fields=['personal_id', 'personal_code', ]),
        ]
    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

## tabla categoria
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    category = models.ForeignKey(
    Category, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name

class Lender(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    class Meta:
        verbose_name = 'lender'
        verbose_name_plural = 'lenders'

    def __str__(self):
        return "{}".format(self.user)

class Has(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=False, null=True)
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, blank=False, null=True)
    
    class Meta:
        verbose_name = 'has'
        verbose_name_plural = 'has'

    def __str__(self):
        return self.skill + ' ' + self.lender

class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        verbose_name = 'applicant'
        verbose_name_plural = 'applicants'

    def __str__(self):
        return "{}".format(self.user)

class Qualification(models.Model):
    score_ap_to_le = models.CharField(max_length=30, blank=False, null=False)
    comment_ap_to_le =  models.CharField(max_length=30, blank=False, null=False)
    score_le_to_ap = models.CharField(max_length=30, blank=False, null=False)
    comment_le_to_ap =  models.CharField(max_length=30, blank=False, null=False)
  
    class Meta:
        verbose_name = 'qualification'
        verbose_name_plural = 'qualifications'

    def __str__(self):
        return self.score_ap_to_le + ' ' + self.score_le_to_ap

    
class Offer(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, blank=False, null=True)
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, blank=False, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=30, blank=False, null=False)
    price = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=30, blank=False, null=False)
    status = models.CharField(max_length=30, blank=False, null=False)
    date_start = models.DateField()
    date_end = models.DateField()
    
    class Meta:
        verbose_name = 'offer'
        verbose_name_plural = 'offers'

    def __str__(self):
        return self.title

class Postulation(models.Model):
    lender = models.ForeignKey(Lender, on_delete=models.CASCADE, blank=False, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=False, null=True)
  
    class Meta:
        verbose_name = 'postulation'
        verbose_name_plural = 'postulations'

    def __str__(self):
        #return  "{} {}".format(self.lender,self.offer)
        return '' 
