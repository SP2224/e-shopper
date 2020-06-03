from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class OurUserProfileManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, name, mobile_no, username, email, password, **extra_fields):
        if not name:
            raise ValueError("User must have a name.")
        elif not mobile_no:
            raise ValueError("User must have a mobile number.")
        elif not username:
            raise ValueError("User must use a username.")
        elif not email:
            raise ValueError("User must have an email address.")
        elif not password:
            raise ValueError("User must use password.")
        email = self.normalize_email(email)
        user = self.model(name=name, username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, mobile_no, username, email, password, **extra_fields):
        user = self.create_user(email, mobile_no, username, name, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user     

class OurUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    mobile_no = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = OurUserProfileManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['name', 'email', 'password', 'mobile_no']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name




class Product(models.Model):
    PRODUCT_CHOICES = [
        
        ('Cosmetics', 'Cosmetics'),
        ('Digital', 'Digital'),
        ('Electronics', 'Electronics'),
        ('Bag', 'Bag'),
        ('Wallet', 'Wallet'),
        ('T-Shirt', 'T-Shirt'),
        ('Jeans', 'Jeans'),
        ('Wrist-Watch', 'Wrist Watch'),
        ('Belt', 'Belt'),
        ('Sunglass', 'Sunglass'),
        ('Shirt', 'Shirt'),
        ('Trouser', 'Trouser'),
        ('Shorts', 'Shorts'),
        ('Book', 'Book'),
        ('None', 'None'),
    ]

    
    TYPE_CHOICES = [
            ('Hair-Care', 'Hair Care'),
            ('Skin-Care', 'Skin Care'),
            ('Beauty-Care', 'Beauty Care'),
            ('Health-Care', 'Health Care'),
            ('Wireless', 'Wireless'),
            ('Wired', 'Wired'),
            ('SLR', 'SLR'),
            ('DSLR', 'DSLR'),
            ('None', 'None')
    ]

    
    SUBPRODUCT_CHOICES = [
            ('E-Book', 'E-Book'),
            ('Kindle-Edition', 'Kindle Edition'),
            ('Software', 'Software'),
            ('None', 'None'),
            ('Monitor', 'Monitor'),
            ('Mouse', 'Mouse'),
            ('Keyboard', 'Keyboard'),
            ('Headphone', 'Headphone'),
            ('Earphone', 'Earphone'),
            ('Laptop', 'Laptop'),
            ('TV', 'TV'),
            ('Pen-Drive', 'Pen Drive'),
            ('Router', 'Router'),
            ('AC', 'AC'),
            ('Tablets', 'Tablets'),
            ('Camera', 'Camera'),
            ('None', 'None')
    ]

    FOR_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('None', 'None'),
    ]

    title = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(choices=PRODUCT_CHOICES, max_length=20, default=None)
    sub_category = models.CharField(choices=SUBPRODUCT_CHOICES, max_length=15, default=None)
    category_type = models.CharField(choices=TYPE_CHOICES, max_length=12, default=None)
    usable_by = models.CharField(choices=FOR_CHOICES, max_length=6, default=None)
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='products', blank=True)
    added_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title