import os
from django.conf import settings
from django.core.management.base import BaseCommand
from cloudinary.uploader import upload

class Command(BaseCommand):
    help = "Migrate local uploads to Cloudinary and update model fields"

    def handle(self, *args, **options):
        # Blog Post images
        from blog.models import Post
        for post in Post.objects.all():
            if post.image and os.path.exists(post.image.path):
                self.stdout.write(f"Uploading blog post image: {post.image.path}")
                result = upload(post.image.path)
                post.image = result['public_id']
                post.save()

        # Bookstore Book images
        from bookstore.models import Book
        for book in Book.objects.all():
            if book.image and os.path.exists(book.image.path):
                self.stdout.write(f"Uploading book image: {book.image.path}")
                result = upload(book.image.path)
                book.image = result['public_id']
                book.save()

        # Recipes Recipe images and covers
        from recipes.models import Recipe
        for recipe in Recipe.objects.all():
            if recipe.image and recipe.image.path and os.path.exists(recipe.image.path):
                self.stdout.write(f"Uploading recipe image: {recipe.image.path}")
                result = upload(recipe.image.path)
                recipe.image = result['public_id']
                recipe.save()
            if recipe.cover and recipe.cover.path and os.path.exists(recipe.cover.path):
                self.stdout.write(f"Uploading recipe cover: {recipe.cover.path}")
                result = upload(recipe.cover.path)
                recipe.cover = result['public_id']
                recipe.save()

        # Portfolio Project images and modal_images
        from portfolio.models import Project
        for project in Project.objects.all():
            if project.image and os.path.exists(project.image.path):
                self.stdout.write(f"Uploading project image: {project.image.path}")
                result = upload(project.image.path)
                project.image = result['public_id']
                project.save()
            if project.modal_image and os.path.exists(project.modal_image.path):
                self.stdout.write(f"Uploading project modal image: {project.modal_image.path}")
                result = upload(project.modal_image.path)
                project.modal_image = result['public_id']
                project.save()

        # anish0m Contents icons
        from anish0m.models import Contents
        for content in Contents.objects.all():
            if content.icon and os.path.exists(content.icon.path):
                self.stdout.write(f"Uploading contents icon: {content.icon.path}")
                result = upload(content.icon.path)
                content.icon = result['public_id']
                content.save()

        self.stdout.write(self.style.SUCCESS("Migration complete."))