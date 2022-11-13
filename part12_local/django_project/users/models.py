from django.db import models
from django.contrib.auth.models import User
from PIL import Image # pillow module -tian

# after changing this file, do the following. -tian
#    restart django will not be enough
#    the last command covers the first two
# 1. python manage.py makemigrations
#    genertate sql under users/migrations/0001.py
# 2. python manage.py sqlmigrate users 0001
#    print the sql that the 0001.py will run
# 3. python manage.py migrate
#    run the sql to update database. this command covers the above 2 commands

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # is user is deleted, so will be the Profile -tian

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # this is how to print(f'{Profile}') -tian
    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            # resize image -tian
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
