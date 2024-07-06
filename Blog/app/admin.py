# from django.contrib import admin
# from .models import Post,Category, Comment
# from .schema_generator import SchemaMarkupGenerator






# # Register your models here.
# # admin.site.register(Post)
# admin.site.register(Category)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display=('title' , 'slug' ,'author','section', 'status')
#     list_filter=('status' , 'created' ,'author', )
#     search_fields =('title',)
#     # prepopulated_fields={'slug':('title',)} // this will write the slug automatically as the title  
#     raw_id_fields=('author',)  #this is to search the author if the website contain more than on author
#     date_hierarchy='created'
#     ordering=('status', '-created') # this will order the posts by status and then by created
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'post')
#     search_fields = ('name', 'email', 'content')
#     actions = ['approve_comments', 'delete_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)
#     approve_comments.short_description = "Approve selected comments"

#     def delete_comments(self, request, queryset):
#         queryset.delete()
#     delete_comments.short_description = "Delete selected comments"

# admin.site.register(Comment, CommentAdmin)
# @admin.action(description='Generate Schema Markup')
# def generate_schema_markup(modeladmin, request, queryset):
#     for post in queryset:
#         generator = SchemaMarkupGenerator()
#         generator.set_headline(post.title)
#         generator.set_description(post.excerpt)
#         generator.set_author(post.author.username)
#         generator.set_date_published(post.published_date.strftime("%Y-%m-%d"))
#         generator.set_image(post.image.url if post.image else "")
#         generator.set_publisher("Your Site Name", "/path/to/logo.png")
#         generator.set_main_entity_of_page(f"{request.build_absolute_uri(post.get_absolute_url())}")

#         schema_json = generator.get_schema()
#         # Here you could save the schema JSON to the model or do something else with it
#         print(schema_json)

# class BlogPostAdmin(admin.ModelAdmin):
#     actions = [generate_schema_markup]
# admin.site.register(Post, BlogPostAdmin)




# admin.py
from django.contrib import admin
from .models import Post, Category, Comment
from .schema_generator import SchemaMarkupGenerator
from .content_optimizer import ContentOptimizer
from django.contrib.sitemaps import views as sitemap_views
from .sitemap import PostSitemap


@admin.action(description='Generate Schema Markup')
def generate_schema_markup(modeladmin, request, queryset):
    for post in queryset:
        generator = SchemaMarkupGenerator()
        generator.set_headline(post.title)
        generator.set_description(post.content)
        generator.set_author(post.author.username)
        generator.set_date_published(post.published.strftime("%Y-%m-%d"))
        generator.set_image(post.post_img.url if post.post_img else "")
        generator.set_publisher("Your Site Name", "/path/to/logo.png")
        generator.set_main_entity_of_page(f"{request.build_absolute_uri(post.get_absolute_url())}")

        schema_json = generator.get_schema()
        post.schema_json = schema_json
        post.save()
        print(schema_json)

@admin.action(description='Optimize Content')
def optimize_content(modeladmin, request, queryset):
    for post in queryset:
        optimizer = ContentOptimizer(post.content)
        suggestions = optimizer.analyze()
        
        if suggestions:
            for suggestion in suggestions:
                modeladmin.message_user(request, suggestion)
        else:
            modeladmin.message_user(request, "No suggestions. Your content looks great!")

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'section', 'status')
    list_filter = ('status', 'created', 'author', )
    search_fields = ('title',)
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('status', '-created')
    actions = [generate_schema_markup, optimize_content]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'post')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments', 'delete_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
    approve_comments.short_description = "Approve selected comments"

    def delete_comments(self, request, queryset):
        queryset.delete()
    delete_comments.short_description = "Delete selected comments"
