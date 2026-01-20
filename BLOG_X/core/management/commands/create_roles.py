from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post, Comment
class Command(BaseCommand):
    help = 'Create default roles: Admin, Author, Reader'
    def handle(self, *args, **options):
        admin, _ = Group.objects.get_or_create(name='Admin')
        author, _ = Group.objects.get_or_create(name='Author')
        reader, _ = Group.objects.get_or_create(name='Reader')
        # give author add/change/delete post perms
        ct = ContentType.objects.get_for_model(Post)
        perms = Permission.objects.filter(content_type=ct)
        for p in perms:
            author.permissions.add(p)
        self.stdout.write('Roles created/updated')
