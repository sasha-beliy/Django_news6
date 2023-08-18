import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import News

class NewsFilter(FilterSet):
   class Meta:
       model = News
       fields = {
           'name': ['exact'],
           'description': ['exact']
       }

       date = django_filters.DateFilter(
           field_name="publish",
           lookup_expr="gt",
           label="Date",
           widget=DateInput(
               attrs={"type": "date"},
           ),
       )