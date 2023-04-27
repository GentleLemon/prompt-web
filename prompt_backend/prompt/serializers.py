from rest_framework import serializers

from .models import Prompt, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title',)


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = (
            'id',
            'title',
            'description',
            'position_salary',
            'position_location',
            'company_name',
            'created_at_formatted'
        )


class PromptDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = (
            'id',
            'category',
            'title',
            'description',
            'position_salary',
            'position_location',
            'company_name',
            'company_location',
            'company_email',
            'created_at_formatted'
        )