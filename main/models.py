from django.db import models
from django.contrib.auth.models import User

# exceptions
from django.core.exceptions import ValidationError


# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=30)
    url = models.URLField()
    logo = models.ImageField(upload_to='companies')
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    role = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.country)

    def __str__(self):
        return '{}, {}'.format(self.role, self.company)


class Education(models.Model):
    university = models.CharField(max_length=40)
    url = models.URLField()
    logo = models.ImageField(upload_to='universities')
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    major = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.country)

    def __str__(self):
        return '{}, {}'.format(self.major, self.university)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    projects = models.ManyToManyField('Project', through='ProjectTag', related_name='tags')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects')
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return '{} in {}'.format(self.tag, self.project)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile')
    message = models.TextField(max_length=255)
    resume = models.FileField(upload_to='profile')
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "profile"

    @property
    def origin(self):
        return '{}, {}'.format(self.city, self.country)

    def save(self, *args, **kwargs):
        if Profile.objects.exists() and not self.pk:
            raise ValidationError('There can be only one Profile instance')
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return 'Main Profile'


class SiteMetaData(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.CharField(max_length=155, blank=True, null=True)
    keywords = models.CharField(max_length=155, blank=True, null=True)
    site_name = models.CharField(max_length=60, blank=True, null=True)
    image = models.ImageField(upload_to='meta', blank=True, null=True)
    google_tracking_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name_plural = "site meta data"

    def save(self, *args, **kwargs):
        if SiteMetaData.objects.exists() and not self.pk:
            raise ValidationError('There can be only one SiteMetaData instance')
        return super(SiteMetaData, self).save(*args, **kwargs)

    def __str__(self):
        return 'Site Meta Data'
