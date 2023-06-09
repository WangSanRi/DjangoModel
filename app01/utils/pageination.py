from django.utils.safestring import mark_safe
from django.http.request import QueryDict
import copy
class PageInation(object):
    def __init__(self,request,queryset,page_size=10,page_param="page",plus = 2):

        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page=1
        self.page = page
        self.page_param=page_param
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        total = queryset.count()
        total_page, div = divmod(total, page_size)
        if div:
            total_page += 1
        self.total_page = total_page
        self.plus =plus

    def html(self):
        if self.total_page <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page:
                    start_page = self.total_page - 2 * self.plus
                    end_page = self.total_page
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        page_list = []
        self.query_dict.setlist(self.page_param,[1])
        page_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(prev)
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_list.append(ele)

        if self.page < self.total_page:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_list.append(prev)
        self.query_dict.setlist(self.page_param, [self.total_page])
        page_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))
        search_string = """
            <li>
                <form style="float:left;margin-left:-1px" method="get">
                  <input name="page"
                         style="position:relative;float:left;display:inline-block;width:80px;border-radius:0;"
                         type="text" class="form-control" placeholder="页码">
                  <button style="border-radius:0;" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
            """
        page_list.append(search_string)
        page_string = mark_safe("".join(page_list))
        return page_string