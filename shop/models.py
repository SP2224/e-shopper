from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.html import format_html

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=50)
    address = models.CharField(max_length=30, blank=True)
    

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)                                   ###################################
def create_user_profile(sender, instance, created, **kwargs):       # Thus, we are hooking the methods
    if created:                                                     # to the User model,
        Profile.objects.create(user=instance)                       # whenever a save event occurs
                                                                    ###################################
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Product(models.Model):
    PRODUCT_CHOICES = [
        
        ('Cosmetics', (
            ('Hair Care', 'Hair Care'),
            ('Skin Care', 'Skin Care'),
            ('Beauty Care', 'Beauty Care'),
            )
        ),
        ('Digital', (
            ('E-Book', 'E-Book'),
            ('Kindle Edition', 'Kindle Edition'),
            ('Software', 'Software'),
            )
        ),
        ('Electronics', (
            ('Monitor', 'Monitor'),
            ('Mouse', 'Mouse'),
            ('Keyboard', 'Keyboard'),
            ('Headphone', 'Headphone'),
            ('Earphone', 'Earphone'),
            ('Laptop', 'Laptop'),
            ('TV', 'TV'),
            ('Pen Drive', 'Pen Drive'),
            ('Router', 'Router'),
            ('AC', 'AC'),
            ('Tablets', 'Tablets'),
            ('Camera', 'Camera'),
            )
        ),
        ('Bag', 'Bag'),
        ('Wallet', 'Wallet'),
        ('T-Shirt', 'T-Shirt'),
        ('Jeans', 'Jeans'),
        ('Wrist Watch', 'Wrist Watch'),
        ('Belt', 'Belt'),
        ('Sunglass', 'Sunglass'),
        ('Shirt', 'Shirt'),
        ('Trouser', 'Trouser'),
        ('Shorts', 'Shorts'),
        ('Book', 'Book'),
        ('None', 'None'),
    ]
            
    TYPE_CHOICES = [
        ('Wired', 'Wired'),
        ('Wireless', 'Wireless'),
        ('SLR', 'SLR'),
        ('DSLR', 'DSLR'),
        ('None', 'None'),

    ]

    FOR_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('All', 'All'),
        ('None', 'None'),
    ]

    title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    offer = models.BooleanField(default=False, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(
        choices=PRODUCT_CHOICES, 
        max_length=20,
        blank=True
    )
    sub_category = models.CharField(
        choices=TYPE_CHOICES, 
        max_length=20,
        blank=True
    )
    usable_by = models.CharField(choices=FOR_CHOICES, max_length=6, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='products', blank=True)
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def show_image(self):
        return format_html('<img src="/media/%s" width="50" />'%self.image)

    

    
