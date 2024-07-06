import json

class SchemaMarkupGenerator:
    def __init__(self, context="https://schema.org", schema_type="BlogPosting"):
        self.schema = {
            "@context": context,
            "@type": schema_type
        }

    def set_headline(self, headline):
        self.schema["headline"] = headline

    def set_description(self, description):
        self.schema["description"] = description

    def set_author(self, name):
        self.schema["author"] = {
            "@type": "Person",
            "name": name
        }

    def set_date_published(self, date):
        self.schema["datePublished"] = date

    def set_image(self, image_url):
        self.schema["image"] = image_url

    def set_publisher(self, name, logo_url):
        self.schema["publisher"] = {
            "@type": "Organization",
            "name": name,
            "logo": {
                "@type": "ImageObject",
                "url": logo_url
            }
        }

    def set_main_entity_of_page(self, page_url):
        self.schema["mainEntityOfPage"] = {
            "@type": "WebPage",
            "@id": page_url
        }

    def get_schema(self):
        return json.dumps(self.schema, indent=4)

# Usage example
if __name__ == "__main__":
    generator = SchemaMarkupGenerator()
    generator.set_headline("Example Blog Post")
    generator.set_description("This is an example of a blog post with schema markup.")
    generator.set_author("John Doe")
    generator.set_date_published("2024-07-04")
    generator.set_image("https://example.com/images/blog-post.jpg")
    generator.set_publisher("Example Inc.", "https://example.com/images/logo.png")
    generator.set_main_entity_of_page("https://example.com/blog/example-blog-post")

    schema_json = generator.get_schema()
    print(schema_json)
