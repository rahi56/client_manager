from django.db import models

class Client(models.Model):
    COMPANY_CHOICES = [
        ('Roc Citizenship DMCC', 'Roc Citizenship DMCC'),
        ('Greeth Brookes', 'Greeth Brookes'),
        ('Passport Gate', 'Passport Gate'),
        ('Citizenship Invest DMCC', 'Citizenship Invest DMCC'),
        ('KG', 'KG'),
        ('TFG', 'TFG'),
        ('Mirka', 'Mirka'),
        ('Sparco', 'Sparco'),
        ('Winvested', 'Winvested'),
        ('Others', 'Others'),
    ]

    company = models.CharField(max_length=255, choices=COMPANY_CHOICES)
    other_company = models.CharField(max_length=255, null=True, blank=True)

    main_applicant = models.CharField(max_length=255)

    # Make status a free text field (manual input)
    status = models.CharField(max_length=500, null=True, blank=True, default='Current')

    # Optional YES/NO fields
   # YES_NO_CHOICES = [('YES', 'YES'), ('NO', 'NO')]
    initial_payment = models.CharField(max_length=20, null=True, blank=True)
    investment = models.CharField(max_length=20, null=True, blank=True)

    local_agent = models.CharField(max_length=255, null=True, blank=True)
    gcbl_no = models.CharField(max_length=100, null=True, blank=True)

    cbi_submission_date = models.DateField(null=True, blank=True)
    approval_date = models.DateField(null=True, blank=True)

    fm = models.CharField(max_length=255, null=True, blank=True)
    status_notes = models.TextField(null=True, blank=True)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.main_applicant} - {self.company}"

# models.py
class ApprovedClient(Client):
    class Meta:
        proxy = True  # Optional if same fields, else use separate table

class IssuedClient(Client):
    class Meta:
        proxy = True
class DeniedClient(Client):
    class Meta:
        proxy = True
