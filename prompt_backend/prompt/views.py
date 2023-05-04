from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import PromptForm
from .models import Prompt, Category
from .serializers import PromptSerializer, PromptDetailSerializer, CategorySerializer


class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class NewestPromptsView(APIView):
    def get(self, request, format=None):
        # 获取最新的 8 个 Prompt 对象
        prompts = Prompt.objects.all()[0:8]
        serializer = PromptSerializer(prompts, many=True)

        return Response(serializer.data)


class MyPromptsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        prompts = Prompt.objects.filter(created_by=request.user)
        serializer = PromptSerializer(prompts, many=True)

        return Response(serializer.data)


class CreatePromptView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = PromptForm(request.data)

        if form.is_valid():
            prompt = form.save(commit=False)
            prompt.created_by = request.user
            prompt.save()

            return Response({'status': 'created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})

    def put(self, request, pk):
        prompt = Prompt.objects.get(pk=pk, created_by=request.user)
        form = PromptForm(request.data, instance=prompt)
        form.save()

        return Response({'status': 'updated'})

    def delete(self, request, pk):
        prompt = Prompt.objects.get(pk=pk, created_by=request.user)
        prompt.delete()

        return Response({'status': 'deleted'})


class BrowsePromptsView(APIView):
    def get(self, request, format=None):
        prompts = Prompt.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')

        if query:
            prompts = prompts.filter(title__icontains=query)

        if categories:
            prompts = prompts.filter(category_id__in=categories.split(','))

        serializer = PromptSerializer(prompts, many=True)

        return Response(serializer.data)


class PromptsDetailView(APIView):
    def get(self, request, pk, format=None):
        prompt = Prompt.objects.get(pk=pk)
        serializer = PromptDetailSerializer(prompt)

        return Response(serializer.data)
