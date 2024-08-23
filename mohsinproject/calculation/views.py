import json
from functools import reduce
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def total_sum(request) :
    data = json.loads(request.body)
    number = data.get('numbers')
    sum_result = sum(number)
    return JsonResponse({'numbers' : sum_result})

def total_average(request) :
    data = json.loads(request.body)
    number = data.get('numbers')
    average_result_1 = sum(number)
    average_result_2 = average_result_1 / len(number)
    return JsonResponse({'numbers' : average_result_2})

def total_product(request) :
    data = json.loads(request.body)
    number = data.get('numbers')
    product_result = reduce(lambda x, y : x * y, number)
    return JsonResponse({'numbers' : product_result})


