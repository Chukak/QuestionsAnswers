from django.shortcuts import render
from django.views.generic import TemplateView
from ..questions.models import Question

# Create your views here.


# Homepage view
class HomepageView(TemplateView):
    template_name = 'homepage/homepage.html'

    # get questions list limit 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = list(Question.objects.all().order_by('-date_created')[:10])
        return context
