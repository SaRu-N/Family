from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from .models import Person,GrandFather,GrandMother,Father,Mother,Son,Daughter
from .serializers import PersonSerializer,GrandFatherSerializer,GrandMotherSerializer,FatherSerializer,MotherSerializer,SonSerializer,DaughterSerializer

# Get Family 
@api_view(['GET'])
# @renderer_classes([JSONRenderer])
def getfamily(request,pk):
    try:
        person= Person.objects.get(pk=pk)
    except:
        return HttpResponse("Person Does Not Exist")
    if hasattr(person,'grandfather')==True:
        print("GrandFather")
        per=person.grandfather
        name=per.person.name
        sons=[son.person.name for son in per.son.all() ]
        daughters=[daughter.person.name for daughter in per.daughter.all()]
        grandsons=[grandson.person.name for grandson in per.grandson.all() ]
        granddaughters=[granddaughter.person.name for granddaughter in per.granddaughter.all()]

        data={
            'me':name,
            'sons':sons,
            'daughters':daughters,
            'grandsons':grandsons,
            'granddaughters':granddaughters,

        }
        return JsonResponse(data)
    
    elif hasattr(person,'grandmother')==True:
        print("GrandMother")
        per=person.grandmother
        name=per.person.name
        sons=[son.person.name for son in per.son.all() ]
        daughters=[daughter.person.name for daughter in per.daughter.all()]
        grandsons=[grandson.person.name for grandson in per.grandson.all() ]
        granddaughters=[granddaughter.person.name for granddaughter in per.granddaughter.all()]
        data={
            'me':name,
            'sons':sons,
            'daughters':daughters,
            'grandsons':grandsons,
            'granddaughters':granddaughters,
        }
        return JsonResponse(data)
    elif hasattr(person,'father')==True:
        print("Father")
        per=person.father
        # print(per)
        name=per.person.name
        father=per.father.person.name
        mother=per.mother.person.name
        sons=[son.person.name for son in per.son.all() ]
        daughters=[daughter.person.name for daughter in per.daughter.all()]
        data={
            'me':name,
            'father':father,
            'mother':mother,
            'sons':sons,
            'daughters':daughters,
        }
        return JsonResponse(data)
    elif hasattr(person,'mother')==True:
        print("Mother")
        per=person.mother
        name=per.person.name
        father=per.father.person.name
        mother=per.mother.person.name
        sons=[son.person.name for son in per.son.all() ]
        daughters=[daughter.person.name for daughter in per.daughter.all()]
        data={
            'me':name,
            'father':father,
            'mother':mother,
            'sons':sons,
            'daughters':daughters,
        }
        return JsonResponse(data)
    elif hasattr(person,'son')==True:
        print("Son")
        per=person.son
        name=per.person.name
        grandfather=per.grandfather.person.name
        father=per.father.person.name
        mother=per.mother.person.name
        brothers=[brother.person.name for brother in per.brother.all() ]
        sisters=[sister.person.name for sister in per.sister.all()]
        data={
            'me':name,
            'grandfather':grandfather,
            'father':father,
            'mother':mother,
            'brothers':brothers,
            'sisters':sisters,
        }
        return JsonResponse(data)
    elif hasattr(person,'daughter')==True:
        print("Daughter")
        per=person.daughter
        name=per.person.name
        father=per.father.person.name
        mother=per.mother.person.name
        brothers=[brother.person.name for brother in per.brother.all() ]
        sisters=[sister.person.name for sister in per.sister.all()]
        data={
            'me':name,
            'father':father,
            'mother':mother,
            'brothers':brothers,
            'sisters':sisters,
        }
        return JsonResponse(data)
    
    return HttpResponse("Person does not have any family!!")

# Home Page
def home(request):
    return render(request, 'home.html')

