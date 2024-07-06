from django.test import TestCase
from django.urls import reverse
from .models import News_post

# Create your tests here.

#News_post modelga test
class PostModelTest(TestCase):
  def setUp(self):
    News_post.objects.create(title= 'Mavzu', text = 'Yangilik', author = 'Javlonbek')

  def test_text_content(self):
    post = News_post.objects.get(id=1)
    expected_object_title = f'{post.title}'
    expected_object_text = f'{post.text}'
    expected_object_author = f'{post.author}'
    self.assertEqual(expected_object_title, 'Mavzu')
    self.assertEqual(expected_object_text, 'Yangilik')
    self.assertEqual(expected_object_author, 'Javlonbek')

#HomePageView ga test

class HomePageViewTest(TestCase):
  def setUp(self):
    News_post.objects.create(title = 'Mavzu2', text = 'Yangilik2', author = 'Sarvarbek')

  def test_views_urls_exists(self):
    resp = self.client.get('/')
    self.assertEqual(resp.status_code, 200)

  def test_view_url_by_name(self):
    resp = self.client.get(reverse('home'))
    self.assertEqual(resp.status_code, 200)

  def test_view_uses_correct_template(self):
    resp = self.client.get(reverse('home'))
    self.assertEqual(resp.status_code, 200)
    self.assertTemplateUsed(resp, 'home.html')