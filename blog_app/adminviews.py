from django.shortcuts import render, redirect

from blog_app.models import Users, Blog


def users_view(request):
    data = Users.objects.all()
    return render(request, 'admin/user_details.html', {"data":data})

def user_delete(request,id):
    use_del=Users.objects.get(id=id)
    use_del.delete()
    return redirect('users_view')


def blog_list_admin(request):
    data=Blog.objects.all()
    return render(request,'admin/blog_list.html',{'data':data})
