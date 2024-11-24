import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from supplier.models import BankingDetail
from django.contrib.auth.hashers import make_password

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.role_name


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.permission_name


class Entity(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.entity_name


class RolePermission(models.Model):
    
    role = models.ForeignKey(Role, related_name='role_permissions', on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, related_name='role_permissions', on_delete=models.CASCADE)

    # Specific permissions
    view = models.BooleanField(default=False)
    create = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    full_access = models.BooleanField(default=False)

    class Meta:
        unique_together = ('role', 'entity')

class Employees(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.CharField(max_length=255)
    isDeleted = models.BooleanField(default=False)
    avatar = models.CharField(max_length=255)
    tel = models.CharField(max_length=50)
    role = models.ForeignKey('Role', related_name='employees', on_delete=models.CASCADE,null=True, blank=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']
    class Meta:
        db_table = 'db_diy_employees'

    def __str__(self):
        return self.email
    

class Clients(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    id = models.AutoField(primary_key=True)
    bank_account = models.ForeignKey(BankingDetail, on_delete=models.CASCADE, related_name='clients', null=True, blank=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tel = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    isDelete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        from django.contrib.auth.hashers import check_password
        return check_password(password, self.password)

    def __str__(self):
        return self.name
    def __str__(self):
        return self.name
