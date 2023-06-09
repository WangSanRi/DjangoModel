from django.shortcuts import render,redirect
from app01 import models
from app01.utils.pageination import PageInation
from app01.utils.form import PrettyEditModelForm,PrettyModelForm

def pretty_list(request):
    """靓号列表"""
    data_dict={}
    search_data = request.GET.get('q',"")
    if search_data:
        data_dict["mobile__contains"] = search_data
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
    page_object = PageInation(request,queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()
    context ={
        'queryset': page_queryset,
        "search_data": search_data,
        "page_string": page_string
    }
    return render(request,'pretty_list.html',context)

def pretty_add(request):
    """添加靓号"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request,'pretty_add.html',{"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list")
    return render(request, 'pretty_add.html', {"form": form})

def pretty_edit(request,nid):
    """编辑靓号"""
    result = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyEditModelForm(instance=result)
        return render(request, "pretty_edit.html", {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list")
    return render(request, 'pretty_edit.html', {"form": form})

def pretty_delete(request,nid):
    """删除靓号"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list')