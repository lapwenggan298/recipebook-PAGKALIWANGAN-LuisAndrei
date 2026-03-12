from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Recipe, RecipeImage

from .forms import RecipeForm, RecipeImageForm
# Create your views here.

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
    
    
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    success_url = reverse_lazy('ledger:recipe_list')


class RecipeImageAddView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'image_add.html'

    def form_valid(self, form):
        form.instance.recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recipe_pk'] = self.kwargs['pk']
        return ctx

    def get_success_url(self):
        return reverse_lazy('ledger:recipe_detail', kwargs={'pk':self.kwargs['pk']})