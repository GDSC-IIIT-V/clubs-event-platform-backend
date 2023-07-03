from django.db import models

class User(models.Model):
    pass

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)


class Event(models.Model):
    Options = (
        ('Draft','Draft'),
        ('Published','Published'),
    )
    event_title= models.CharField(max_length=200)
    short_desc= models.CharField(max_length=300)
    event_desc=models.TextField()
    event_banner=models.FileField()
    event_thumbnail=models.FileField()
    tags =models.ManyToManyField(Tag)
    location=models.TextField()
    status = models.CharField(max_length=200,choices=Options)
    event_created_on = models.DateField()
    virtual_meet_instructions=models.TextField()
    virtual_meet_link= models.URLField()
    speaker = models.CharField(max_length=200,null=True)

class Schedule(models.Model):
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    no_of_days= models.BigIntegerField()
    start_time= models.TimeField()
    end_time= models.TimeField()
    event_schedule = models.JSONField(default=dict(day_title="", start_time="", end_time=""))


