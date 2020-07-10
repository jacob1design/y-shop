from django import forms

class OrderForm(forms.Form):
    delivery_address = forms.CharField(label='Adresse de livraison', max_length=255,widget=forms.Textarea)
    phone_number = forms.IntegerField(label='Numero de telephone')