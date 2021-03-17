from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactAddForm



def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts_list.html', {'contacts': contacts})

def create_contact(request):
    form = ContactAddForm()
    if request.method == 'POST':
        form = ContactAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            contact = Contact(name=cd['name'],
                        tel_number=cd['tel_number'],
                        email=cd['email'])
            contact.save()
        return redirect('/contacts')

    return render(request, 'contacts/create_contact.html', {'create_form': form})
