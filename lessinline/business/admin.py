from django.contrib import admin
from .models import Business, BusinessStaff, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


class StaffInline(admin.TabularInline):
    model = BusinessStaff
    extra = 1


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'category', 'created_at']
    inlines = [StaffInline]
