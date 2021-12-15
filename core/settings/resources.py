from import_export import resources

from core.settings.models import Nationality


class NationalityResource(resources.ModelResource):

    class Meta:
        model = Nationality
        skip_unchanged = True
        report_skipped = True
        exclude = ('id', 'history_instance',)
        import_id_fields = ('name', 'is_enable',)