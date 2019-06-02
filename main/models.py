from django.db import models

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=30)
    url = models.URLField()
    logo = models.ImageField(upload_to='companies')
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    role = models.CharField(max_length=30)
    start_date = models.IntegerField()
    end_date = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ['start_date']

    @property
    def date(self):
        if self.start_date == self.end_date:
            return self.end_date

        return '{} - {}'.format(self.start_date, self.end_date if self.end_date else 'Present')

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.country)

    def __str__(self):
        return '{}, {} {}'.format(self.role, self.company, self.date)


class Education(models.Model):
    university = models.CharField(max_length=40)
    url = models.URLField()
    logo = models.ImageField(upload_to='universities')
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    major = models.CharField(max_length=50)
    start_date = models.IntegerField()
    end_date = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        ordering = ['start_date']

    @property
    def date(self):
        if self.start_date == self.end_date:
            return self.end_date

        return '{} - {}'.format(self.start_date, self.end_date if self.end_date else 'Present')

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.country)

    def __str__(self):
        return '{}, {} {}'.format(self.major, self.university, self.date)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    projects = models.ManyToManyField('Project', through='ProjectTag', related_name='tags')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='projects')
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return '{} in {}'.format(self.tag, self.project)
