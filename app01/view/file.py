from django.shortcuts import render,redirect,HttpResponse
import os
from django.conf import settings
from  django.http import FileResponse

def file_upload(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file_object = request.FILES['file']
            filename, ext = os.path.splitext(file_object.name)
            if ext[1:].lower() not in settings.ALLOWED_EXTENSIONS:
                # 文件类型不符合预期
                return HttpResponse('不支持该类型的文件')
            with open(os.path.join(settings.MEDIA_ROOT, file_object.name), 'wb+') as destination:
                for chunk in file_object.chunks():
                    destination.write(chunk)
    return redirect('/file/list/')

def file_list(request):
    search = str(request.GET.get('q', ''))
    dataList = {}
    i = 0
    # 遍历文件夹下的所有文件和目录
    for dirpath, dirnames, filenames in os.walk(settings.MEDIA_ROOT):
        # 遍历目录下的所有文件
        for filename in filenames:
            if search == '':
                # 输出文件名
                i = i + 1
                dataList[i] = filename
            elif search in filename:
                # 输出文件名
                i = i + 1
                dataList[i] = filename
    return render(request,'file_list.html', {"dataList": dataList})

def file_delete(request,name):
    filepath = os.path.join(settings.MEDIA_ROOT,name)
    if os.path.exists(filepath):  # 如果文件存在
        os.remove(filepath)  # 删除文件
        return redirect('/file/list/')
    else:
        return HttpResponse("删除失败")

def file_download(request,name):
    file_path = os.path.join(settings.MEDIA_ROOT, name)
    if os.path.exists(file_path):
        file_path = os.path.join(settings.MEDIA_ROOT, name)
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'), as_attachment=True,filename=name)
            return response
    return HttpResponse("失败")