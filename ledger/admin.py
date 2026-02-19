from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient
# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)