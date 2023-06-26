from django.shortcuts import render
from django.http import JsonResponse

def chart_list(request):
    """数据统计界面"""
    return render(request,'chart_list.html')

def chart_line(request):
    """构造折线图数据"""
    legend = ['广州', '深圳']
    xAxis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
    data_list = [
                {
                  "name": '广州',
                  "type": 'line',
                  "stack": 'Total',
                  "data": [120, 132, 141, 154, 90, 230, 220]
                },
                {
                  "name": '深圳',
                  "type": 'line',
                  "stack": 'Total',
                  "data": [220, 182, 191, 234, 290, 330, 310]
                }
    ]
    result = {
        "status":True,
        "data":{
            "legend":legend,
            "xAxis":xAxis,
            "data_list":data_list
        }
    }
    return JsonResponse(result)

def chart_bar(request):
    """构造柱状图数据"""
    legend = ['zhuzhu','yyds']
    xAxis = ['1月', '2月', '3月', '4月', '5月', '6月']
    data_list = [
              {
                "name": 'zhuzhu',
                "type": 'bar',
                "data": [15, 20, 36, 10, 10, 68]
              },
              {
                "name": 'yyds',
                "type": 'bar',
                "data": [45, 10, 66, 40, 20, 10]
              }
    ]
    result = {
        "status":True,
        "data":{
            "legend":legend,
            "xAxis":xAxis,
            "data_list":data_list
        }
    }
    return JsonResponse(result)

def chart_pie(request):
    """构造饼形图数据"""
    data_list =  [
        { "value": 1048, "name": '信息部' },
        { "value": 735, "name": '运营部' },
        { "value": 580, "name": '销售部' },
        { "value": 484, "name": '新媒体' },
    ]
    result = {
        "status":True,
        "data":data_list
    }
    return JsonResponse(result)