from django.test import TestCase, override_settings, Client
from .models import ImageField
from .utils import get_hex_value
from PIL import Image
import tempfile


def get_temp_image(temp_file):
    size = (300, 300)
    color = (0, 255, 0)
    image = Image.new("RGB", size, color)
    image.save(temp_file, "jpeg")
    return temp_file


# Create your tests here.
class ImageModelTest(TestCase):
    def set_up(self):
        self.client = Client()

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_simple_test(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temp_image(temp_file)
        pic = ImageField.objects.create(
            uploaded_image_file=test_image.name, avg_hex_value=get_hex_value(test_image)
        )
        self.assertEqual(len(ImageField.objects.all()), 1)

    """ def test_image_upload(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temp_image(temp_file)
        data = {"image": test_image}
        response = self.client.post("", data, follow=True)
       #image_src = response.context.get("image")
        ImageField.objects.create(
            uploaded_image_file=data, avg_hex_value=get_hex_value(image_src)
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(ImageField.objects.all()), 1) """


class WebPagesTest(TestCase):
    def set_up(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_display_images(self):
        response = self.client.get("/display_images")
        self.assertEqual(response.status_code, 200)
