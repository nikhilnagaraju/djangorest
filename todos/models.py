from django.db import models


# class TodoList(models.Model) :
#     title = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now=True)
#     duedate = models.DateTimeField(null=True)
#     completed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ('duedate',)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    duedate = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    # todolist = models.ForeignKey(TodoList, related_name="items", on_delete=models.CASCADE )
    # todolist = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        """A string representation of the model."""
        return self.title

    

    class Meta:
        ordering = ('duedate',)

    def close(self):
        self.is_finished = True
        self.save()

    def reopen(self):
        self.is_finished = False
        self.save()