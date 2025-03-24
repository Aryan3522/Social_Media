from django.shortcuts import render, redirect, get_object_or_404
from .models import Signup, Admin_Signup
from .forms import StudentForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.utils import timezone

def home(request):
    user_first_name = request.session.get('user_first_name', None)  # Get the user's first name
    return render(request, 'index.html', {'user_first_name': user_first_name})

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Check if the email already exists
            if Signup.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.error(request, "Email already exists. Please use a different email.")
                return render(request, 'Signup.html', {'signupForm': form})

            # Save the password as plain text (not recommended)
            form.cleaned_data['password'] = form.cleaned_data.get('password')
            user = form.save()

            print(f"User created: {user.email}, Password: {user.password}")  # Debugging message
            name = form.cleaned_data.get('firstName')
            messages.success(request, f'hi {name}, your account was created successfully')
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = StudentForm()
    return render(request, 'Signup.html', {'signupForm': form})

def login(request):
    user = None  # Initialize user variable

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Email: {email}, Password: {password}")  # Debugging message

        # Check for superuser credentials
        if email == "admin@example.com" and password == "adminpass":
            user = Admin_Signup.objects.filter(email=email).first()  # Get the superuser instance
            if user:
                auth_login(request, user)  # Use Django's login method
                request.session['is_superuser'] = True  # Set to True for superuser
                request.session['user_id'] = user.id  # Set user ID in session
                request.session['user_first_name'] = user.firstName  # Set user's first name in session
                messages.success(request, f'Hi {user.firstName}, welcome back!')
                user.last_login = timezone.now()  # Update last_login field
                user.save()  # Save the user instance
                print(f"Session data after login: {request.session.items()}")  # Debugging statement for session data
                return redirect("home")  # Redirect to home after successful login

        user = Signup.objects.filter(email=email).first()  # Get the user instance
        if user and user.password == password:  # Check password directly (not recommended for production)
            request.session['is_superuser'] = user.is_superuser
            auth_login(request, user)  # Use Django's login method
            request.session['user_id'] = user.id  # Set user ID in session
            request.session['user_first_name'] = user.firstName  # Set user's first name in session
            messages.success(request, f'Hi {user.firstName}, welcome back!')
            user.last_login = timezone.now()  # Update last_login field
            user.save()  # Save the user instance
            print(f"Session data after login: {request.session.items()}")  # Debugging statement for session data
            return redirect("home")  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    remember_me = request.POST.get('remember_me')  # Get the value of the Remember Me checkbox
    print(f"Remember Me: {remember_me}")  # Debugging statement to log the checkbox value

    if remember_me == 'on':  # Check if the Remember Me checkbox is checked
        request.session.set_expiry(60 * 60 * 24 * 30)  # Set session to expire in 30 days
        print(f"Session expiry age: {request.session.get_expiry_age()}")  # Debugging statement to log session expiry age
    else:
        request.session.set_expiry(0)  # Session expires when the browser is closed

    return render(request, "Login.html")  # Render the login page


def admin_data(request):
    # Check if the user is a superuser
    if request.session.get('is_superuser'):
        # Fetch any necessary admin data here
        admin_info = "This is the admin data."  # Placeholder for actual admin data
        return render(request, "admin_data.html", {'admin_info': admin_info})
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

def admin_edit(request):
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
    return render(request, 'admin_edit.html', {'user_details': user, 'form': form})  

def update(request, id):
    dataget = Signup.objects.get(id=id)
    fm = EditForm(instance=dataget)
    if request.method == 'POST':
        fm = EditForm(request.POST, instance=dataget)
        if fm.is_valid():
            fm.save()
            return redirect('profile')  # Redirect to the profile page after saving

    return render(request, 'user_edit_profile.html', {'editForm': fm})

def edit(request, id):
    dataget = Signup.objects.get(id=id)
    fm = EditForm(instance=dataget)
    if request.method == 'POST':
        fm = EditForm(request.POST, instance=dataget)
        if fm.is_valid():
            fm.save()
            return redirect('profile')  # Redirect to the profile page after saving

    return render(request, 'admin_edit.html', {'editForm': fm})

def read(request):
    data = Signup.objects.all()
    return render(request, 'alldata.html', {'records': data})

def delete(request, id):
    dataget = Signup.objects.get(id=id)
    dataget.delete()
    return redirect('read')

def custom_404_view(request, exception):
    return render(request, '404_error.html', status=404)

def logout(request):
    request.session.flush()  # Clear the session data
    return render(request, "logout.html")
