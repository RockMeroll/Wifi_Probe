from django.db import models


class Room(models.Model):
    rid = models.IntegerField(primary_key=True, db_column='RID')  # Field name made lowercase.
    rno = models.CharField(db_column='Rno', max_length=20)  # Field name made lowercase.
    mmac = models.CharField(db_column='MMac', max_length=20)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Room'


class Course(models.Model):
    cid = models.IntegerField(primary_key=True, db_column='CID')  # Field name made lowercase.
    cname = models.CharField(db_column='CName', max_length=20)  # Field name made lowercase.
    rid = models.IntegerField(db_column='RID')  # Field name made lowercase.
    sid = models.IntegerField(db_column='SID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'Course'


class Courseselect(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cid = models.IntegerField(db_column='CID')  # Field name made lowercase.
    sid = models.IntegerField(db_column='SID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'CourseSelect'

