from django.db import models
from django.utils import timezone

from core.models import User, Semester, Card
from core.utils import get_semester
from members.models import Member


# Create your models here.
class AccessLevel(models.Model):
    name = models.CharField(max_length=20)
    uio_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class InternGroup(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(User)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, null=True, blank=True)
    groups = models.ManyToManyField(InternGroup, related_name='groups')
    access_levels = models.ManyToManyField(AccessLevel)

    def __str__(self):
        return self.name



class Intern(models.Model):
    user = models.ForeignKey(User)
    member = models.ForeignKey(Member, blank=True, null=True)
    recived_card = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    comments = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def cards(self):
        cards = self.user.card_set.all()
        return cards



class InternRole(models.Model):
    intern = models.ForeignKey(Intern, related_name='roles')
    role = models.ForeignKey(Role, related_name='intern')
    semester_start = models.ForeignKey(Semester, related_name='start', default=get_semester)
    semester_end = models.ForeignKey(Semester, related_name='end', null=True, blank=True)
    comments = models.CharField(max_length=300, null=True, blank=True)
    date_added =models.DateField(default=timezone.now)
    date_access_given = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.role, self.intern)