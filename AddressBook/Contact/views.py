from django.shortcuts import render
from django.http import request, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import *

# Create your views here.

def getContactPage(request):

    return render(request,'Contact/index.html',{})

def getContacts(request):

    results = []

    if request.method == 'GET':

        Contacts = Contact.objects.filter()

        for cur in Contacts:

            result = {

                'id': cur.address_id,

                'firstname': cur.firstname,

                'lastname': cur.lastname,

                'email': cur.email,

                'phone': cur.phone,

                'image': str(cur.image),
                
            }

            results.append(result)

        return JsonResponse(results, safe=False)
    
    response = JsonResponse({})

    response.status_code = 500

    return response

@csrf_exempt
def updateContact(request):

    if request.method == "POST":

        post = json.loads(request.body.decode('utf-8'))

        if post:

            address_id = post.get('address_id',-1)

            if address_id == -1:

                firstname = post.get('firstname','')

                lastname = post.get('lastname','')

                email = post.get('email','')

                phone = post.get('phone','')

                image = post.get('image','')

                if Contact.objects.get_or_create(firstname = firstname, lastname = lastname, email = email, phone = phone, image = image)[1]:

                    return JsonResponse({})

                response = JsonResponse({})

                response.status_code = 500

                return response

            Contacts = Contact.objects.filter(address_id = address_id)

            if len(Contacts) == 1:

                if post.get('Function') == 'Delete':

                    Contacts.delete()

                    return JsonResponse({})

                firstname = post.get('firstname')

                lastname = post.get('lastname')

                email = post.get('email')

                phone = post.get('phone')

                image = post.get('image')

                if firstname != None:

                    Contacts.update(firstname = firstname)

                if lastname != None:

                    Contacts.update(lastname = lastname)

                if email != None:

                    Contacts.update(email = email)

                if phone != None:

                    Contacts.update(phone = phone)

                if image != None:

                    Contacts.update(image = image)

                return JsonResponse({})
            
    response = JsonResponse({})

    response.status_code = 500
    
    return response            
