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

current_file = "Web_menu_api"


def check_page(request):
    try:
        pagename = request.GET['pagename']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t1.* FROM web_menus t1 WHERE t1.status_id=%s AND t1.record_status = %s "
                                     "AND t1.menuName =%s",
                                     [1, 1, pagename])

            cursor.close()
            if counter > 0:
                access = True
                feedback = {
                        'status': 'success',
                        'statusmsg': 'success',
                        'msg': '',
                        'result': '',
                        'ifUserHasAccess': access,
                        'classname': '',
                    }
            else:
                access = False
                msg = """Oops! The page you requested cannot be found. The page might be temporary down,
                       the URL may be misspelled, no longer available or you do not have permission to use it,
                       please contact our support for further assistance."""

                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': str(msg),
                    'result': '',
                    'ifUserHasAccess': access,
                    'classname': 'alert-danger p-2',
                }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def list_record(request):
    try:
        getlimit = int(request.GET['limitTo'])
        if int(getlimit) == 1:
            limitTo = 18446744073709551615
            offset = 0
        else:
            limitTo = int(request.GET['limitTo'])
            offset = 0

        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM web_menus WHERE record_status=%s "
                                     "ORDER BY date_modified DESC, time_modified DESC, status_id DESC LIMIT %s OFFSET "
                                     "%s", [1, limitTo, offset])
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'There is no record here yet.',
                    'classname': 'alert-danger p-2',
                }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def list_filter(request):
    try:
        statusid = request.GET['status_id']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM web_menus WHERE "
                                     "record_status=%s AND status_id=%s OR visibility=%s ORDER BY date_modified DESC, "
                                     "time_modified DESC, status_id DESC, visibility DESC ", [1, statusid, statusid])
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'There is no record for your search, try another or'
                           ' use the New menu button to create one.',
                    'classname': 'alert-danger p-2',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def list_search(request):
    try:
        search = request.GET['search']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM web_menus WHERE record_status=%s AND "
                                     "menuName like %s OR time_modified like %s OR date_modified like %s "
                                     "ORDER BY date_modified DESC, time_modified DESC, status_id DESC",
                                     [1, '%{}%'.format(search), '%{}%'.format(search), '%{}%'.format(search)])

            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'There is no record for your search,'
                           ' try another or use the New menu button to create one.',
                    'classname': 'alert-danger p-2',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def preview(request):
    try:
        keyid = request.GET['keyid']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM web_menus WHERE record_status=%s AND id=%s "
                                     "ORDER BY date_modified DESC, time_modified DESC, status_id DESC", [1, keyid])
            row = dictfetchall(cursor)
            if counter > 0:
                data = {
                    'keyid': row[0]['id'],
                    'category': row[0]['category'],
                    'menuName': row[0]['menuName'],
                    'displayName': row[0]['menu_description'],
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
                    'msg': 'Something went wrong or this record no longer exist. '
                           'Kindly confirm this update and try again.',
                    'classname': 'alert-danger p-2',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def download(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t1.*, t2.email_one as Created_By FROM web_menus t1 "
                                     "INNER JOIN admin_record t2 ON t1.modified_by = t2.id "
                                     "ORDER BY t1.date_modified DESC, t1.time_modified DESC, t1.status_id DESC")

            row = dictfetchall(cursor)

            if counter > 0:
                df = pd.DataFrame(row)
                gettime = datetime.datetime.now()
                date_modified = str(datetime.date.today())
                time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
                filename = '{}_{}_{}.csv'.format(current_file, date_modified, time_modified)
                df.to_csv('static/reports/' + filename)
                with open("static/reports/" + filename, "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': 'Your file is ready for download, click the button below',
                    'result': '',
                    'baseData': str('data:text/csv;base64, ' + my_string.decode('utf-8')),
                    'baseDataname': str(filename),
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'There is no record to download,'
                           ' use the New menu button to create one.',
                    'classname': 'alert-danger p-2',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong! Please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)
