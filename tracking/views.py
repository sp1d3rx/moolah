from django.views.generic import TemplateView, ListView

from models import Transaction, Rate, get_timestamp


class Summary(TemplateView):
    template_name = 'tracking/summary.html'

    def get_context_data(self, *args, **kwargs):
        transactions = Transaction.objects
        context = super(Summary, self).get_context_data(*args, **kwargs)
        context['timestamp'] = get_timestamp()
        context['rate'] = Rate.objects.total()
        context['today'] = transactions.today().total()
        context['week'] = transactions.last_week().total()
        context['month'] = transactions.last_month().total()
        context['year'] = transactions.last_year().total()
        return context


class Today(ListView):
    model = Transaction
    queryset = Transaction.objects.today()