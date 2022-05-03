from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
import cv2
import os
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'dataset.html')

def camera(request):
    if request.method=='POST':
        f_name = request.POST['foldername']
        f_path = request.POST['folderpath']
        try:
            cap = cv2.VideoCapture(0)
            count=0
            # Path
            path = os.path.join(f_path, f_name)
            os.makedirs(path, mode=0o666)

            while True:
                ret,frame=cap.read()
                # print(frame)
                cv2.imshow('live video',frame)
                if (cv2.waitKey(1) & 0xff == ord('c')):
                    cv2.imwrite(path+"\\"+f_name+"_"+str(count) + ".jpg", frame)
                    count += 1
                if (cv2.waitKey(1) & 0xff == ord('q')):
                    break
            messages.success(request, 'Your dataset is successfully created')
            cap.release()
            cv2.destroyAllWindows()

        except:

            messages.info(request, 'Cannot create a file when that file already exists!!!!!!!!')

        return render(request,'dataset.html')