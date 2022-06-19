from django.views import generic
from django.urls import reverse_lazy
from .models import Student

class IndexView(generic.ListView):
    template_name = 'students/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """Return all students."""
        return Student.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'students/create.html'
    model = Student
    fields = ['first', 'last', 'email']
    success_url = reverse_lazy('students:index') # more robust than hardcoding to /students/; directs user to index view after adding a student

class UpdateView(generic.edit.UpdateView):
    template_name = 'students/update.html'
    model = Student
    fields = ['first', 'last', 'email']
    success_url = reverse_lazy('students:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'students/delete.html' # override default of students/student_confirm_delete.html
    model = Student
    success_url = reverse_lazy('students:index')
