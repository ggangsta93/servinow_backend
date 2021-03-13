from rest_framework import serializers
from .models import Category, Skill

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validate_data):
        instance = Category.objects.create(**validate_data)
        return instance

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

    def create(self, validate_data):
        instance = Skill.objects.create(**validate_data)
        return instance