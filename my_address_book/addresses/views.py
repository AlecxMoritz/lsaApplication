from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', { 'contacts': contacts})

def create_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(request('list_contacts'))

    return render(request, 'contacts-form.html', {'form': form})

def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(request.POST or None, instance=contact)

    if form.is_valid():
        form.save()
        return redirect('list_contacts')

    return render(request, 'contacts-form.html', {'form': form, 'contact': contact})

def delete_contact(request, id):
    contact = Contact.objects.get(id=id)

    if request.method == "POST":
        contact.delete()
        return redirect('list_contacts')

    return render(request('cont-delete-confirm.html', {'contact': contact}))