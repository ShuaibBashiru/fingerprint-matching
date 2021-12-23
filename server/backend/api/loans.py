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

current_file = "Loan_record"


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
            counter = cursor.execute("SELECT t2.id userid, t2.surname, t2.firstname, t2.email_one, t2.phone_one, "
                                     "t1.* FROM loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id "
                                     "WHERE t2.record_status=%s ORDER BY t1.date_modified DESC, t1.time_modified DESC, "
                                     "t1.status_id DESC LIMIT %s OFFSET %s",
                                     [1, limitTo, offset])
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': 'alert-primary p-2',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
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
            counter = cursor.execute("SELECT t2.surname, t2.firstname, t2.email_one, t2.phone_one, t1.* FROM "
                                     "loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id WHERE "
                                     "t2.record_status=%s AND t1.status_id=%s ORDER BY t1.date_modified DESC, "
                                     "t1.time_modified DESC, t1.status_id DESC", [1, statusid])
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': 'alert-primary p-2',
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
            counter = cursor.execute("SELECT t2.surname, t2.firstname, t2.email_one, t2.phone_one, t1.* FROM "
                                     "loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id WHERE "
                                     "t2.record_status=%s AND (t2.surname like %s OR t2.firstname like %s OR "
                                     "t2.email_one like %s OR t2.phone_one like %s OR t1.date_modified like %s OR "
                                     "t1.time_modified like %s)", [1, "%{}%".format(search), "%{}%".format(search),
                                                                   "%{}%".format(search), "%{}%".format(search),
                                                                   "%{}%".format(search), "%{}%".format(search)])

            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': 'alert-primary p-2',
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


def validate_data(request):
    try:
        keyid = request.GET['keyid']
        userid = request.session['userdata']['id']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t2.id userid, t2.surname, t2.firstname, t2.othername, t2.email_one, "
                                     "t2.phone_one, "
                                     "t1.* FROM loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id "
                                     "WHERE t1.record_status=%s AND t1.status_id=%s AND t1.attended_by=%s AND t1.id=%s "
                                     "ORDER BY t1.date_modified "
                                     "DESC, t1.time_modified DESC, t1.status_id DESC", [1, 1, userid, keyid])
            row = dictfetchall(cursor)
            if counter > 0:
                data = {
                    'keyid': row[0]['id'],
                    'user': row[0]['userid'],
                    'surname': row[0]['surname'],
                    'firstname': row[0]['firstname'],
                    'othername': row[0]['othername'],
                    'email_one': row[0]['email_one'],
                    'phone_one': row[0]['phone_one'],
                    'request_amount': row[0]['request_amount'],
                    'duration': row[0]['duration'],
                    'year_apply': row[0]['year_apply'],
                    'month_apply': row[0]['month_apply'],
                    'day_apply': row[0]['day_apply'],
                    'year_expire': row[0]['year_expire'],
                    'month_expire': row[0]['month_expire'],
                    'day_expire': row[0]['day_expire'],
                    'expire_date': row[0]['expire_date'],
                    'user_comment': row[0]['user_comment'],
                    'admin_comment': row[0]['admin_comment'],
                    'uniqueCode': row[0]['uniqueCode'],
                }
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': data,
                    'record': True,
                    'classname': 'alert-primary p-2',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'Oops! This request has not been activated for you or is being attended to by another '
                           'user, please confirm and try again.',
                    'record': False,
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


