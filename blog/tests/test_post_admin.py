from django.contrib import admin

from blog.admin import PostAdmin
from blog.models import Post


def test_post_is_registered_in_django_admin():
    assert admin.site.is_registered(Post)
    assert isinstance(admin.site._registry[Post], PostAdmin)


def test_post_admin_list_display():
    post_admin = admin.site._registry[Post]

    assert post_admin.list_display == (
        "title",
        "author",
        "published",
        "created_at",
    )
