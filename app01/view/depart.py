from django.shortcuts import render,redirect
from app01 import models
from app01.utils.pageination import PageInation


def depart_list(request):
    """部门列表"""
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["title__contains"] = search_data
    queryset = models.Department.objects.filter(**data_dict)
    page_object = PageInation(request, queryset)
    context = {
        'queryset': queryset,
        'page_string': page_object.html(),
        "search_data": search_data,
    }
    return render(request,"depart_list.html",context)

def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request,"depart_add.html")

    # 获取用户POST方式提交的数据
    title = request.POST.get("title")

    # 保存到数据库
    models.Department.objects.create(title=title)

    return redirect("/depart/list")

def depart_delete(request):
    """删除部门"""
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")

def depart_edit(request,nid):
    """编辑部门"""
    if request.method == "GET":
        result = models.Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html",{"result":result})

    # 获取用户POST方式提交的数据
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list")
