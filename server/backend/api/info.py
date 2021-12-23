import sys
import os
from django.http import HttpResponse, JsonResponse
# import json
import datetime
import time
from numpy import random
# import urllib.request
from django.db import connection
from authentication.query_columns import dictfetchall
from authentication.writer import write_error
import nltk
from difflib import SequenceMatcher
current_file = "User information"


def getenrolled(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, CreatedDate FROM enroll")
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
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def preview(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, CreatedDate FROM train_data LIMIT 10")
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
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def preview2(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, CreatedDate FROM train_data LIMIT 10 OFFSET 9")
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
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def user(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, CreatedDate FROM enroll LIMIT 10")
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
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def user2(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, CreatedDate FROM enroll LIMIT 10 OFFSET 9")
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
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def classify(request):
    try:
        finger_id_one = request.GET['finger_id_one']
        finger_id_two = request.GET['finger_id_two']
        print(finger_id_one)
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, FingerSample,"
                                     " HEX(CONVERT(FingerSample using utf8)),"
                                     " CreatedDate FROM enroll WHERE id =%s OR id=%s", [finger_id_one, finger_id_two])
            row = dictfetchall(cursor)
            finger1 = str(row[0]['FingerSample'])
            finger2 = str(row[1]['FingerSample'])
            s = SequenceMatcher(None, finger1, finger2)
            threshold = s.ratio()
            score = nltk.translate.bleu_score.sentence_bleu([finger1], finger2, weights=(0.5, 0.5))

            newdata1 = {
                "Category": row[0]['Category'],
                "id": row[0]['id'],
                "CreatedDate": row[0]['CreatedDate'],
                "identical": score,
                "threshold": '{:.2f}'.format(threshold),
            }
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': newdata1,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def classify2(request):
    try:
        finger_id_one = request.GET['finger_id_one']
        finger_id_two = request.GET['finger_id_two']
        print(finger_id_one)
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT Category, id, FingerSample,"
                                     " HEX(CONVERT(FingerSample using utf8)),"
                                     " CreatedDate FROM enroll WHERE id =%s OR id=%s", [finger_id_one, finger_id_two])
            row = dictfetchall(cursor)
            finger1 = str(row[0]['FingerSample'])
            finger2 = str(row[1]['FingerSample'])
            s = SequenceMatcher(None, finger1, finger2)
            threshold = s.ratio()
            score = nltk.translate.bleu_score.sentence_bleu([finger1], finger2, weights=(0.5, 0.5))

            newdata1 = {
                "Category": row[0]['Category'],
                "id": row[0]['id'],
                "CreatedDate": row[0]['CreatedDate'],
                "identical": score,
                "threshold": '{:.2f}'.format(threshold),
            }
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': newdata1,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'No record returned',
                    'classname': 'alert-danger p-2',
                }
    except KeyError as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)
