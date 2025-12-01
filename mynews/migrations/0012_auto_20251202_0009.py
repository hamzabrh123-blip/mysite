from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    
    # Superuser data (change if you want)
    username = "hamzareal"
    email = "admin@example.com"
    password = "Hamza@5555"  # Render पर भी काम करेगा

    # अगर user already है तो skip
    if not User.objects.filter(username=username).exists():
        User.objects.create(
            username=username,
            email=email,
            is_staff=True,
            is_superuser=True,
            password=make_password(password)
        )

def delete_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username="hamzareal").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0011_merge_20251202_0009'),
    ]

    operations = [
        migrations.RunPython(create_admin, delete_admin),
    ]
