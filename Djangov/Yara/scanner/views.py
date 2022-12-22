from django.shortcuts import render
from django.http import request
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage



# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'upload.html', {
                'form': form,
                'uploaded_file_url': uploaded_file_url
            })
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})