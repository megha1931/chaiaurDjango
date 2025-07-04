from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('BL', 'BLACK'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image =models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    def __str__(self):
        return self.name
    
#one to many
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE , related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


#many to many
class Store (models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')
    image = models.ImageField(upload_to='stores/', null=True, blank=True)

    def __str__(self):
        return self.name

#one to one
class StoreOwner(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE, related_name='storeowner')
    owner = models.ForeignKey(User, on_delete=models.CASCADE )
    contact_number = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.owner.username



