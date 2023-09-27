from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse 
from .forms import ImageFieldForm
from .models import ImageField
from .utils import get_hex_value, get_color
from webcolors import hex_to_rgb


# Create your views here.

#home page view
def index(request):
    if request.method == "POST":
        form = ImageFieldForm(request.POST, request.FILES)
        if form.is_valid():
            #if form is valid create new object and save
            data = form.cleaned_data.get("uploaded_image_file")
            hex_val = get_hex_value(data)
            rgb_val = hex_to_rgb(hex_val)
            newIm = ImageField(
                uploaded_image_file=data,
                avg_hex_value=hex_val,
                rgb_val=rgb_val,
                color_name=get_color(rgb_val)
            )
            newIm.save()
            #on success redirect
            return redirect("success")
    else:
        form = ImageFieldForm()
    return render(request, "index.html", {"form": form})


def success(request):
    #on success redirect to the home page
    return HttpResponseRedirect(reverse("index"))


#display all images page
def display(request):
    if request.method == "GET":
        uploaded_images = ImageField.objects.all()
        return render(request, "display.html", {"list_of_images": uploaded_images})

def delete(request, id):
    #delete functionality for an image
    pic = ImageField.objects.get(id=id)
    pic.delete()
    return HttpResponseRedirect(reverse("display"))