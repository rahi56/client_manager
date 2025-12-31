from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'company', 'other_company', 'main_applicant', 'status',
            'initial_payment', 'investment', 'local_agent', 'gcbl_no',
            'cbi_submission_date', 'approval_date', 'fm', 'status_notes'
        ]
        widgets = {
            'status': forms.TextInput(attrs={'placeholder': 'Enter client status manually'}),
            'other_company': forms.TextInput(attrs={'placeholder': 'Enter company name if Others selected'}),
            'cbi_submission_date': forms.DateInput(attrs={'type': 'date'}),
            'approval_date': forms.DateInput(attrs={'type': 'date'}),
            'local_agent': forms.TextInput(attrs={'placeholder': 'Enter local agent'}),
            'gcbl_no': forms.TextInput(attrs={'placeholder': 'Enter GCBL number'}),
            'fm': forms.TextInput(attrs={'placeholder': 'Enter FM'}),
            'status_notes': forms.Textarea(attrs={'placeholder': 'Any notes about status', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all optional fields not required
        optional_fields = [
            'other_company', 'status', 'initial_payment', 'investment',
            'local_agent', 'gcbl_no', 'cbi_submission_date', 'approval_date',
            'fm', 'status_notes'
        ]
        for field in optional_fields:
            self.fields[field].required = False

    def clean(self):
        cleaned_data = super().clean()
        company = cleaned_data.get('company')
        other_company = cleaned_data.get('other_company')
        # Require other_company if company is "Others"
        if company == 'Others' and not other_company:
            self.add_error('other_company', 'Please enter the company name.')
