# from django.http import HttpResponse, JsonResponse
# from django.core.files.storage import FileSystemStorage
# import cv2
# import serial
# import string
# import random
# import os
# import tensorflow as tf
# from keras.models import load_model
# from PIL import Image
# from keras.preprocessing import image
# import numpy as np
#
#
# def get_camera(request):
#     img_counter = 0
#     passmessage = "You have {} image(s) captured".format(img_counter)
#     cam = cv2.VideoCapture(0)
#     cv2.namedWindow("FACE CAPTURE PANEL")
#     cap = cv2.VideoCapture(0)
#     if cap is None or not cap.isOpened():
#         print('ok')
#     else:
#         cap.release()
#         cv2.destroyAllWindows()
#
#     try:
#         letters = string.ascii_lowercase
#         id = ''.join(random.choice(letters) for i in range(8))
#         while True:
#             ret, frame = cam.read()
#             cv2.imshow("FACE CAPTURE PANEL "+str(passmessage), frame)
#             if not ret:
#                 break
#             k = cv2.waitKey(1)
#             if k % 256 == 27:
#                 # ESC pressed
#                 cam.release()
#                 cv2.destroyAllWindows()
#                 feedback = {
#                     'status': 'Failed',
#                     'msg': 'Terminated',
#                     'classname': 'alert-danger p-2',
#                 }
#                 return JsonResponse(feedback, safe=False)
#
#             elif k % 256 == 32:
#                 # SPACE pressed
#                 user = id
#                 newuser = user.replace('/', '')
#                 img_name = "{}.jpg".format(newuser)
#                 cv2.imwrite('frontend/src/assets/data_test/' + img_name, frame)
#                 image = cv2.imread('frontend/src/assets/data_test/' + img_name)
#                 y = 0
#                 x = 0
#                 h = 256
#                 w = 256
#                 crop_image = image[x:w, y:h]
#                 cv2.imwrite('frontend/src/assets/data_test/' + img_name, crop_image)
#                 img_counter += 1
#
#         if img_counter > 0:
#             feedback = {
#                 'status': 'success',
#                 'statusmsg': 'success',
#                 'msg': 'Image captured',
#                 'classname': 'alert-primary p-2',
#             }
#         else:
#             feedback = {
#                 'status': 'error',
#                 'statusmsg': 'failed',
#                 'msg': '',
#                 'classname': '',
#             }
#         return JsonResponse(feedback, safe=False)
#
#     except Exception as e:
#         feedback = {
#             'status': 'error',
#             'statusmsg': 'failed',
#             'msg': '',
#             'classname': '',
#         }
#
#     return JsonResponse(feedback, safe=False)
#
#
# def evaluate_def(self, *args):
#     category = {
#         '0': 'Healthy',
#         '1': 'Pest Infected',
#         '-1': 'Unidentified',
#         }
#
#     model_location = 'frontend/src/assets/models/ewedu_model_output.h5'
#     rootdir = 'frontend/src/assets/dataset_test/'
#
#     model = load_model(model_location)
#     test_images = []
#     results = []
#     result_ids = []
#     filenames = []
#     for subdir, dirs, files in os.walk(rootdir):
#         for filename in files:
#             img = image.load_img(rootdir + filename, grayscale=False,
#                                  color_mode="rgb", target_size=(256, 256),
#                                  interpolation="nearest")
#
#             img = image.img_to_array(img)
#             img = np.expand_dims(img, axis=0)
#             img = img / 255
#             test_images.append(img)
#             output = model.predict(img)
#             indexes = tf.argmax(output, axis=1)
#             individual = indexes.numpy()
#             results.append(category[str(individual[0])])
#             result_ids.append((individual[0]))
#             filenames.append(filename)
#
#     print(results)
#     print(result_ids)
#
