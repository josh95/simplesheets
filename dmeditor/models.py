from django.db import models

class Dm(models.Model):
    dm_id = models.IntegerField(default=0, primary_key=True)
    dm_name = models.CharField(max_length=200)

class Player(models.Model):
    player_id = models.IntegerField(default=0, primary_key=True)
    dm_id = models.IntegerField(default=0)
    player_name = models.CharField(max_length=200)

class Sheets(models.Model):
    sheet_id = models.IntegerField(default=0, primary_key=True)
    player_id = models.IntegerField(default=0)
    character_name = models.CharField(max_length=200)

class Attributes(models.Model):
    attr_id = models.IntegerField(default=0, primary_key=True)
    sheet_id = models.IntegerField(default=0)
    attribute_name = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    temp_value = models.IntegerField(default=0)
    order = models.IntegerField(default=0)

class ally(models.Model):
    ally_id = models.IntegerField(default=0, primary_key=True)
    ally_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    personality = models.CharField(max_length=200)
    traits = models.CharField(max_length=200)
    last_edit= models.DateTimeField('date editted')
    img_url = models.CharField(max_length=300)

class level(models.Model):
    ally_id = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    decription = models.CharField(max_length=1000)

class item(models.Model):
    item_id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)
    decription = models.CharField(max_length=1000)
    importance = models.IntegerField(default=0)
    last_edit= models.DateTimeField('date editted')
    img_url = models.CharField(max_length=300)
    
