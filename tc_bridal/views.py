from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        full_name = request.POST.get("full-name")
        email = request.POST.get("email")
        remember_Me = request.POST.get("remember-Me")  # Optional

        # Send an Email
        send_mail(
            subject=f"{full_name} just subscribed",
            message=f"Their email address is: {email}",
            from_email="noreply@tcbridalshop.com",  # use a valid email
            recipient_list=["tcbridals@gmail.com"],
            fail_silently=False
        )

        return render(request, 'index.html', {
            'full_name': full_name,
        })

    return render(request, 'index.html')



def bags(request):
    return render(request, 'bags.html')

def necklaces(request):
    return render(request, 'necklaces.html')

def shoes(request):
    return render(request, 'shoes.html')

def appoint(request):
    if request.method == "POST":
        full_name = request.POST.get("f-name")
        email = request.POST.get("e-email")
        phone = request.POST.get("p-phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        address = request.POST.get("address")
        message = request.POST.get("m-message")

        # Compose full message
        full_message = f"""
Hello TC Bridals,

You have received a new appointment booking:

Name: {full_name}
Email: {email}
Phone: {phone}
Date: {date}
Time: {time}
Address: {address}

Message:
{message}

Please respond for any changes.

Regards,
TC Bridal Website
"""

        # Send the email
        send_mail(
            subject=f"New Booking from {full_name}",
            message=full_message,
            from_email=email,
            recipient_list=['tcbridals@gmail.com'],
            fail_silently=False
        )

        # Pass name and email to trigger success message in template
        return render(request, 'appoint.html', {
            'full_name': full_name,
            'email': email
        })

    return render(request, 'appoint.html')


def kids(request):
    return render(request, 'kids.html')

def events(request):
    return render(request, 'event.html')

def inquires(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        inquiry_type = request.POST.get("inquiry_type")  # ✅ corrected name
        message = request.POST.get("message")            # ✅ corrected typo

        # Compose the full message
        full_message = f"""
Hello TC Bridals,

You've received a new customer inquiry.

Name: {name}
Email: {email}
Phone: {phone}
Inquiry Type: {inquiry_type}

Message:
{message}

Please respond accordingly.

Regards,
TC Bridal Website
"""

        # Send the email
        send_mail(
            subject=f"Inquiry from {name}: {inquiry_type}",
            message=full_message,
            from_email=email,
            recipient_list=['tcbridals@gmail.com'],
            fail_silently=False
        )

        # Pass name and email to template to show confirmation
        return render(request, 'inquires.html', {
            'name': name,
            'email': email
        })

    else:
        return render(request, 'inquires.html')

def makeup(request):
    return render(request, 'makeup.html')

def veils(request):
    return render(request, 'veils.html')

def earring(request):
    return render(request, 'earrings.html')

def ceo(request):
    return render(request, 'ceo.html')

def bracelets(request):
    return render(request, 'bracelets.html')

def evening(request):
    return render(request, 'evening.html')

def maid(request):
    return render(request, 'maid.html')
