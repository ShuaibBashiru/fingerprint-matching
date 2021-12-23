from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os, time, json, sys, serial, random, datetime
import numpy as np
from django.db import connection
from .models import CreateAccount

def create_acccount(request):
    if request.method != "POST":
        feedback = {
            'status': 'Failed',
            'msg': 'Invalid request, try again',
            'row': '',
            'redirect': '/',
            'classname': 'alert-danger',
        }
        return JsonResponse(feedback, safe=False)
    else:
        try:
            save_record = CreateAccount()
            save_record.lastname = request.POST['lastname']
            save_record.firstname = request.POST['firstname']
            save_record.othername = request.POST['othername']
            save_record.email_one = request.POST['email']
            save_record.phone_one = request.POST['phone']
            save_record.persional_id = request.POST['persional_id']
            save_record.account_type = request.POST['account_type']
            save_record.save()
            feedback = {
                'status': 'success',
                'confirmed': 'success',
                'msg': 'Authentication successful, redirecting..',
                'redirect': '/',
                'classname': 'alert-primary',
            }
            return JsonResponse(feedback, safe=False)
        except:
            feedback = {
                'status': 'unidentified',
                'msg': 'Technical error, Please try again',
                'redirect': '/',
                'classname': 'alert-danger'
            }

            return JsonResponse(feedback, safe=False)
