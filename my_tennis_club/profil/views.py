from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from django.contrib.auth.models import User
from .models import User
from .models import Tournament , User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login



# Create your views here.
@api_view(['POST'])
def register(request):
    data = request.data
    
    if User.objects.filter(username=data['username']).exists():
        return HttpResponse('User already exists')
    username = data.get('username')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    # Now, create the user with the retrieved fields
    if username and password:  # Ensure mandatory fields are present
        user = User(username=username, email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # Hash the password
        user.save()
        return Response({"message": "User created successfully"})
    else:
        return Response({"error": "Username and password are required"})

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def login_view(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "User logged in successfully"})
    else:
        return Response({"error": "Invalid username or password"})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    username = request.data.get('username')
    firstname = request.data.get('first_name')
    lastname = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')

    if not User.objects.filter(username=username).exists():
        user = request.user
        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.set_password(password)  # Hash the password
        user.save()
    else:
        return Response({"error": "Username already exists!"})
    return Response({"message": "User is upadate successfully!"})

@api_view(['POST'])
def profile_user(request):
    user_name = request.data.get('user_name')
    win = 0
    loss = 0
    for user in User.objects.all():
        if user.user_name == user_name:
            for tournament in Tournament.objects.all():
                if tournament.winner == user_name :
                    win += 1
                    continue
                else:
                    loss += 1
    return Response({"user_name": user_name, "win": win, "loss": loss, "total_played_tourn": win+loss})

# user = User.objects.all().first()l
# win = 0
# loss = 0
# for user in User.objects.all():
#     if Tournament.objects.filter(winner=user.user_name).exists():
#         print(user.user_name)
#         win += 1
#     else:

#         loss += 1
# print(win)
# print(loss)