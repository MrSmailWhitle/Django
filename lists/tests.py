from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
	def test_resolve_homepage_rootview(self):
		found=resolve('/')
		self.assertEqual(found.func,home_page)
	def test_home_page_return_correct_html(self):
		request=HttpRequest()
		response=home_page(request)
		html=response.content.decode('utf-8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do Lists</title>',html)
		self.assertTrue(html.endswith('</html>'))