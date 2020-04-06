from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from django import forms
import cv2
try: 
    from src.output import cartoonifier as c
    _task1 = 0
except ModuleNotFoundError:
    print("ISSUES WITH IMPORT OUTPUT.PY")
    _task1 = 1
import matplotlib.pyplot as plt
import imageio
from django.shortcuts import render

upload_path = 'cartoonifier\\static\\upload.png'
output_path = 'cartoonifier\\static\\output.png'


class UploadFileForm(forms.Form):
    file = forms.FileField()

def handle_uploaded_file(f):
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
@csrf_exempt
def cartoon(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            handle_uploaded_file(request.FILES['file'])
            imageio.imwrite(output_path,c(upload_path))

            img = Image.open(output_path)

            response = HttpResponse(content_type="image/png")
            img.save(response,'png')
            return render(request,"index.html",{'done':1,'task1':_task1})
        return HttpResponse("There was some issue in uploading the image. Try uploading again.")
    else:
        return render(request,"index.html",{'done':0,'task1':_task1})


#  The following code has been copy pasted from above. You have 
#  to manipulate the code below such that instead of sending a 
#  cartoonified image it sends back a black and white image

@csrf_exempt
def bw(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            handle_uploaded_file(request.FILES['file'])
            imageio.imwrite(output_path,c(upload_path))

            img = Image.open(output_path)

            response = HttpResponse(content_type="image/png")
            img.save(response,'png')
            return render(request,"index.html",{'done':1,'task1':_task1})
        return HttpResponse("There was some issue in uploading the image. Try uploading again.")
    else:
        return render(request,"index.html",{'done':0,'task1':_task1})
