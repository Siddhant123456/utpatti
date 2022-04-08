from django.db import models
from crop.models import Crop
from datetime import date
from account.models import UserProfile
# Create your models here.



class Bid(models.Model):
    bid_id = models.CharField(primary_key=True, max_length=10)
    bid_start_date = models.DateField(blank=False, default=date.today)
    bid_close_date = models.DateField(blank=False, default=date.today)
    base_price = models.FloatField(blank=False, default=0.0)
    is_Active = models.BooleanField(default=True)
    bid_for_crop = models.OneToOneField(Crop, on_delete=models.CASCADE, null=True, blank=True)

class BidEntry(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    merchant_bidding = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bid_price = models.FloatField(default=0.0)
    bid_time = models.DateTimeField(auto_now=True)