from django import forms




class ImageFieldForm(forms.Form):
    #use built in Form field to upload images 
    uploaded_image_file = forms.ImageField(
        widget=forms.FileInput(attrs={"class": "form-control form-control-sm"})
    )
