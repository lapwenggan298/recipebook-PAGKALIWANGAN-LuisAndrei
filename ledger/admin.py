from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, Profile
# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine]
    search_fields = ['name']
    list_display = ['name', 'created_on', 'updated_on', 'author']


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['name']
    list_display = ['name']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Profile, ProfileAdmin)