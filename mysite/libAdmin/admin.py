from django.contrib import admin
from libAdmin.models import Publisher, Author, Book 
# Register your models here.


class BookInLine(admin.TabularInline):
	model = Book
	


class PublisherAdmin(admin.ModelAdmin):
	list_display = ['id','name', 'city']
	list_filter = ['is_active', 'city']
	inlines = [BookInLine]


class AuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name']
	search_fields = ['first_name', 'last_name', 'biography']



class BookAdmin(admin.ModelAdmin):
	actions = ['mark_as_published', 'mark_as_draft', 'mark_as_review']
	
	def mark_as_published(self, request, queryset):
		queryset.update(status='p')
	
	def mark_as_draft(self, request, queryset):
		queryset.update(status='d')
	
	def mark_as_review(self, request, queryset):
		queryset.update(status='r')

	mark_as_published.short_description ='Перевести в статус Опубликовано'
	mark_as_draft.short_description ='Перевести в статус Черновик'
	mark_as_review.short_description ='Перевести в статус Ревью'





admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
