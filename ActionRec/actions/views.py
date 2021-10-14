import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.shortcuts import render
from .forms import VideoForm
from .predictAction import prediction

def home(request):
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            # print("hiii")
            video_name = form.cleaned_data['video']
            # print(video_name)
            path = default_storage.save('tmp/demo.avi', ContentFile(video_name.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            y_pred = prediction(tmp_file)
            # print(y_pred)
            context = {
                'action' : y_pred,
                'video_name': video_name,
            }
            return render(request, 'actions/result.html', context)

    else:
        form = VideoForm()

    return render(request, 'actions/index.html', {'form': form})
