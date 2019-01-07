from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ClientForm
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from PhoneneNumbers.models import Client
from PhoneneNumbers.serializers import ClientSerializer

@csrf_exempt
def clients_list(request, format=None):
    """
    List all code clients, or create a new client.
    """
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def client_detail(request, name, format=None):
    """
    Retrieve, update or delete a client.
    """
    try:
        client = Client.objects.get(name=name)
    except Client.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientSerializer(client, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=204)

def clients(request):
    """
    See all clients in browser.
    """
    clients = Client.objects.all()[:1]
    return render(request, 'clients.html', {'clients': clients})

def client(request, name):
    """
    See  client info in browser.
    """
    clients = Client.objects.filter(name=name)
    return render(request, 'client.html', {'clients': clients})


def search(request):
    """
    Search client.
    """
    if ('name' in request.GET) and request.GET['name'].strip():
        name = request.GET['name']
        client = Client.objects.get(name=name)
        return render(request, 'client.html', {'client': client})
    else:
        return render(request, 'base.html')

def create_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', None)
            client = form.save(commit=False)
            client.save()
            return redirect('/%s'%name)
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})


def update():
    pass