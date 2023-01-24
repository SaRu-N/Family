from rest_framework import serializers
from . models import Person,GrandFather,GrandMother,Father,Mother,Son,Daughter


class PersonSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    def create(self,validated_data):
        return Person.objects.create(**validated_data)
    def update(self,instance,validate_data):
        instance.name =validate_data.get('name',instance.name)
        instance.save()
        return instance
    
    # class Meta:
    #     model=Person
    #     fields ='__all__'
class GrandFatherSerializer(serializers.ModelSerializer):
    class Meta:
        model=GrandFather
        fields ='__all__'
class GrandMotherSerializer(serializers.ModelSerializer):
    class Meta:
        model=GrandMother
        fields ='__all__'
class FatherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Father
        fields ='__all__'
class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mother
        fields ='__all__'
class SonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Son
        fields ='__all__'
class DaughterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Daughter
        fields ='__all__'