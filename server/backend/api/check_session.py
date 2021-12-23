import sys
import os
from django.http import HttpResponse, JsonResponse
import json
import datetime
import time
import random
import numpy as np


def session_on_request():
    try:
        if 'userdata' in request.session:
            print()
        else:
            feedback = {
                'status': 'unidentified',
                'msg': 'Error connecting, now redirecting...',
                'row': '',
                'redirect': '/site/logout',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)
    except:
        feedback = {
            'status': 'unidentified',
            'msg': 'Error connecting, now redirecting...',
            'row': '',
            'redirect': '/site/logout',
            'classname': 'alert-danger p-2',
        }
        return JsonResponse(feedback, safe=False)

