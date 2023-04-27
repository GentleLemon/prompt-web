from django.urls import path

from . import views


urlpatterns = [
    path('', views.BrowsePromptsView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('my/', views.MyPromptsView.as_view()),
    path('create/', views.CreatePromptView.as_view()),
    path('newest/', views.NewestPromptsView.as_view()),
    path('<int:pk>/', views.PromptsDetailView.as_view()),
    path('<int:pk>/delete/', views.CreatePromptView.as_view()),
    path('<int:pk>/edit/', views.CreatePromptView.as_view()),
]
