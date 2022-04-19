from django.shortcuts import redirect, render
from .models import Bid, BidEntry
from crop.models import Crop
from account.models import UserProfile
import datetime

def create_bid(request, id):
    print("Hello")
    crop = Crop.objects.get(id=id)
    b_end = request.POST['last_date']
    b_start = datetime.date.today()
    active = True
    b_price = request.POST['base_price']
    
    crop_bid = Bid()
    crop_bid.bid_start_date = b_start
    crop_bid.bid_close_date = b_end = b_end
    crop_bid.base_price = b_price
    crop_bid.is_Active = active
    crop_bid.bid_for_crop = crop
    crop_bid.save()

    return redirect('individual_crop', crop.id)


def place_bid(request):
    print('hello world')
    amount = request.POST['amount']
    user = request.user
    user_prof = UserProfile.objects.get(user = user)
    crop = request.POST['crop']
    date = datetime.datetime.now()
    crop_info = Crop.objects.get(id = crop)
    bid = Bid.objects.get(bid_for_crop = crop_info)

    new_bid = BidEntry()
    new_bid.bid = bid
    new_bid.merchant_bidding = user_prof
    new_bid.bid_price = amount
    new_bid.bid_time = date

    new_bid.save()
    print("new", new_bid)
    return redirect('individual_crop' , crop_info.id)

    