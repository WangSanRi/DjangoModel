from app01 import models
from django.shortcuts import render,redirect
from app01.utils.pageination import PageInation
from app01.utils.form import AdminModelForm,AdminResetModelForm
def admin_list(request):
    """管理员列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = PageInation(request,queryset)
    context = {
        'queryset': queryset,
        'page_string': page_object.html(),
        "search_data": search_data,
    }
    return render(request,'admin_list.html',context)

def admin_add(request):
    """新建管理员"""
    if request.method == "GET":
        form = AdminModelForm()
        return render(request,'common.html',{"form":form,"title":"新建管理员"})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'common.html', {"form": form, "title": "新建管理员"})

def admin_edit(request,nid):
    """编辑管理员"""
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')

    if request.method == "GET":
        form = AdminModelForm(instance=row_object)
        return render(request, 'common.html', {"form": form, "title": "编辑管理员"})

    form = AdminModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'common.html', {"form": form, "title": "编辑管理员"})

def admin_delete(request,nid):
    """删除管理员"""
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list')

def admin_reset(request,nid):
    """重置密码"""
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    title = "重置密码-{}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'common.html', {"form": form, "title":title })

    form = AdminResetModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'common.html', {"form": form, "title": title})