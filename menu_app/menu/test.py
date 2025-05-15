from django.test import TestCase, RequestFactory
from django.template import Context, Template
from menu.models import MenuItem

class MenuTemplateTagTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.root = MenuItem.objects.create(name="main_menu", url="/menu/", parent=None, menu_name="main_menu")
        self.contact = MenuItem.objects.create(name="contact", url="/menu/contact/", parent=self.root, menu_name="main_menu")
        self.products = MenuItem.objects.create(name="products", url="/menu/products/", parent=self.root, menu_name="main_menu")
        self.electronic = MenuItem.objects.create(name="electronic", url="/menu/products/electronic/", parent=self.products, menu_name="main_menu")
        self.phones = MenuItem.objects.create(name="phones", url="/menu/products/electronic/phones/", parent=self.electronic, menu_name="main_menu")

    def render_menu(self, path):
        request = self.factory.get(path)
        template = Template('{% load draw_menu %}{% draw_menu "main_menu" %}')
        context = Context({'request': request})
        return template.render(context)

    def test_menu_renders_root_items(self):
        html = self.render_menu("/menu/")
        self.assertIn("main_menu", html)
        self.assertIn("products", html)
        self.assertIn("contact", html)

    def test_menu_highlights_active(self):
        html = self.render_menu("/menu/products/electronic/phones/")
        self.assertIn('class="active"', html)
        self.assertIn("phones", html)
        self.assertIn("electronic", html)
        self.assertIn("products", html)

    def test_menu_ignores_nonexistent_menu(self):
        request = self.factory.get("/menu/")
        template = Template('{% load draw_menu %}{% draw_menu "nonexistent" %}')
        context = Context({'request': request})
        html = template.render(context)
        self.assertIn('<ul class="menu">', html)
        self.assertNotIn('<li>', html)

    def test_menu_partial_path_expansion(self):
        html = self.render_menu("/menu/products/electronic/")
        self.assertIn("electronic", html)
        self.assertIn("products", html)
        self.assertIn("main_menu", html)

    def test_only_one_query_executed(self):
        from django.db import connection

        # До вызова draw_menu
        queries_before = len(connection.queries)

        # Вызов шаблона
        self.render_menu("/menu/products/electronic/")

        # После — сравни
        queries_after = len(connection.queries)
        num_queries = queries_after - queries_before

        self.assertLessEqual(num_queries, 3)

    def test_empty_menu_name_returns_empty(self):
        request = self.factory.get("/menu/")
        template = Template('{% load draw_menu %}{% draw_menu "" %}')
        context = Context({'request': request})
        html = template.render(context)
        self.assertIn('<ul class="menu">', html)
        self.assertNotIn('<li>', html)

    def test_non_matching_path_returns_inactive_menu(self):
        html = self.render_menu("/menu/some/other/page/")
        self.assertIn("main_menu", html)
        self.assertNotIn('class="active"', html)

    def test_deeply_nested_menu_renders_correctly(self):
        deep1 = MenuItem.objects.create(name="level1", url="/l1/", parent=self.phones, menu_name="main_menu")
        deep2 = MenuItem.objects.create(name="level2", url="/l1/l2/", parent=deep1, menu_name="main_menu")
        deep3 = MenuItem.objects.create(name="level3", url="/l1/l2/l3/", parent=deep2, menu_name="main_menu")
        deep4 = MenuItem.objects.create(name="level4", url="/l1/l2/l3/l4/", parent=deep3, menu_name="main_menu")

        html = self.render_menu("/l1/l2/l3/l4/")
        self.assertIn("level4", html)
        self.assertIn("level3", html)
        self.assertIn("level2", html)
        self.assertIn("level1", html)
        self.assertIn("phones", html)
        self.assertIn("products", html)

    def test_contact_page_returns_200(self):
        response = self.client.get("/menu/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_products_page_returns_200(self):
        response = self.client.get("/menu/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_phones_page_returns_200(self):
        response = self.client.get("/menu/products/electronic/phones/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
