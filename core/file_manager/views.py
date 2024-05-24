# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from .models import Directory, File
from .forms import DirectoryForm, FileForm

def home(request):
    root_directories = Directory.objects.filter(parent__isnull=True)
    return render(request, 'home.html', {'root_directories': root_directories})

def directory_detail(request, directory_id):
    current_directory = get_object_or_404(Directory, id=directory_id)
    subdirectories = current_directory.subdirectories.all()
    files = current_directory.files.all()

    return render(request, 'directory_detail.html', {
        'current_directory': current_directory,
        'subdirectories': subdirectories,
        'files': files,
    })

def create_directory(request, parent_id=None):
    parent_directory = get_object_or_404(Directory, id=parent_id) if parent_id else None

    if request.method == 'POST':
        form = DirectoryForm(request.POST)
        if form.is_valid():
            new_directory = form.save(commit=False)
            new_directory.parent = parent_directory
            new_directory.save()
            if parent_directory:
                return redirect('directory_detail', directory_id=parent_id)
            else:
                return redirect('home')
    else:
        form = DirectoryForm()

    return render(request, 'create_directory.html', {'form': form, 'parent_directory': parent_directory})

def upload_file(request, directory_id):
    directory = get_object_or_404(Directory, id=directory_id)

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.directory = directory
            new_file.save()
            return redirect('directory_detail', directory_id=directory_id)
    else:
        form = FileForm()

    return render(request, 'upload_file.html', {'form': form, 'directory': directory})

def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    return FileResponse(file.file.open(), as_attachment=True, filename=file.name)