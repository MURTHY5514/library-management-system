from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic.base import TemplateView
from .models import Book
from .forms import BookModelForm,SignUpForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.views.generic.base import View
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView


# Create your views here.
class SignUpView(FormView):
    template_name='app/signup.html'
    form_class=SignUpForm
    success_url=reverse_lazy('login')
    
    def form_valid(self,form):
        form.save()
        messages.success(self.request, f'User signup successfully')
        return super().form_valid(form)

class LogInView(FormView):
    template_name='app/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('book_list_view')
    
    def form_valid(self, form: Any):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(self.request,user)
            messages.success(self.request, f'User {username} logged in successfully')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid username or password')
            return self.form_invalid(form)
    
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('book_list_view'))
        else:
            return super().get(request, *args, **kwargs)
        
class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,'User logged out Successfully')
        return redirect(reverse('login'))



# CRUD Opeartions
@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
class BookListView(TemplateView):
    template_name="app/book_list.html"
    
    def get_context_data(self, **kwargs: Any):
        context= super().get_context_data(**kwargs)
        form=BookModelForm()
        books=Book.objects.all()
        context={'books':books,'form':form}
        return context
    
    def post(self,request):
        form = BookModelForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request,'Book added Successfully')
           return redirect(reverse('book_list_view'))
        else:
            messages.error(request, 'Error While adding book')
            books=Book.objects.all()
            return render(request, self.template_name, {'form': form,'books':books})
       

@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
class BookUpdateView(View):
    def get(self,request,id):
        pi=Book.objects.get(pk=id)
        fm=BookModelForm(instance=pi)
        return render(request,'app/update.html',{'form':fm,'id':id})
    
    def post(self,request,id):
        pi=Book.objects.get(pk=id)
        fm=BookModelForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Book Updated Successfully')
            return render(request,'app/update.html',{'form':fm,'id':id})
        else:
            messages.error(request, 'Error While updating book')
            return render(request,'app/update.html' , {'form': fm,'id':id})
    

@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
class BookDeleteView(RedirectView):
    def get_redirect_url(self, *args: Any, **kwargs):
        del_id=kwargs['id']
        book=Book.objects.get(pk=del_id)
        book.delete()
        messages.success(self.request, f'Book "{book.title}" deleted successfully.')
        return reverse('book_list_view')
    
    
@method_decorator(login_required(login_url=reverse_lazy('login')),name='dispatch')
class BookDetailView(DetailView):
    template_name='app/book_detail.html'
    context_object_name='book'
    model=Book


class Custom404View(TemplateView):
    template_name = 'app/404.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.status_code = 404
        return response
    
    