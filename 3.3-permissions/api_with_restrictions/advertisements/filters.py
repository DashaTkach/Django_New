from django_filters import rest_framework as filters, FilterSet, DateTimeFromToRangeFilter, CharFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    class F_date(FilterSet):
        created_at = DateTimeFromToRangeFilter()
        updated_at = DateTimeFromToRangeFilter()
        status = CharFilter()

        class Meta:
            model = Advertisement
            fields = ['created_at', 'updated_at', 'status', ]
