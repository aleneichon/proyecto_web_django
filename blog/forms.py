from django import forms
<<<<<<< HEAD

=======
>>>>>>> 2a24358cbeed6e98fb07b4dac7b4b79ad29addf3
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('title', 'text',)
=======
        fields = ('title', 'text',)

>>>>>>> 2a24358cbeed6e98fb07b4dac7b4b79ad29addf3
