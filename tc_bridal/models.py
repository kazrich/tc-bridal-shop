from django.db import models


class Subscription(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    remember_me = models.BooleanField(default=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    address = models.TextField()
    message = models.TextField(blank=True, null=True)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment - {self.full_name} on {self.date}"


class Inquiry(models.Model):
    INQUIRY_CHOICES = [
        ('Bridal Gown', 'Bridal Gown'),
        ('Maid Dresses', 'Maid Dresses'),
        ('Kids Gowns', 'Kids Gowns'),
        ('Evening Dresses Gowns', 'Evening Dresses Gowns'),
        ('Makeup Booking', 'Makeup Booking'),
        ('Accessories', 'Accessories'),
        ('Bridal Consultation', 'Bridal Consultation'),
        ('Offers', 'Offers'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    inquiry_type = models.CharField(max_length=50, choices=INQUIRY_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.inquiry_type}"