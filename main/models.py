from django.db import models

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='companies', blank=True)
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    role = models.CharField(max_length=30)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['start_date']

    @property
    def date(self):
        if self.start_date == self.end_date:
            return self.end_date

        return '{} - {}'.format(self.start_date, self.end_date)

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.country)

    def __str__(self):
        return '{}, {} {}'.format(self.role, self.company, self.date)


class Education(models.Model):
    university = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='universities', blank=True)
    country = models.CharField(max_length=2)
    city = models.CharField(max_length=24)
    major = models.CharField(max_length=50)
    start_date = models.IntegerField()
    end_date = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['start_date']

    @property
    def date(self):
        if self.start_date == self.end_date:
            return self.end_date

        return '{} - {}'.format(self.start_date, self.end_date)

    @property
    def location(self):
        return '{}, {}'.format(self.city, self.country)

    def __str__(self):
        return '{}, {} {}'.format(self.major, self.university, self.date)
