from django.db import models
from student.models import Student
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_images/')
    pdf = models.FileField(upload_to='book_pdfs/')
    description = models.TextField()

    def __str__(self):
        return self.title
    


class FavoriteBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} added {self.book} to favorites"

