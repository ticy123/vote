

# 需要登录才能访问的资源路径
from django.http import JsonResponse
from django.shortcuts import redirect

LOGIN_REQUIRED_URLS = {'/praise/', '/criticize/', '/excel/', '/teachers_data/'}

def check_login_middleware(fun):
    def wrapper(request,*args,**kwargs):
        if request.path in LOGIN_REQUIRED_URLS:
            if 'userid' not in request.session:
                if request.is_ajax():
                    return JsonResponse({'code': 10003, 'hint': '请先登录','mesg':'请先登录'})
                else:
                    backurl = request.get_full_path()
                    return redirect(f'/login/?backurl={backurl}')
        return fun(request,*args,**kwargs)
    return wrapper