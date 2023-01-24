from django.contrib import admin
from . models import Person,GrandFather,GrandMother,Father,Mother,Son,Daughter



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(GrandFather)
class GrandFatherAdmin(admin.ModelAdmin):
    list_display=['id','person']

@admin.register(GrandMother)
class GrandMotherAdmin(admin.ModelAdmin):
    list_display=['id','person']

@admin.register(Father)
class FatherAdmin(admin.ModelAdmin):
    list_display=['id','person','father','mother']

@admin.register(Mother)
class MotherAdmin(admin.ModelAdmin):
    list_display=['id','person','father','mother']

@admin.register(Daughter)
class DaughterAdmin(admin.ModelAdmin):
    list_display=['id','person','grandfather','grandmother','father','mother','brothers','sisters']

@admin.register(Son)
class SonAdmin(admin.ModelAdmin):
    list_display=['id','person','grandfather','grandmother','father','mother','brothers','sisters']