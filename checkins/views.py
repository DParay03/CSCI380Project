from django.shortcuts import render, redirect
from .models import CheckIn
from .form import CheckInForm
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.utils import timezone


@login_required
def daily_checkin(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=6)
    checkin, created = CheckIn.objects.get_or_create(user=request.user, date=today) #Check-In Retrieval or Initialization
    # Method return a tuple:
    # checkin: instance of the check-in record
    # created: a Boolean indicating whether the record was created or fetched from the DB

    if request.method == 'POST':
        form = CheckInForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect('checkin-home')
    else:
        form = CheckInForm(instance=checkin)

    # Get weekly checkins
    weekly_checkins = CheckIn.objects.filter(
        user=request.user,
        date__range=(week_ago, today)
    ).order_by('-date')  # Order by most recent first

    # Calculate weekly average
    weekly_avg = weekly_checkins.aggregate(Avg('score'))['score__avg'] # Result is a dictionary {'score__avg': calculated_average} extract value using key 'score_avg'

    # Get the last few days' entries
    recent_entries = [
        {
            'date': entry.date,
            'score': entry.score
        }
        for entry in weekly_checkins
    ]


    range_param = request.GET.get('range')
    today = timezone.now().date()

    if range_param == "week":
        start_date = today - timedelta(days=7)
        checkins = CheckIn.objects.filter(user=request.user, date__gte=start_date).order_by("date")
    elif range_param == "month":
        start_date = today - timedelta(days=30)
        checkins = CheckIn.objects.filter(user=request.user, date__gte=start_date).order_by("date")
    elif range_param == "year":
        start_date = today - timedelta(days=365)
        checkins = CheckIn.objects.filter(user=request.user, date__gte=start_date).order_by("date")
    else: # default to all
        checkins = CheckIn.objects.filter(user=request.user).order_by("date")

    date = [{"date": str(checkin.date), "score": checkin.score} for checkin in checkins]

    context = {
        'form': form,
        'today_score': checkin.score,
        'weekly_avg': weekly_avg,
        'recent_entries': recent_entries,
        'entries_count': len(recent_entries),
        'chart_data': date,
        'range': range_param,
    }

    return render(request, 'checkins/checkin.html', context)