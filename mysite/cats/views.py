from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Breed, Cat
from cats.forms import MakeForm

# Create your views here.

class CatList(LoginRequiredMixin, View) :
    def get(self, request):
        bc =Breed.objects.all().count();
        cl =Cat.objects.all();

        count = { 'breed_count': bc, 'cat_list': cl };
        return render(request, 'cats/cats_list.html', count)

class BreedView(LoginRequiredMixin,View) :
    def get(self, request):
        bc = Breed.objects.all();
        count = { 'breed_list': bc };
        return render(request, 'cats/breed_list.html', count)

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded
class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')
    def get(self, request) :
        form = MakeForm()
        count = { 'form': form }
        return render(request, self.template, count)

    def post(self, request) :
        form = MakeForm(request.POST)
        if not form.is_valid() :
            count = {'form' : form}
            return render(request, self.template, count)

        breed=form.save()
        return redirect(self.success_url)

# MakeUpdate has code to implement the get/post/validate/store flow
# AutoUpdate (below) is doing the same thing with no code
# and no form by extending UpdateView
class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_form.html'
    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=breed)
        count = { 'form': form }
        return render(request, self.template, count)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance = breed)
        if not form.is_valid() :
            count= {'form' : form}
            return render(request, self.template, count)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=breed)
        count = { 'breed': breed }
        return render(request, self.template, count)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')