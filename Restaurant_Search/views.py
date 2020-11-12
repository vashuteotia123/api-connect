from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pyzomato import Pyzomato
import json
from Restaurant_Search.models import Reviews

# Create your views here.

def home(request):
    return render(request, 'Restaurant_Search/index.html')

@csrf_exempt
def searchRestaurant(request):
    p = Pyzomato('f60135cc9df671c1030f88ca24e36fc0')
    if request.GET.get('city', False) or request.GET.get('search', False):
        city = request.GET["city"]
        search_key = request.GET["search"]


        city = p.getLocations("query="+str(city))
        res_id = [] 
        data = {}

        search_results = p.search(entity_id=city['location_suggestions'][0]['entity_id'], entity_type=city['location_suggestions'][0]['entity_type'] ,q=search_key)
        # print(search_results['restaurants'][0]['restaurant']['R']['res_id'],search_results['restaurants'][1]['restaurant']['R']['res_id'])
        # search_results = p.search(entity_id=city['location_suggestions'][id]['entity_id'], entity_type=city['location_suggestions'][id]['entity_type'] ,q=search_key)
        try:
            for id in range(0,10):
                resta_id = search_results['restaurants'][id]['restaurant']['R']['res_id']
                data[resta_id]={}
                data[resta_id]['name'] = search_results['restaurants'][id]['restaurant']['name']
                data[resta_id]['cusine'] = search_results['restaurants'][id]['restaurant']['cuisines']
                data[resta_id]['address'] = search_results['restaurants'][id]['restaurant']['location']['address']
                data[resta_id]['average_cost_for_two'] = search_results['restaurants'][id]['restaurant']['average_cost_for_two']
                data[resta_id]['rating'] = search_results['restaurants'][id]['restaurant']['user_rating']['aggregate_rating']
                res_id.append(resta_id)
        except:
            status = 'failed'
        else:
            status = 'success'
        if status=='success':
            return render(request, 'Restaurant_Search/SearchResults.html',{'res_id':res_id, 'data':data,'city':request.GET["city"],'search_key':search_key} )
        if status=='failed':
            return render(request, 'Restaurant_Search/SearchResults.html',{'res_id':res_id, 'data':data,'city':request.GET["city"],'search_key':search_key,'no_results':'no_results'} )

    elif request.GET.get('res_id', False):
        res_id = request.GET["res_id"]
        data = p.getRestaurantDetails(restaurant_id=res_id)
        
        print(data['name'])
        data
        return JsonResponse (data)
