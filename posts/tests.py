from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

# Create your tests here.


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user1 = User.objects.create_user(
            username="testuser1", password="abc1234")
        test_user1.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=test_user1, title="Blog title", content="Body content ...")
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        content = f'{post.content}'

        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(content, 'Body content ...')
