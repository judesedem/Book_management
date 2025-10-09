from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from .forms import BookForm

#Create
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        # If form is invalid, fall through to render with errors
    else:
        form = BookForm()  # GET request: empty form

    return render(request, 'books/add_book.html', {'form': form})

#Read
def book_list(request):
    books=Book.objects.all()
    return render(request, 'books/book_list.html', {'books':books})

#Update
def edit_book(request,pk):
    book=get_object_or_404(Book, pk=pk)
    form=BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request,'books/edit_book.html',{'form': form, 'book':book})

#Delete
def delete_book(request, pk):
    book=get_object_or_404(Book, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request,'books/delete_book.html',{'book':book})


# Create your views here.
