from django.shortcuts import render

def portofolio(request):
    return render(request, 'index.html')


from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse

def sendEmail(request):
    if request.method == 'POST':
        name = request.POST.get('contactName')
        email = request.POST.get('contactEmail')
        subject = request.POST.get('contactSubject', 'Contact Form Submission')
        message = request.POST.get('contactMessage')

        # Validate message
        if len(message) < 15:
            return JsonResponse({'error': 'Please enter a message with at least 15 characters.'}, status=400)

        # Send email
        try:
            send_mail(subject, message, email, ['aadhitnc@google.com'])
            return JsonResponse({'success': 'Your message has been sent successfully.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