def check_previous_debt(request):
    try:
        keyid = request.session['userdata']['id']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM loan_request WHERE user_id =%s AND payment_status =%s", [keyid, 0])
            if counter > 0:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'Hi, {}! You have an existing loan you have not paid, kindly pay or contact our '
                           'support to help you further.'.format(request.session['userdata']['surname']),
                    'classname': 'alert-danger p-2',
                }
            else:
                with connection.cursor() as cursor_check:
                    counter = cursor_check.execute("SELECT email_one, surname, firstname FROM user_record WHERE "
                                                   "record_status=%s AND id=%s", [1, keyid])

                    row = dictfetchall(cursor_check)
                    cursor.close()
                    if counter > 0:
                        feedback = {
                            'status': 'success',
                            'statusmsg': 'success',
                            'msg': '',
                            'result': row[0],
                            'classname': '',
                        }

                    else:
                        feedback = {
                            'status': 'failed',
                            'msg': 'Something went wrong with your record, please refresh or contact our support for '
                                   'further assistance.',
                            'classname': '',
                        }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, please refresh or contact our support for '
                   'further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def allow_debtor(request):
    try:
        keyid = request.session['userdata']['id']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM loan_request WHERE user_id =%s AND payment_status =%s", [keyid, 0])
            if counter >= 3:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'Hi, {}! You have too many loan requests you have not been cleared of, kindly contact our '
                           'support to help you further.'.format(request.session['userdata']['surname']),
                    'classname': 'alert-danger p-2',
                }
            else:
                with connection.cursor() as new_cursor:
                    counter = new_cursor.execute("SELECT email_one, surname, firstname FROM user_record WHERE "
                                                 "record_status=%s AND id=%s", [1, keyid])

                    row = dictfetchall(new_cursor)
                    cursor.close()
                    if counter > 0:
                        feedback = {
                            'status': 'success',
                            'statusmsg': 'success',
                            'msg': '',
                            'result': row[0],
                            'classname': '',
                        }

                    else:
                        feedback = {
                            'status': 'failed',
                            'msg': 'Something went wrong with your record, please refresh or contact our support for '
                                   'further assistance.',
                            'classname': '',
                        }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, please refresh or contact our support for '
                   'further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def loan_history(request):
    try:
        email = request.GET['email'].lower()
        keyid = request.GET['keyid']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t2.surname, t2.firstname, t2.email_one, t2.phone_one, t1.* FROM "
                                     "loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id WHERE "
                                     "t1.record_status=%s AND t1.user_id=%s AND t2.email_one=%s "
                                     "ORDER BY t1.date_modified DESC, t1.time_modified DESC, "
                                     "t1.status_id DESC", [1, keyid, email])
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'record': True,
                    'classname': 'alert-primary p-2',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'You currently do not have any loan history',
                    'record': False,
                    'classname': 'alert-danger p-2',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong! please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def preview(request):
    try:
        keyid = request.GET['keyid']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t2.surname, t2.firstname, t2.email_one, t2.phone_one, t1.* FROM "
                                     "loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id WHERE "
                                     "t1.record_status=%s AND t1.id=%s ORDER BY t1.date_modified DESC, "
                                     "t1.time_modified DESC, t1.status_id DESC", [1, keyid])
            row = dictfetchall(cursor)
            if counter > 0:
                data = {
                    'keyid': row[0]['id'],
                    'surname': row[0]['surname'],
                    'firstname': row[0]['firstname'],
                    'email_one': row[0]['email_one'],
                    'phone_one': row[0]['phone_one'],
                    'request_amount': row[0]['request_amount'],
                    'duration': row[0]['duration'],
                    'year_apply': row[0]['year_apply'],
                    'month_apply': row[0]['month_apply'],
                    'day_apply': row[0]['day_apply'],
                    'year_expire': row[0]['year_expire'],
                    'month_expire': row[0]['month_expire'],
                    'day_expire': row[0]['day_expire'],
                    'expire_date': row[0]['expire_date'],
                    'user_comment': row[0]['user_comment'],
                    'admin_comment': row[0]['admin_comment'],
                    'uniqueCode': row[0]['uniqueCode'],
                }
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': data,
                    'classname': 'alert-primary p-2',
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
            counter = cursor.execute("SELECT t2.surname, t2.firstname, t2.email_one, t2.phone_one, t1.* FROM "
                                     "loan_request as t1 INNER JOIN user_record as t2 on t1.user_id = t2.id WHERE "
                                     "t2.record_status=%s ORDER BY t1.date_modified DESC, "
                                     "t1.time_modified DESC, t1.status_id DESC", [1, ])
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
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)
