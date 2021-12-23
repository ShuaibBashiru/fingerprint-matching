import sys
import os
from django.http import HttpResponse, JsonResponse
import json
import datetime
import time
from numpy import random
import numpy as np
import pandas as pd
import csv
import urllib.request
from django.db import connection
from authentication.query_columns import dictfetchall
from authentication.writer import write_error
import pickle
import base64

current_file = "list_user_record"


def get_user_profile(request):
    try:
        email = request.GET['email'].lower()
        keyid = request.GET['keyid']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM user_record WHERE record_status=%s AND id=%s AND email_one =%s", [1, keyid, email])
            row = dictfetchall(cursor)
            cursor.close()
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'record': True,
                    'msg': '',
                    'result': row[0],
                    'classname': 'alert-primary',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'record': False,
                    'msg': 'Something went wrong or record not found! please go back and try again.',
                    'classname': 'alert-danger p-2',
                }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'record': False,
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger',
        }

    return JsonResponse(feedback, safe=False)


def user_data_session(request):
    try:
        keyid = request.session['userdata']['id']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT email_one, phone_one, surname, firstname, othername FROM user_record "
                                     "WHERE record_status=%s "
                                     "AND id=%s", [1, keyid])
            row = dictfetchall(cursor)
            cursor.close()
            print(row)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'record': True,
                    'result': row[0],
                    'classname': 'alert-primary',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'record': False,
                    'msg': 'Something went wrong or record not found! please go back and try again.',
                    'classname': 'alert-danger',
                }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'record': False,
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger',
        }

    return JsonResponse(feedback, safe=False)
