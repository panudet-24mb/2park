from django.db import models
import uuid
import datetime
# Create your models here.

class Device_type(models.Model):
    device_type_id = models.AutoField(primary_key=True)
    device_type_name =  models.CharField(max_length=100, blank=True, null=True , default=None)
    class Meta:
        db_table = "device_type"
    def __str__(self):
        return str(self.device_type_name)
class Device_model(models.Model):
    device_model_id = models.AutoField(primary_key=True) 
    device_model_name =   models.CharField( blank=True, null=True , default=None,max_length=100,)
    class Meta:
        db_table = "device_model"
    def __str__(self):
        return str(self.device_model_name)

class Device(models.Model):
  device_id = models.AutoField(primary_key=True)
  device_uuid = models.UUIDField(
         default=uuid.uuid4, editable=False ,unique = True
    ) 
  device_type = models.ForeignKey( Device_type , on_delete=models.CASCADE)
  device_model = models.ForeignKey( Device_model , on_delete=models.CASCADE)
  device_name = models.CharField(max_length=100, blank=True, null=True)
  class Meta:
      db_table = "device"
  def __str__(self):
      return str(self.device_name)
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_public_id = models.UUIDField(
         default=uuid.uuid4, editable=False ,unique = True
    )
    company_name = models.CharField(max_length=180, blank=True, null=True)
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

class Car_brand(models.Model):
    car_brand_id = models.AutoField(primary_key=True)
    car_brand_name = models.CharField(max_length=80, blank=True, null=True)
    class Meta:
        db_table = "car_brand"
    def __str__(self):
        return str(self.car_brand_name)
class Car_type(models.Model):
    car_type_id =  models.AutoField(primary_key=True)
    car_type_name = models.CharField(max_length=80, blank=True, null=True)
    class Meta:
        db_table = "car_type"
    def __str__(self):
        return str(self.car_type_name)
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_public_id =  models.UUIDField(
         default=uuid.uuid4, editable=False
    )
    car_brand = models.ForeignKey(Car_brand, models.CASCADE)
    car_type = models.ForeignKey(Car_type, models.CASCADE)
    car_license_plate = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
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
    event_public_id =  models.UUIDField(
         default=uuid.uuid4, editable=False
    )
    event_license_plate = models.CharField(max_length=100, blank=True, null=True )
    timestamp = models.DateTimeField( default=datetime.datetime.now)
    class Meta :
        db_table = "event"
    def __str__(self):
        return str(self.event_name)