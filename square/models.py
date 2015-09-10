from django.db import models

import uuid

from django.utils import timezone


class Event(models.Model):
    event_id = models.UUIDField(default=uuid.uuid4, editable=False)

    created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)


class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    event = models.ForeignKey(Event)

    created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)


class Expense(models.Model):

    event = models.ForeignKey(Event)
    amount = models.FloatField(default=0)
    title = models.CharField(max_length=255)

    created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)


class Contribution(models.Model):

    created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)

    amount = models.IntegerField(default=0)
    event = models.ForeignKey(Event)
    member = models.ForeignKey(Member)


