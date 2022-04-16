from django.shortcuts import render
from .models import Bid, BidEntry
from crop.models import Crop
from account.models import UserProfile


def place_bid(request):
    amount = request.POST['amount']
    user = request.user
    user_prof = UserProfile.objects.get(user = user)
    crop = request.POST['crop']
    time = request.POST['time']
    crop_info = Crop.objects.get(id = crop)
    bid = Bid.objects.get(bid_for_crop = crop_info)

    

    new_bid = BidEntry()
    new_bid.bid = bid
    new_bid.merchant_bidding = user_prof
    new_bid.bid_price = amount
    new_bid.bid_time = time

    new_bid.save()

    



    