from django.urls import path
from .views import *

app_name = 'apps.posts'

urlpatterns = [
    path('posts/',PostListView.as_view(), name ='posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name= 'post_individual'),
    path('post/', PostCreateView.as_view(), name='post_crear'),
    path('post/categoria', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('categoria', CategoriaListView.as_view(), name='categoria_lista'),
    path('categoria/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('posts/<int:pk>/modificar/', PostUpdateView.as_view(), name='post_modificar'),
    path('posts/<int:pk>/eliminar/', PostDeleteView.as_view(), name='post_eliminar'),
    path('categoria/<int:pk>/posts/', PostsPorCategoriaView.as_view(), name='posts_por_categoria'),
    path('comentario/<int:pk>/modificar/', ComentarioUpdateView.as_view(), name='comentario_modificar'),
    path('comentario/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='comentario_eliminar'),
]
