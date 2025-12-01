from django.contrib.auth import get_user_model

def run():
    User = get_user_model()
    username = "hamzabrh1"
    password = "Hamza@4443"
    email = "hamzabrh@gmail.com"

    if not User.objects.filter(username=username).exists():
        print("Creating admin user...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("Admin user already exists.")