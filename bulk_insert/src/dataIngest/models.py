from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()



class CassiniData(models.Model):

    id = models.BigAutoField(primary_key=True)
    start_time_utc = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=250, null=True)
    date = models.CharField(null=True, max_length=50)
    team = models.CharField(max_length=25, null=True)
    spass_type = models.CharField(max_length=100, null=True)
    target = models.CharField(max_length=25, null=True)
    request_name = models.CharField(max_length=50, null=True)
    library_definition = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    identifier = models.UUIDField(auto_created=False, unique=True)

    class Meta:
        db_table = "cassinni_data"
