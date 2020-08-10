from django.test import TestCase
from .models import post
from django.urls import reverse

class PostModelTest(TestCase):
	def setUp(self):
		post.objects.create(text="just a test")
	
	def Test_text_context(self):
		post = post.objects.get(id=1)
		expected_text = post.text
		self.assertEqual(expected_text, "just a test")

class HomePageViewTest(TestCase):
	def setUp(self):
		post.objects.create(text="this a home page test")

	def test_view_url_redirect_proper_location(self):
		resp = self.client.get("/")
		self.assertEqual(resp.status_code, 200)

	def test_view_url_by_name(self):
		resp = self.client.get(reverse("home"))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse("home"))
		self.assertTemplateUsed(resp, "home.html")


# test for Home page and about when use Template view not List view

#class SimpleTests(SimpleTestCase):
#	def test_home_page_status_code(self):
#		response = self.client.get('/')
#		self.assertEqual(response.status_code, 200)
#	def test_about_page_status_code(self):
#		response = self.client.get('/about/')
#		self.assertEqual(response.status_code, 200)

