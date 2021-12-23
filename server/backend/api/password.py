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

current_file = "password_validate"


def validate_password_id(request):
    try:
        keyid = request.GET['keyid']
        email = request.GET['email']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM reset_password WHERE status_id=%s AND "
                                     "resetCode=%s AND email_one =%s LIMIT 1", [1, keyid, email])
            row = dictfetchall(cursor)
            if counter > 0:
                data = {
                   'keyid': row[0]['resetCode'],
                }
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': data,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'Something went wrong or this record no longer exist, kindly try again using forgotten '
                           'password.',
                    'classname': '',
                        }
    except Exception as e:
        write_error('widget_list', e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong or this record no longer exist. '
                   'Kindly try again using forgotten password.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)

