from django.db import models

class BankingDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    holder_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    bank_branch = models.CharField(max_length=255)
    bank_number = models.IntegerField()
    swift_code = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Representative(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id = models.AutoField(primary_key=True)
    bank_account = models.ForeignKey(BankingDetail, on_delete=models.CASCADE, related_name='representatives')
    avatar = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    tel = models.IntegerField()
    email = models.EmailField(max_length=255)
    position = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    bank_account = models.ForeignKey(BankingDetail, on_delete=models.CASCADE, related_name='suppliers')
    avatar = models.CharField(max_length=255, blank=True, null=True)
    representative_id =  models.ForeignKey(Representative, on_delete=models.CASCADE, related_name='suppliers')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tel = models.IntegerField()
    email = models.EmailField(max_length=255)
    tax_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
