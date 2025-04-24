from django.shortcuts import render, redirect
from .models import CheckIn
from .form import CheckInForm
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.utils import timezone

# Functions that handles daily mood check-in logic and chart rendering
@login_required
def daily_checkin(request):

    # Get Current dates
    today = timezone.now().date()
    week_ago = today - timedelta(days=6)

    #Retrieve or create today's check-in for the user
    checkin, created = CheckIn.objects.get_or_create(user=request.user, date=today) #Check-In Retrieval or Initialization

    #Handle form submission
    if request.method == 'POST':
        form = CheckInForm(request.POST, instance=checkin)
        if form.is_valid():
            form.save()
            return redirect('checkin-home')
    else:
        form = CheckInForm(instance=checkin)

    # Get user's last seven daily checkins
    weekly_checkins = CheckIn.objects.filter(
        user=request.user,
        date__range=(week_ago, today)
    ).order_by('-date')  # Order by most recent first

    # Calculate weekly average
    weekly_avg = weekly_checkins.aggregate(Avg('score'))['score__avg'] # Result is a dictionary {'score__avg': calculated_average} extract value using key 'score_avg'

    # Prepare recent check-ins data for display
    recent_entries = [
        {
            'date': entry.date,
            'score': entry.score
        }
        for entry in weekly_checkins
    ]

    # Get selected date range from URL query parameters (?range=week/month/year/all)
    range_param = request.GET.get('range')
    today = timezone.now().date()

    # Determine date range for chart
    if range_param == "week":
        start_date = today - timedelta(days=6)
        checkins = CheckIn.objects.filter(user=request.user, date__gte=start_date).order_by("date")
    elif range_param == "month":
        start_date = today - timedelta(days=29)
        checkins = CheckIn.objects.filter(user=request.user, date__gte=start_date).order_by("date")
    elif range_param == "year":
        start_date = today - timedelta(days=364)
        checkins = CheckIn.objects.filter(user=request.user, date__gte=start_date).order_by("date")
    else: # default to all
        checkins = CheckIn.objects.filter(user=request.user).order_by("date")

    chart_date = [{"date": str(checkin.date), "score": checkin.score} for checkin in checkins]

    # Context data for template
    context = {
        'form': form,
        'today_score': checkin.score,
        'weekly_avg': weekly_avg,
        'recent_entries': recent_entries,
        'entries_count': len(recent_entries),
        'chart_data': chart_date,
        'range': range_param,
    }

    return render(request, 'checkins/checkin.html', context)