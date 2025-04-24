import io
import base64
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from users.models import User
from communityPost.models import Post
from checkins.models import CheckIn
from django.db.models import Avg

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result.getvalue()
    return None

def generate_single_chart(title, label, value):
    buffer = io.BytesIO()
    plt.figure(figsize=(4, 3))
    plt.bar([label], [value], color='mediumpurple')
    plt.title(title)
    plt.ylim(0, max(10, value + 5))
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode('utf-8')


def report_views(request):
    # Stats
    user_count = User.objects.count()
    post_count = Post.objects.count()
    mood_checkins = CheckIn.objects.count()

    # Average mood via reverse relationship
    avg_mood = CheckIn.objects.aggregate(avg_score=Avg('user__checkin__score'))['avg_score'] or 0
    avg_mood = round(avg_mood, 2)

    # Generate 4 individual charts
    chart_user = generate_single_chart("Total Users", "Users", user_count)
    chart_posts = generate_single_chart("Total Posts", "Posts", post_count)
    chart_checkins = generate_single_chart("Mood Check-Ins", "Check-Ins", mood_checkins)
    chart_mood = generate_single_chart("Average Mood Score", "Mood", avg_mood)

    context = {
        'user_count': user_count,
        'post_count': post_count,
        'mood_checkins': mood_checkins,
        'average_mood': avg_mood,
        'chart_user': f'data:image/png;base64,{chart_user}',
        'chart_posts': f'data:image/png;base64,{chart_posts}',
        'chart_checkins': f'data:image/png;base64,{chart_checkins}',
        'chart_mood': f'data:image/png;base64,{chart_mood}',
    }

    pdf = render_to_pdf('report/statistics.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report.pdf"'
        return response
    return HttpResponse("Failed to generate PDF")