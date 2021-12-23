from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
import time
import json
import sys
import random
import datetime
import numpy as np
from django.db import connection, transaction
from upload.user_account_model import AddUserAccount
from authentication.writer import write_error
from authentication.query_columns import dictfetchall
import mimetypes
import tensorflow as tf
from tensorflow.keras.models import model_from_json, load_model
import imagehash
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


current_file = 'Upload'


def classify(request):
    data = b'00f88001c82ae3735cc0413709ab71b0b71455924635a401bac5a99439ccd0e275c83d29f9581c94c643dabef50cacde054d04981fbd2b62463ff3d7ca099fe495cafb10110db6c72dfac7ca03ef1e98577ae084af1b98e8f21fd497f521bca1e39924a3b5a9874bc41f7509e0269e655ac7de18195ddd8c9020710a9e32e55ffa73a65081323a5d944401faa74022af3cd489d36bbf2a49c74cff385e8bcf04062ea975e77aa08a16ccb8be4bbaef5dcf9732b85a60d9272cdc63ca8c7b92225e25ecdf68a33882b1429c3939d94461bb7ef027dc9ec66428e9cb35a487fa0dfde1e50fadeab3a82851ae0c7dbfbef9b0257483928f7d8eb5a16591e6aee1'
    success = 0
    failed = 0
    filename = ''
    load_output = ''
    accepted_file = 'image/png'
    accepted_file2 = 'image/jpg'

    try:
        filename = str(int(round(time.time() * 1000)))
        if request.method != 'POST':
            feedback = {
                'status': 'Invalid request',
                'statusmsg': 'error',
                'msg': 'Something went wrong! please refresh or contact our support for further assistance',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)
        else:
            form = request.FILES['fileupload']
            location = 'static/fileuploaded/'
            file_url = location + filename + '.png'
            file_type = mimetypes.guess_type(file_url, strict=True)
            if str(file_type[0]) != str(accepted_file) and str(file_type[0]) != str(accepted_file2):
                # print(file_type[0])
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'Something went wrong! This file type is not an acceptable format, please try another file '
                           'format such as (PNG).',
                    'classname': 'alert-danger p-2',
                }
                return JsonResponse(feedback, safe=False)
            else:
                fs = FileSystemStorage(location=location)
                fs.save(filename + '.png', form)
                success += 1

    except Exception as e:
        failed += 1
        write_error(current_file, e)

    if success > 0:
        # Comparison
        res = test(filename)
        if res != 0:
            score = res
            # print(res[2])
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'This signal most likely belongs to {} signal with a {} percent confidence.'.format(res[0], res[1]),
                'information': 'About this signal: {}'.format(res[2]),
                'filename': filename + str('.png'),
                'classname': 'alert-primary p-2'
            }
            print(feedback)
        else:
            feedback = {
                'status': 'success',
                'statusmsg': 'error',
                'result': "Sorry, I could not recognized this image, please use an acceptable format.",
                'filename': filename + str('.png'),
                'msg': 'Success! Kindly confirm the information about about this signal as stated below',
                'classname': 'alert-primary p-2'
            }

    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'total': 0,
            'msg': 'Something went wrong! refresh and try again or contact support',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)



def test(filename):
    class_names = ['Fusion beat', 'Normal', 'Supraventricular ectopic beat', 'Ventricular ectopic beat']
    class_info = ['A fusion beat occurs when electrical impulses from different sources act upon the same region of the heart at the same time. If it acts upon the ventricular chambers it is called a ventricular fusion beat, whereas colliding currents in the atrial chambers produce atrial fusion beats', 'This is a Normal heartbeat signal', 'Supraventricular Ectopy (SVE) indicates sinus rhythm with occasional irregular beats originating from the top of the heart. A common reason for this is premature atrial contractions (PACs)', 'Ventricular tachycardia may last for only a few seconds, or it can last for much longer. You may feel dizzy or short of breath, or have chest pain. Sometimes, ventricular tachycardia can cause your heart to stop (sudden cardiac arrest), which is a life-threatening medical emergency.']
    img_height = 432
    img_width = 288
    testimage = 'static/fileuploaded/'+filename+'.png'
    model_location = 'static/model/model_output.h5'
    acceptableFile = 'static/model/F1.png'
    hash0 = imagehash.average_hash(Image.open(acceptableFile))
    hash1 = imagehash.average_hash(Image.open(testimage))
    cutoff = 16
    # print(hash0 - hash1)
    if (hash0 - hash1) <= cutoff:
        model = load_model(model_location)
        img = tf.keras.utils.load_img(
        testimage, target_size=(img_height, img_width)
        )
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)
        predictions = model(img_array)
        score = tf.nn.softmax(predictions[0])
        getClass = class_names[np.argmax(score)]
        getPercentage = int(100 * np.max(score))
        getInfo = class_info[np.argmax(score)]
        result = [getClass, getPercentage, getInfo]
        return result

    else:
        return 0
