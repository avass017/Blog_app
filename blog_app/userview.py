from django.contrib.auth import logout
from django.shortcuts import render, redirect

from blog_app.forms import UsersRegister, BlogRegister
from blog_app.models import Users, Blog


def my_profile(request):
    data = request.user
    # print(data.id)
    my_profile = Users.objects.get(users_detail=data.id)
    # print(passenger_profile.phone)
    return render(request,"users/profile.html",{"data":my_profile})

def user_edit(request):

    user=request.user
    users=Users.objects.get(users_detail=user)

    if request.method == "POST":
        use_form = UsersRegister(request.POST,request.FILES,instance=users)
        if use_form.is_valid():
            use_form.save()
            return redirect('my_profile')
    else:
        use_form = UsersRegister(instance=users)
    return render(request,"users/update_profile.html",{"data":use_form})

def Log_out(request):
    logout(request)
    return redirect('users')



def blog_add(request):

    if request.method == "POST":
        form = BlogRegister(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)


            user_profile = Users.objects.get(users_detail=request.user)

            blog.blog_detail = user_profile
            blog.save()

            return redirect('blog_view')

    else:
        form = BlogRegister()

    return render(request, 'users/blog.html', {'form': form})

def blog_list(request):
    data=Blog.objects.all()
    return render(request,'users/blog_list.html',{'data':data})

def blog_view(request):
    user = Users.objects.get(users_detail=request.user)
    data = Blog.objects.filter(blog_detail=user)
    return render(request,'users/blog_view.html',{'data':data})

def blog_update(request,id):
    blog_up=Blog.objects.get(id=id)

    if request.method == "POST":
        up_form = BlogRegister(request.POST,instance=blog_up)
        if up_form.is_valid():
            up_form.save()
            return redirect('blog_view')
    else:
        form = BlogRegister(instance=blog_up)

    return render(request,'users/update_blog.html',{'data':form})

def blog_delete(request,id):
    blog_del=Users.objects.get(id=id)
    blog_del.delete()
    return redirect('blog_view')