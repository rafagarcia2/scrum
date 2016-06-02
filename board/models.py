from __future__ import unicode_literals
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Sprint(models.Model):
	name = models.CharField(max_length=100, blank=True, default='')
	descript = models.TextField(blank=True, default='')
	end = models.DateField(unique=True)

	def __str__(self):
		return self.name or _('Sprint ending %s') % self.end

class Task(models.Model):
	"""Unidade referente ao trabalho a ser realizado no sprint."""

	STATUS_TODO = 1
	STATUS_IN_PROGRESS = 2
	STATUS_TESTING = 3
	STATUS_DONE = 4

	STATUS_CHOICE = (
		(STATUS_TODO, _('Not Started')),
		(STATUS_IN_PROGRESS, _('In Processing')),
		(STATUS_TESTING, _('Testing')),
		(STATUS_DONE, _('Done')),
	)

	name = models.CharField(max_length=100)
	descript = models.TextField(blank=True, default='')
	sprint = models.ForeignKey(Sprint, blank=True, default='')
	status = models.SmallIntegerField(choices=STATUS_CHOICE, default=STATUS_TODO)
	order = models.SmallIntegerField(default=0)
	assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	started = models.DateField(blank=True, null=True)
	due = models.DateField(blank=True, null=True)
	completed = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.name;