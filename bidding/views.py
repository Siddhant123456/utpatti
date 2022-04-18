from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Bid
from crop.models import Crop
from account.models import UserProfile
import datetime

def place_bid(request):
    print('hello world')
    # amount = request.POST['amount']
    # user = request.user
    # user_prof = UserProfile.objects.get(user = user)
    # crop = request.POST['crop']
    # date = datetime.datetime.now()
    # crop_info = Crop.objects.get(id = crop)
    # bid = Bid.objects.get(bid_for_crop = crop_info)

    # new_bid = BidEntry()
    # new_bid.bid = bid
    # new_bid.merchant_bidding = user_prof
    # new_bid.bid_price = amount
    # new_bid.bid_time = date

    # new_bid.save()

    

    return HttpResponse('hello world')

    #return redirect('individual_crop' , crop_info.id)

    