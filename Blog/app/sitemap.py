from django.contrib.sitemaps import Sitemap
from.models import Post ,Category # Assuming you have a Post model

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated  # Use the updated field

    def location(self, obj):
        return f"/post/{obj.slug}"
    

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated  # Use the updated field

    def location(self, obj):
        return f"/category/{obj.name}"