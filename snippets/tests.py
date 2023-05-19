from django.test import TestCase, client, RequestFactory
from django.urls import resolve
from django.contrib.auth import get_user_model

from snippets.views import top, snippet_new, snippet_edit, snippet_detail
from snippets.models import Snippet

UserModel = get_user_model()

class TopPageRenderSnippetTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create(
            username = 'test_user',
            email = 'test@example.com',
            password = 'secret',
        )
        self.client.force_login(self.user)

    def test_render_creation_form(self.user):
        response = self.client.get('/snippets/new/')
        self.assertContains(response, "スニペットの登録", status_code=200)

    def test_create_snippet(self):
        data = {'title': 'タイトル', 'code' 'コード', 'description': '説明'}
        snippet = Snippet.objects.get(title='タイトル')
        self.assertEqual('コード', snippet.code)
        self.assertEqual('説明', snippet.description)