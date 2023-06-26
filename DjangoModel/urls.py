from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from app01.view import depart,user,pretty,admin,account,order,chart,file
urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT},name='media'),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 登录
    path('login/',account.login),
    # 注销
    path('logout/',account.logout),

    # 验证码
    path('img/code/',account.img_code),

    # 订单管理
    path('order/list/',order.order_list),
    path('order/add/',order.order_add),
    path('order/edit/',order.order_edit),
    path('order/saveEdit/',order.order_saveEdit),
    path('order/delete/',order.order_delete),

    # 文件管理
    path('file/list/',file.file_list),
    path('file/upload/',file.file_upload),
    path('file/<str:name>/delete/',file.file_delete),
    path('file/<str:name>/download/', file.file_download),

    # 数据统计
    path('chart/list/',chart.chart_list),
    path('chart/line/',chart.chart_line),
    path('chart/bar/',chart.chart_bar),
    path('chart/pie/',chart.chart_pie),
]
