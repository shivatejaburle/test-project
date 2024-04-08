from django.forms import models

from posts.models import Post

class AddPost(models.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'