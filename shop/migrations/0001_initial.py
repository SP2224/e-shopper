# Generated by Django 3.0.4 on 2020-06-05 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8)),
                ('offer', models.BooleanField(default=False, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('Cosmetics', (('Hair Care', 'Hair Care'), ('Skin Care', 'Skin Care'), ('Beauty Care', 'Beauty Care'))), ('Digital', (('E-Book', 'E-Book'), ('Kindle Edition', 'Kindle Edition'), ('Software', 'Software'))), ('Electronics', (('Monitor', 'Monitor'), ('Mouse', 'Mouse'), ('Keyboard', 'Keyboard'), ('Headphone', 'Headphone'), ('Earphone', 'Earphone'), ('Laptop', 'Laptop'), ('TV', 'TV'), ('Pen Drive', 'Pen Drive'), ('Router', 'Router'), ('AC', 'AC'), ('Tablets', 'Tablets'), ('Camera', 'Camera'))), ('Bag', 'Bag'), ('Wallet', 'Wallet'), ('T-Shirt', 'T-Shirt'), ('Jeans', 'Jeans'), ('Wrist Watch', 'Wrist Watch'), ('Belt', 'Belt'), ('Sunglass', 'Sunglass'), ('Shirt', 'Shirt'), ('Trouser', 'Trouser'), ('Shorts', 'Shorts'), ('Book', 'Book'), ('None', 'None')], max_length=20)),
                ('sub_category', models.CharField(blank=True, choices=[('Wired', 'Wired'), ('Wireless', 'Wireless'), ('SLR', 'SLR'), ('DSLR', 'DSLR'), ('None', 'None')], max_length=20)),
                ('usable_by', models.CharField(blank=True, choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids'), ('Boys', 'Boys'), ('Girls', 'Girls'), ('All', 'All'), ('None', 'None')], max_length=6)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
