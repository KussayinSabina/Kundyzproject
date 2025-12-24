from django.shortcuts import render

def order(request):
    return render(request, 'orders/order.html')

def orders_list(request):
    return render(request, 'orders/order_list.html')

def order_create(request):
    return render(request, 'orders/create_order.html')

def canceled(request):
    return render(request, 'orders/canceled.html')

def success(request):
    return render(request, 'orders/success.html')
