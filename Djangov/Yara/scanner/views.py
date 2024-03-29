from django.shortcuts import render,HttpResponse
from django.http import request
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import requests
import json
from .function import handle_uploaded_file




# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('Successfully uploaded')        
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})


def uploaded_file_handler():
    files = {'file': open('scanner/static/upload/'+f.name, 'rb')}
    r = requests.post('https://yaraify-api.abuse.ch/api/v1/', files=files, verify=True)
    print(r.text)

    response = requests.post('https://yaraify-api.abuse.ch/api/v1/', files=files, verify=True)
    print(response.text)
