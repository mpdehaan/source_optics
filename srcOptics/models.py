from django.db import models

# ?? rather than have 'Account', you can use the built in Django user and
# group models - definitely do this, because Django logins already work with
# these
class Organization(models.Model):
    # parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    owner = models.TextField(max_length=32, default='')
    name = models.TextField(max_length=32, default='')
    admins = models.ManyToManyField('Account', related_name='admins')
    members = models.ManyToManyField('Account', related_name='members')

    def __str__(self):
        return self.name

class Repository(models.Model):
    parent = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    url = models.TextField(max_length=256, default='')
    name = models.TextField(max_length=32, default='')
    
    def __str__(self):
        return self.name

class LoginCredential(models.Model):
    repo = models.ForeignKey(Repository, on_delete=models.CASCADE)
    username = models.TextField(max_length=32, default='')
    password = models.TextField(max_length=128, default='')
    
class Commit(models.Model):
    repo = models.ForeignKey(Repository, on_delete=models.CASCADE)
    sha = models.TextField(max_length=256, default='')
    lines_added = models.IntegerField(default=0)
    lines_removed = models.IntegerField(default=0)

class Author(models.Model):
    commit = models.ForeignKey(Commit, on_delete=models.CASCADE)
    email = models.TextField(max_length=64, default='')

# ?? get rid of me
class Account(models.Model):
    organizations = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    repos = models.ForeignKey(Repository, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.TextField(max_length=16, default='')
    email = models.TextField(max_length=32, default='')

    def __str__(self):
        return self.username