# Person
@api_view(['GET','POST','PUT','PATCH','Delete'])
def person_api(request,pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            per=Person.objects.get(id=id)
            serializer =PersonSerializer(per)
            return Response(serializer.data)
        per=Person.objects.all()
        serializer =PersonSerializer(per,many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer=PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person Created'})
        return Response(serializer.errors)
    
    if request.method == "PUT":
        id=pk
        per=Person.objects.get(pk=id)
        serializer=PersonSerializer(per,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person Updated Completely'})
        return Response(serializer.errors)
    if request.method == "PATCH":
        id=pk
        per=Person.objects.get(pk=id)
        serializer=PersonSerializer(per,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Person Updated Partially'})
        return Response(serializer.errors)
    if request.method == "DELETE":
        id=pk
        per=Person.objects.get(pk=id)
        per.delete()
        return Response({'msg':'Person Deleted'})
# GrandFather
@api_view(['GET','POST','PUT','PATCH','Delete'])
def grandfather_api(request,pk=None):
    if request.method == "GET":
        id=pk
        if id is not None:
            gf=GrandFather.objects.get(id=id)
            serializer=GrandFatherSerializer(gf)
            return Response(serializer.data)
        gf=GrandFather.objects.all()
        serializer=GrandFatherSerializer(gf,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer=GrandFatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Grandfather Added'})
        return Response(serializer.errors)
    if request.method == "PUT":
        id=pk
        gf=GrandFather.objects.get(pk=id)
        serializer=GrandFatherSerializer(gf,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'GrandFather Updated Completely'})
        return Response(serializer.errors)
    if request.method == "PATCH":
        id=pk
        gf=GrandFather.objects.get(pk=id)
        serializer=GrandFatherSerializer(gf,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'GrandFather Updated Partially'})
        return Response(serializer.errors)
    if request.method == "DELETE":
        id=pk
        gf=GrandFather.objects.get(pk=id)
        gf.delete()
        return Response({'msg':'Grandfather Deleted'})
# GrandMother
@api_view(['GET','POST','PUT','PATCH','Delete'])
def grandmother_api(request,pk=None):
    if request.method == "GET":
        id=pk
        if id is not None:
            gm=GrandMother.objects.get(id=id)
            serializer=GrandMotherSerializer(gm)
            return Response(serializer.data)
        gm=GrandMother.objects.all()
        serializer=GrandFatherSerializer(gm,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer=GrandMotherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Grandmother Added'})
        return Response(serializer.errors)
    if request.method == "PUT":
        id=pk
        gm=GrandMother.objects.get(pk=id)
        serializer=GrandMotherSerializer(gm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Grandmother Updated Completely'})
        return Response(serializer.errors)
    if request.method == "PATCH":
        id=pk
        gm=GrandMother.objects.get(pk=id)
        serializer=GrandMotherSerializer(gm,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Grandmother Updated Partially'})
        return Response(serializer.errors)
    if request.method == "DELETE":
        id=pk
        gm=GrandMother.objects.get(pk=id)
        gm.delete()
        return Response({'msg':'Grandmother Deleted'})
# Father
@api_view(['GET','POST','PUT','PATCH','Delete'])
def father_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            father=Father.objects.get(id=id)
            serializer=FatherSerializer(father)
            return Response(serializer.data)
        father=Father.objects.all()
        serializer=FatherSerializer(father,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=FatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Father Added"})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        father=Father.objects.get(pk=id)
        serializer=FatherSerializer(father,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Father Updated Completely"})
        return Response(serializer.errors)
    if request.method=="PATCH":
        id=pk
        father=Father.objects.get(pk=id)
        serializer=FatherSerializer(father,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Father Updated Partially"})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        father=Father.objects.get(pk=id)
        father.delete()
        return Response({'msg':"father removed"})
# Mother
@api_view(['GET','POST','PUT','PATCH','Delete'])
def mother_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            mother=Mother.objects.get(id=id)
            serializer=MotherSerializer(mother)
            return Response(serializer.data)
        mother=Mother.objects.all()
        serializer=MotherSerializer(mother,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=MotherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Mother Added"})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        mother=Mother.objects.get(pk=id)
        serializer=MotherSerializer(mother,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Mother Updated Completely"})
        return Response(serializer.errors)
    if request.method=="PATCH":
        id=pk
        mother=Mother.objects.get(pk=id)
        serializer=MotherSerializer(mother,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Mother Updated Partially"})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        mother=Mother.objects.get(pk=id)
        mother.delete()
        return Response({'msg':"Mother removed"})

# Son
@api_view(['GET','POST','PUT','PATCH','Delete'])
def son_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            son=Son.objects.get(id=id)
            serializer=SonSerializer(son)
            return Response(serializer.data)
        son=Son.objects.all()
        serializer=SonSerializer(son,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=SonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Son Added"})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        son=Son.objects.get(pk=id)
        serializer=SonSerializer(son,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Son Updated Completely"})
        return Response(serializer.errors)
    if request.method=="PATCH":
        id=pk
        son=Son.objects.get(id=id)
        serializer=SonSerializer(son,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Son Updated Partially"})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        son=Son.objects.get(pk=id)
        son.delete()
        return Response({'msg':"Son Removed"})
    
# Daughter
@api_view(['GET','POST','PUT','PATCH','Delete'])
def daughter_api(request,pk=None):
    if request.method=="GET":
        id=pk
        if id is not None:
            daughter=Daughter.objects.get(id=id)
            serializer=DaughterSerializer(daughter)
            return Response(serializer.data)
        daughter=Daughter.objects.all()
        serializer=DaughterSerializer(daughter,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=DaughterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Daughter Added"})
        return Response(serializer.errors)
    if request.method=="PUT":
        id=pk
        daughter=Daughter.objects.get(pk=id)
        serializer=DaughterSerializer(daughter,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Daughter Updated Completely"})
        return Response(serializer.errors)
    if request.method=="PATCH":
        id=pk
        daughter=Daughter.objects.get(pk=id)
        serializer=DaughterSerializer(daughter,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Daughter Updated Partially"})
        return Response(serializer.errors)
    if request.method=="DELETE":
        id=pk
        daughter=Daughter.objects.get(pk=id)
        daughter.delete()
        return Response({'msg':"Daughter Removed"})



