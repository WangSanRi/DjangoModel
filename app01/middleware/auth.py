from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        if request.path_info in ["/login/","/img/code/"]:
            return None

        info_dict = request.session.get("info")
        if info_dict:
            return
        return redirect('/login/')