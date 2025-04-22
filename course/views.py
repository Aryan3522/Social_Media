from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image, Notification, Signup, Admin_Signup
from .forms import StudentForm, EditForm,ImgForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.utils import timezone
from .utils import notify_superusers


def handle_approval(request, user_id, approve):
    if not request.session.get('is_superuser'):
        messages.error(request, "You do not have permission to approve users.")
        return redirect('admin_data')

    user = get_object_or_404(Signup, id=user_id)
    user.is_superuser = approve.lower() == 'true'

    if user.is_superuser:
        notify_superusers(user.email)

    user.save()
    messages.success(request, f"User {user.email} has been {'approved' if user.is_superuser else 'disapproved'}.")
    return redirect('admin_data')

def approve_superuser(request):
    if not request.session.get('is_superuser'):
        messages.error(request, "You do not have permission to view this page.")
        return redirect('admin_data')

    return render(request, 'approve_superuser.html')

def get_admin_notifications(request):
    notifications = Notification.objects.filter(is_approved=False)
    return notifications



def home(request):
    notifications = get_admin_notifications(request)
    post = Image.objects.all()
    user_id = request.session.get('user_id')
    context = {"img":post}
    user_details = Signup.objects.filter(id=user_id).first() if user_id else None
    merged_context = context.copy()
    merged_context["user_details"] = user_details
    return render(request, 'index.html', merged_context)

def add_image(request):
    if request.method == 'POST':
        prod = Image()
        prod.image = request.FILES["image"]
        prod.save()
        print(prod)
        print("Image Saved Succefully")
        return redirect('/')
    else:
        print("Image is not Saved Succefully")
    return render(request, 'addImage.html')
        
# def create(request):
#     superuser_identifier = {"username":"Hooda","email":"aryanhooda@gmail.com"}
#     superuser_password = {"password":"1234"}
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             if Signup.objects.filter(email=form.cleaned_data.get('email')).exists():
#                 messages.error(request, "Email already exists. Please use a different email.")
#                 return render(request, 'Signup.html', {'signupForm': form})
#             user = form.save()
#             if user.identifier == superuser_identifier and user.password == superuser_password:
#                 user.is_superuser = request.POST.get('is_superuser') == 'true'
#             else:
#                 user.is_superuser = request.POST.get('is_superuser') == 'false'
#             user.save()
#             return redirect('login')
#     else:
#         form = StudentForm()
#     return render(request, 'Signup.html', {'signupForm': form})

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            if Signup.objects.filter(email=form.cleaned_data.get('email')).exists():
                messages.error(request, "Email already exists. Please use a different email.")
                return render(request, 'Signup.html', {'signupForm': form})
            user = form.save()
            # user = form.save(commit=False)
            user.is_superuser = request.POST.get('is_superuser') == 'true'
            user.save()
            if user.is_superuser:
                notify_superusers(user.email)
            messages.success(request, f'Hi {form.cleaned_data.get("firstName")}, your account was created successfully')
            return redirect('login')
    else:
        form = StudentForm()
    return render(request, 'Signup.html', {'signupForm': form})

def login(request):
    user = None
    if request.method == "POST":
        identifier = request.POST.get('username_or_email')
        password = request.POST.get('password')
        if identifier:
            user = Admin_Signup.objects.filter(email=identifier).first()
            if not user:
                user = Admin_Signup.objects.filter(username=identifier).first()
        else:
            user = None
        if user and user.password == password:
            auth_login(request, user)
            request.session['is_superuser'] = True
            request.session['is_superuser'] = False   
            request.session['user_id'] = user.id
            request.session['user_first_name'] = user.firstName
            messages.success(request, f'Hi {user.firstName}, welcome back!')
            user.last_login = timezone.now()
            user.save()
            return redirect("home")
        if identifier:
            user = Signup.objects.filter(email=identifier).first()
            if not user:
                user = Signup.objects.filter(username=identifier).first()
        else:
            user = None
        if user and user.password == password:
            request.session['is_superuser'] = user.is_superuser
            auth_login(request, user)
            request.session['user_id'] = user.id
            request.session['user_first_name'] = user.firstName
            messages.success(request, f'Hi {user.firstName}, welcome back!')
            user.last_login = timezone.now()
            user.save()
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    return render(request, "Login.html")

# def login(request):
#     superuser_identifier = {"username":"Hooda","email":"aryanhooda@gmail.com"}
#     superuser_password = {"password":"1234"}
#     user = None
#     if request.method == "POST":
#         identifier = request.POST.get('username_or_email')
#         password = request.POST.get('password')
#         if identifier:
#             user = Admin_Signup.objects.filter(email=identifier).first()
#             if not user:
#                 user = Admin_Signup.objects.filter(username=identifier).first()
#         else:
#             user = None
#         if user and user.password == password:
#             auth_login(request, user)
#             if user.identifier == superuser_identifier and user.password == superuser_password:
#                 request.session['is_superuser'] = True
#             else:
#                 request.session['is_superuser'] = False   
#             request.session['user_id'] = user.id
#             request.session['user_first_name'] = user.firstName
#             messages.success(request, f'Hi {user.firstName}, welcome back!')
#             user.last_login = timezone.now()
#             user.save()
#             return redirect("home")
#         if identifier:
#             user = Signup.objects.filter(email=identifier).first()
#             if not user:
#                 user = Signup.objects.filter(username=identifier).first()
#         else:
#             user = None
#         if user and user.password == password:
#             request.session['is_superuser'] = user.is_superuser
#             auth_login(request, user)
#             request.session['user_id'] = user.id
#             request.session['user_first_name'] = user.firstName
#             messages.success(request, f'Hi {user.firstName}, welcome back!')
#             user.last_login = timezone.now()
#             user.save()
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid credentials. Please try again.")
#     return render(request, "Login.html")

