from django.shortcuts import render,redirect
from app01 import models
from app01.utils.form import UserModelForm
from app01.utils.pageination import PageInation


def user_list(request):
    """用户列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.UserInfo.objects.filter(**data_dict)
    page_object = PageInation(request, queryset)
    context = {
        'queryset': queryset,
        'page_string': page_object.html(),
        "search_data": search_data,
    }
    return render(request, "user_list.html",context)

def user_add(request):
    """添加用户"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request,'user_add.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    return render(request, 'user_add.html', {"form": form})

def user_edit(request,nid):
    """编辑用户"""
    result = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=result)
        return render(request,"user_edit.html",{"form": form})
    form = UserModelForm(data=request.POST,instance=result)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    return render(request, 'user_edit.html', {"form": form})

def user_delete(request,nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')