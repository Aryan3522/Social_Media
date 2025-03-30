from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification  # Assuming there's a Notification model
from .models import Signup, Admin_Signup
from .forms import StudentForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.utils import timezone
from .utils import notify_superusers  # Import the notification function

def handle_approval(request, user_id, approve):
    if not request.session.get('is_superuser'):
        messages.error(request, "You do not have permission to approve users.")
        return redirect('admin_data')  # Redirect to admin data if not a superuser

    user = get_object_or_404(Signup, id=user_id)  # Retrieve the user by ID
    user.is_superuser = approve.lower() == 'true'  # Convert string to boolean

    if user.is_superuser:
        notify_superusers(user.email)  # Notify existing superusers

    user.save()  # Save the updated user instance
    messages.success(request, f"User {user.email} has been {'approved' if user.is_superuser else 'disapproved'}.")
    return redirect('admin_data')  # Redirect to admin data page

def approve_superuser(request):
    if not request.session.get('is_superuser'):
        messages.error(request, "You do not have permission to view this page.")
        return redirect('admin_data')  # Redirect to admin data if not a superuser

    return render(request, 'approve_superuser.html')  # Render the approval page

def get_admin_notifications(request):
    notifications = Notification.objects.filter(is_approved=False)  # Fetch unapproved notifications
    return notifications

def home(request):
    notifications = get_admin_notifications(request)  # Get notifications for the modal
    user_first_name = request.session.get('user_first_name', None)  # Get the user's first name
    return render(request, 'index.html', {'user_first_name': user_first_name})

def create(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if Signup.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.error(request, "Email already exists. Please use a different email.")
                return render(request, 'Signup.html', {'signupForm': form})
            user = form.save(commit=False)  # Save the user instance without committing to the database
            user.is_superuser = request.POST.get('is_superuser') == 'true'  # Set superuser status based on checkbox
            user.save()  # Now save the user instance
            if user.is_superuser:
                notify_superusers(user.email)  # Notify existing superusers

            messages.success(request, f'Hi {form.cleaned_data.get("firstName")}, your account was created successfully')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = StudentForm()
    return render(request, 'Signup.html', {'signupForm': form})

def login(request):
    user = None  # Initialize user variable
    if request.method == "POST":
        identifier = request.POST.get('username_or_email')
        password = request.POST.get('password')
        if identifier:
            user = Admin_Signup.objects.filter(email=identifier).first()  # Get the superuser instance
            if not user:
                user = Admin_Signup.objects.filter(username=identifier).first()  # Check for username
        else:
            user = None

        if user and user.password == password:  # Check password directly (not recommended for production)
            auth_login(request, user)  # Use Django's login method
            request.session['is_superuser'] = True  # Set to True for superuser
            request.session['user_id'] = user.id  # Set user ID in session
            request.session['user_first_name'] = user.firstName  # Set user's first name in session
            messages.success(request, f'Hi {user.firstName}, welcome back!')
            user.last_login = timezone.now()  # Update last_login field
            user.save()  # Save the user instance
            return redirect("home")  # Redirect to home after successful login
        if identifier:
            user = Signup.objects.filter(email=identifier).first()  # Get the user instance, case-sensitive

            if not user:
                user = Signup.objects.filter(username=identifier).first()  # Check for username
        else:
            user = None

        if not user:
            user = Signup.objects.filter(username=identifier).first()  # Check for username

        if user and user.password == password:  # Check password directly (not recommended for production)
            request.session['is_superuser'] = user.is_superuser
            auth_login(request, user)  # Use Django's login method
            request.session['user_id'] = user.id  # Set user ID in session
            request.session['user_first_name'] = user.firstName  # Set user's first name in session
            messages.success(request, f'Hi {user.firstName}, welcome back!')
            user.last_login = timezone.now()  # Update last_login field
            user.save()  # Save the user instance
            return redirect("home")  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    remember_me = request.POST.get('remember_me')  # Get the value of the Remember Me checkbox
    if remember_me == 'on':  # Check if the Remember Me checkbox is checked
        request.session.set_expiry(60 * 60 * 24 * 30)  # Set session to expire in 30 days
    else:
        request.session.set_expiry(0)  # Session expires when the browser is closed

    return render(request, "Login.html")  # Render the login page

def admin_data(request):
    if request.session.get('is_superuser'):
        records = Signup.objects.all()  # Fetch all user records
        return render(request, "alldata.html", {'records': records})  # Render alldata.html with records
    else:
        messages.error(request, "You do not have permission to view this page.")
        return redirect("login")  # Redirect to login if not a superuser

def profile(request):
    user_id = request.session.get('user_id', None)
    user_details = Signup.objects.filter(id=user_id).first() if user_id else None
    user_first_name = request.session.get('user_first_name', None)  # Get the user's first name

    if user_details is None:
        messages.error(request, "You need to be logged in to view your profile.")
        return redirect('login')  # Redirect to login if user is not found

    if request.session.get('is_superuser'):
        return render(request, "admin_profile.html", {'user_details': user_details, 'user_first_name': user_first_name})
    else:
        return render(request, "profile.html", {'user_details': user_details, 'user_first_name': user_first_name})

def edit_profile(request):
    user_id = request.session.get('user_id')
    user = Signup.objects.filter(id=user_id).first() if user_id else None  # Get the Signup instance

    if user is None:
        messages.error(request, "You need to be logged in to edit your profile.")
        return redirect('login')  # Redirect to login if user is not found

    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)  # Use the Signup instance
        if form.is_valid():  # Check if the form is valid
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = EditForm(instance=user)
    return render(request, 'user_edit_profile.html', {'user_details': user, 'form': form})  # Render the edit profile page

def delete(request, id):
    dataget = Signup.objects.get(id=id)
    dataget.delete()
    return redirect('admin_data')

def custom_404_view(request, exception):
    return render(request, '404_error.html', status=404)

def logout(request):
    request.session.flush()  # Clear the session data
    return render(request, "logout.html")