def admin_data(request):
    print("Admin_data Page")
    if request.session.get('is_superuser'):
        records = Signup.objects.all()
        return render(request, "alldata.html", {'records': records})
    else:
        messages.error(request, "You do not have permission to view this page.")
        return redirect("login")

def profile(request):
    post = Image.objects.all()
    context = {"img":post}
    user_id = request.session.get('user_id', None)
    user_details = Signup.objects.filter(id=user_id).first() if user_id else None
    merged_context = context.copy()
    merged_context["user_details"] = user_details

    if user_details is None:
        messages.error(request, "You need to be logged in to view your profile.")
        return redirect('login')

    if request.session.get('is_superuser'):
        return render(request, "profile.html", merged_context)
    else:
        return render(request, "profile.html", merged_context)

def edit_profile(request):
    user_id = request.session.get('user_id')
    user = Signup.objects.filter(id=user_id).first() if user_id else None

    if user is None:
        messages.error(request, "You need to be logged in to edit your profile.")
        return redirect('login')

    if request.method == 'POST':
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = EditForm(instance=user)
    return render(request, 'user_edit_profile.html', {'user_details': user, 'form': form})

def delete(request, id):
    dataget = Signup.objects.get(id=id)
    dataget.delete()
    return redirect('admin_data')

@csrf_exempt
def deletePost(request, id):
    dataget = Image.objects.get(id=id)
    dataget.delete()
    return redirect('profile')
    

# @csrf_exempt
# def deletePost(request, id):
#     if request.method == 'POST':
#         try:
#             dataget = Image.objects.get(id=id)
#             dataget.delete()
#             return JsonResponse({'status': 'success'})
#         except Image.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Image not found'}, status=404)
#     return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def custom_404_view(request, exception):
    return render(request, '404_error.html', status=404)

def logout(request):
    request.session.flush()
    return render(request, "logout.html")

def forgot_password(request):
    print("Forgot password function called")
    alert_message = ""
    if request.method == "POST":
        identifier = request.POST.get('username_or_email')
        user = Signup.objects.filter(email=identifier).first() or Signup.objects.filter(username=identifier).first()
        
        if user:
            alert_message = "Password reset instructions have been sent to your email."
        else:
            alert_message = "No user found with that email or username."
    
    return render(request, "forgot_password.html", {'alert_message': alert_message})


# post functions
# @csrf_exempt
# @login_required
# def delete_image(request, image_id):
#     if request.method == 'POST':
#         try:
#             image = Image.objects.get(id=image_id, user=request.user)
#             image.delete()  # This will trigger the soft delete
#             return JsonResponse({'status': 'success'})
#         except Image.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Image not found'}, status=404)
#     return JsonResponse({'status': 'error'}, status=400)

# @csrf_exempt
# @login_required
# def upload_image(request):
#     if request.method == 'POST':
#         image_file = Image(request.POST)
#         if image_file.is_valid():
#             image_file = image_file.save()
#             Image.objects.create(name=request.POST['name'], img=image_file)
#             print("Image successfully uploaded")
#             return HttpResponse('Image successfully uploaded')
#         else:
#             print("Image is not uploaded")
#             return HttpResponse('Image is not uploaded')
#     return JsonResponse({'status': 'error'}, status=400)

# @login_required
# def post_list(request):
#     posts = Post.objects.filter(author=request.user, is_active=True).order_by('-created_at')
#     post_data = [{
#         'id': post.id,
#         'content': post.content,
#         'created_at': post.created_at.strftime('%Y-%m-%d %H:%M')
#     } for post in posts]

#     images = Image.objects.filter(user=request.user, is_active=True).order_by('-created_at')
#     image_data = [{
#         'id': img.id,
#         'image_data': img.image_data,
#         'caption': img.caption,
#         'created_at': img.created_at.strftime('%Y-%m-%d %H:%M')
#     } for img in images]

#     return JsonResponse({'status': 'success', 'posts': post_data, 'images': image_data})

# @csrf_exempt
# @login_required
# def post_update(request, post_id):
#     if request.method == 'PUT':
#         try:
#             post = Post.objects.get(id=post_id, author=request.user)
#             data = json.loads(request.body)
#             post.content = data['content']
#             post.save()
#             return JsonResponse({
#                 'status': 'success',
#                 'post': {
#                     'id': post.id,
#                     'content': post.content
#                 }
#             })
#         except Post.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Post not found'}, status=404)
#         except Exception as e:
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
#     return JsonResponse({'status': 'error'}, status=400)

# @csrf_exempt
# @login_required
# def post_delete(request, post_id):
#     if request.method == 'DELETE':
#         try:
#             post = Post.objects.get(id=post_id, author=request.user)
#             post.is_active = False
#             post.save()
#             return JsonResponse({'status': 'success'})
#         except Post.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Post not found'}, status=404)
#     return JsonResponse({'status': 'error'}, status=400)
