from django.contrib import admin
from django.utils.html import format_html
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'thumbnail')
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 10

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />'.format(obj.image.url))
        return "-"
    thumbnail.short_description = 'Image'

    def formfield_for_db_field(self, db_field, request, **kwargs):
        formfield = super().formfield_for_db_field(db_field, request, **kwargs)
        if db_field.name == 'image' and formfield:
            formfield.widget.attrs.update({'style': 'display: block; margin: 10px 0;' })
            if request and request.instance and request.pk:
                image_tag = format_html('<img src="{}" class="admin-image-preview" />'.format(request.instance.image.url))
                formfield.widget.attrs.update({'after': image_tag})
        return formfield

    fieldsets = [
        (None, {'fields': ['title', 'author', 'content', 'image_preview', 'image', 'created_at', 'updated_at']}),
    ]

    readonly_fields = ('image_preview', 'created_at', 'updated_at')

    def image_preview(self, obj):
        return self.thumbnail(obj)
    image_preview.short_description = 'Image Preview'

admin.site.register(Post, PostAdmin)
