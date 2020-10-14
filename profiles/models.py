from django.db import models
from django.conf import settings
from PIL import Image
#from django.db.models.signals import post_save

class Profile(models.Model):

    USER_CHOICES = (
        ('student', 'student'),
        ('counsel', 'counsel'),
        ('dean', 'dean'),
    )

    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #slug = models.SlugField()

    #appointments = models.ManyToManyField("Profile", blank=True)
    user_type = models.CharField(max_length = 20, choices=USER_CHOICES, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length = 20, choices=GENDER_CHOICES, null=True, blank=True)
    year = models.IntegerField(default=1)
    course = models.CharField(max_length=50, default='', null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size =(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    #def get_absolute_url(self):
    	#return "/users/{}".format(self.slug)


#def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#   if created:
#        try:
#            Profile.objects.create(user=instance)
#        except:
#            pass

#post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
