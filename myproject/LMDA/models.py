from django.db import models


class Locomotive(models.Model):
    registration_number = models.CharField(max_length=255, unique=True)
    depot = models.CharField(max_length=255)
    LOCOMOTIVE_TYPE_CHOICES = (
        ('cargo', 'Cargo'),
        ('passenger', 'Passenger'),
    )
    locomotive_type = models.CharField(max_length=10, choices=LOCOMOTIVE_TYPE_CHOICES)
    year_of_production = models.DateField()


class Brigade(models.Model):
    brigade_number = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15)


class Repair(models.Model):
    locomotive = models.ForeignKey(Locomotive, on_delete=models.CASCADE)
    REPAIR_TYPE_CHOICES = (
        ('current', 'Current'),
        ('maintenance', 'Maintenance'),
        ('unscheduled', 'Unscheduled'),
    )
    repair_type = models.CharField(max_length=12, choices=REPAIR_TYPE_CHOICES)
    start_date = models.DateField()
    days_required = models.IntegerField()
    daily_repair_cost = models.DecimalField(max_digits=10, decimal_places=2)
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)


class Worker(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.SET_NULL, null=True, blank=True)
    is_brigade_leader = models.BooleanField()
    birth_date = models.DateField()
