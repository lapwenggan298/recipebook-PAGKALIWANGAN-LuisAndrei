from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage
# Register your models here.

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInLine(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInLine, RecipeImageInLine,]
    search_fields = ['name']
    list_display = ['name', 'author', 'created_on', 'updated_on']


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ['name']
    list_display = ['name']


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['name']
    list_display = ['name']


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ['image_description']
    search_fields = ['image_description']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)