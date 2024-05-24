# urls.py

from django.urls import path
from .views import home, directory_detail, create_directory, upload_file, download_file

urlpatterns = [
    path('', home, name='home'),
    path('directory/<int:directory_id>/', directory_detail, name='directory_detail'),
    path('directory/create/', create_directory, name='create_directory'),
    path('directory/<int:parent_id>/create_directory/', create_directory, name='create_directory'),
    path('directory/<int:directory_id>/upload_file/', upload_file, name='upload_file'),
    path('download_file/<int:file_id>/', download_file, name='download_file'),
]
