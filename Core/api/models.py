from django.db import models
import uuid
import datetime
# Create your models here.

class Device(models.Model):
  device_id = models.AutoField(primary_key=True)
  device_uuid = models.UUIDField(
         default=uuid.uuid4, editable=False ,unique = True
    ) 
  device_type = models.CharField(max_length=100, blank=True, null=True , unique =True)
  device_model = models.CharField(max_length=100, blank=True, null=True , unique =True)
  device_name = models.CharField(max_length=100, blank=True, null=True , unique =True)
  class Meta:
      db_table = "device"
  def __str__(self):
      return str(self.device_name)
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_public_id = models.UUIDField(
         default=uuid.uuid4, editable=False ,unique = True
    )
    company_name = models.CharField(max_length=180, blank=True, null=True , unique =True)
    company_is_active = models.BooleanField(default=False)
    created_on = models.DateField( default=datetime.datetime.now)
    class Meta:
        db_table = "company"
    def __str__(self):
        return self.company_name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_public_id =  models.UUIDField(
         default=uuid.uuid4, editable=False
    )
    company = models.ForeignKey(Company, models.CASCADE)
    admin_username = models.CharField(max_length=100, unique=True , blank=False, null=False )
    admin_password = models.CharField(max_length=80, blank=True, null=True)
    admin_is_active = models.BooleanField(default=False)
    class Meta:
        db_table = "admin"
    def __str__(self):
        return str(self.admin_public_id)
class Car(models.Model):
  car_id = models.AutoField(primary_key=True)
  car_name = models.CharField(max_length=100, blank=True, null=True )
  car_license_plate = models.CharField(max_length=100, blank=True, null=True )
  class Meta:
      db_table = "car"
  def __str__(self):
      return str(self.car_license_plate)
class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  user_firstname = models.CharField(max_length=100, blank=True, null=True )
  user_lastname = models.CharField(max_length=100, blank=True, null=True )
  user_mobile = models.CharField(max_length=100, blank=True, null=True )
  user_citizen_id = models.CharField(max_length=100, blank=True, null=True )
  class Meta:
      db_table = "user"
  def __str__(self):
      return str(self.user_firstname)
class User_has_car (models.Model):
  user_has_car_id = models.AutoField(primary_key=True)
  car = models.ForeignKey(Car, models.CASCADE)
  user = models.ForeignKey(User, models.CASCADE)
  class Meta:
      db_table = "user_has_car"
  def __str__(self):
      return str(self.user_has_car_id)
class Event(models.Model):
  event_id = models.AutoField(primary_key=True)
  event_name = models.CharField(max_length=100, blank=True, null=True )
  car = models.ForeignKey(Car, models.CASCADE)
  user = models.ForeignKey(User, models.CASCADE)
  timestamp = models.DateTimeField( default=datetime.datetime.now)
  class Meta :
    db_table = "event"
  def __str__(self):
    return str(self.event_name)