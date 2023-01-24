from django.db import models


class Person(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class GrandFather(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.person.name

class GrandMother(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.person.name

class Father(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    father=models.ForeignKey(GrandFather,on_delete=models.CASCADE, related_name='son')
    mother=models.ForeignKey(GrandMother,on_delete=models.CASCADE, related_name='son')
    def __str__(self):
        return self.person.name

class Mother(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    mother=models.ForeignKey(GrandMother,on_delete=models.CASCADE, related_name='daughter')
    father=models.ForeignKey(GrandFather,on_delete=models.CASCADE, related_name='daughter')
    def __str__(self):
        return self.person.name

class Son(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    father=models.ForeignKey(Father,on_delete=models.CASCADE, related_name='son')
    mother=models.ForeignKey(Mother,on_delete=models.CASCADE, related_name='son')
    brother=models.ManyToManyField("self",blank=True)
    sister=models.ManyToManyField("Daughter",related_name='brother')
    grandmother=models.ForeignKey(GrandMother,on_delete=models.CASCADE, related_name='grandson')
    grandfather=models.ForeignKey(GrandFather,on_delete=models.CASCADE, related_name='grandson')
    def sisters(self):
        return ",".join([str(p) for p in self.sister.all()])
    def brothers(self):
        return ",".join([str(p) for p in self.brother.all()])
    def __str__(self):
        return self.person.name

class Daughter(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    father=models.ForeignKey(Father,on_delete=models.CASCADE, related_name='daughter')
    mother=models.ForeignKey(Mother,on_delete=models.CASCADE, related_name='daughter')
    sister=models.ManyToManyField("self",blank=True)
    grandmother=models.ForeignKey(GrandMother,on_delete=models.CASCADE, related_name='granddaughter')
    grandfather=models.ForeignKey(GrandFather,on_delete=models.CASCADE, related_name='granddaughter')
    def sisters(self):
        return ",".join([str(p) for p in self.sister.all()])
    def brothers(self):
        return ",".join([str(p) for p in self.brother.all()])
    def __str__(self):
        return self.person.name