from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, Tag, Project, ProjectImage, Donation, Rating, Comment, ProjectReport, CommentReport


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):  # بدل ModelAdmin استخدم ImportExportModelAdmin
    list_display = ('title', 'creator', 'category', 'total_target', 'is_canceled', 'featured', 'created_at')
    list_filter = ('category', 'featured', 'is_canceled')
    search_fields = ('title', 'details')
    inlines = [ProjectImageInline]


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    pass


@admin.register(Donation)
class DonationAdmin(ImportExportModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(ImportExportModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    pass


@admin.register(ProjectReport)
class ProjectReportAdmin(ImportExportModelAdmin):
    pass


@admin.register(CommentReport)
class CommentReportAdmin(ImportExportModelAdmin):
    pass