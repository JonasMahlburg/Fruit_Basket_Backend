from django.shortcuts import  render
from django.http import HttpResponse
from .fruit_list import fruits
import json




def send_fruits(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(fruits), content_type="application/json")
    

    elif request.method == 'POST':
        data = json.loads(request.body)

        # Optional: einfache Validierung
        if 'name' in data and 'gewicht' in data and 'farbe' in data:
            fruits.append(data)
            return HttpResponse(json.dumps({"status": "success", "added": data}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status": "error", "message": "Missing fields"}), content_type="application/json", status=400)
        

def send_more_fruits(request):
    return render(request, 'fruit_basket/fruitlist.html', {'fruits': fruits})

def show_info(request):
    return render(request, 'fruit_basket/info.html', {'fruits': fruits})