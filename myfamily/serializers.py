from rest_framework import serializers
from . models import Person,GrandFather,GrandMother,Father,Mother,Son,Daughter


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields ='__all__'

class GrandFatherSerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(read_only=True)
    daughter=serializers.StringRelatedField(many=True,read_only=True)
    son=serializers.StringRelatedField(many=True,read_only=True)
    granddaughter=serializers.StringRelatedField(many=True,read_only=True)
    grandson=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=GrandFather
        fields =['id','person','son','daughter','grandson','granddaughter']
class GrandMotherSerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(read_only=True)
    daughter=serializers.StringRelatedField(many=True,read_only=True)
    son=serializers.StringRelatedField(many=True,read_only=True)
    granddaughter=serializers.StringRelatedField(many=True,read_only=True)
    grandson=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=GrandMother
        fields =['id','person','son','daughter','grandson','granddaughter']
class FatherSerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(read_only=True)
    father=serializers.StringRelatedField(read_only=True)
    mother=serializers.StringRelatedField(read_only=True)
    daughter=serializers.StringRelatedField(many=True,read_only=True)
    son=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Father
        fields =['id','person','father','mother','son','daughter']
class MotherSerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(read_only=True)
    father=serializers.StringRelatedField(read_only=True)
    mother=serializers.StringRelatedField(read_only=True)
    daughter=serializers.StringRelatedField(many=True,read_only=True)
    son=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Mother
        fields =['id','person','father','mother','son','daughter']
class SonSerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(read_only=True)
    father=serializers.StringRelatedField(read_only=True)
    mother=serializers.StringRelatedField(read_only=True)
    grandfather=serializers.StringRelatedField(read_only=True)
    grandmother=serializers.StringRelatedField(read_only=True)
    brother=serializers.StringRelatedField(many=True,read_only=True)
    sister=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Son
        fields ='__all__'
class DaughterSerializer(serializers.ModelSerializer):
    person=serializers.StringRelatedField(read_only=True)
    father=serializers.StringRelatedField(read_only=True)
    mother=serializers.StringRelatedField(read_only=True)
    grandfather=serializers.StringRelatedField(read_only=True)
    grandmother=serializers.StringRelatedField(read_only=True)
    brother=serializers.StringRelatedField(many=True,read_only=True)
    sister=serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model=Daughter
        fields ='__all__'