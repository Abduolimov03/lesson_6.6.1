from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView
from django.shortcuts import render
from .models import Car

class CarList(View):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            cars = Car.objects.filter(model__icontains=query)
        else:
            cars = Car.objects.all().order_by('-id')
        return render(request, 'car_list.html', {'cars': cars, 'query': query})

# class CarDetail(DetailView):
#     model = Car
#     template_name = 'car_detail.html'
#     context_object_name = 'car'

class CarDetail(View):
    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        return render(request, 'car_detail.html', {'car':car})





#
# class CarCreate(CreateView):
#     model = Car
#     form_class = CarForm
#     template_name = 'car_create.html'
#     success_url = reverse_lazy('car')

class CarCreate(View):
    def get(self, request):
        form = CarForm()
        return render(request, 'car_create.html', {'form':form})

    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car')
        return render(request, 'car_create.html', {'form':form})


# class CarUpdate(UpdateView):
#     model = Car
#     form_class = CarForm
#     template_name = 'car_update.html'
#     success_url = reverse_lazy('car')

class CarUpdate(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        form = CarForm(instance=car)
        return render(request, 'car_update.html', {'form':form})

    def post(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car-detail', car.id)
        else:
            form = CarForm(instance=car)
        return render(request, 'car_update.html', {'form':form})

# class CarDetail(View):
#     def get(self, request, pk):
#         car = Car.objects.get(id=pk)
#         return render(request, 'car_detail.html', {'car':car})
#





class CarDelete(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        return render(request, 'car_delete.html', {'car':car})

    def post(self, request, pk):
        car = get_object_or_404(Car, id=pk)
        car.delete()
        return redirect(reverse_lazy('car'))

