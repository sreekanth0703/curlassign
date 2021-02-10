from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, default='')

    class Meta:
        db_table = 'USER_PROFILE'

    def __unicode__(self):
        return self.user.username


class UserMapping(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_user = models.ForeignKey(User, related_name='admin_user', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'USER_MAPPING'

    def __unicode__(self):
        return '%s:%s' % (str(admin_user.username), str(user.username))


class LoginRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=50, default='')
    company = models.CharField(max_length=50, default='')
    status = models.CharField(max_length=16, default='pending')

    class Meta:
        db_table = 'LOGIN_REQUEST'

