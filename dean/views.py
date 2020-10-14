from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
#from .models import Appointment
#from .forms import AppointmentForm
from django.contrib import messages
#from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.views.generic import TemplateView

@login_required()
def dean_home(request):
    query = get_current_users()
    queryset = {
        'query':query
    }
    return render(request, 'dean_home.html', queryset)

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

class DeansView(TemplateView):
    template_name = 'dean_home.html'

    def get_context_data(self, **kwargs):
        context = super(DeansView, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context

