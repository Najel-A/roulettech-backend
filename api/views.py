from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse
from django.http import JsonResponse
import random


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# def index(request):
#     output = "<h1>Obtained response<h1>"
#     return HttpResponse(output)

def about(request):
    data = {
        "name": "Najel Alarcon",
        "description": (
            "During my undergraduate studies, I gained valuable industry experience as a Software Engineer Intern at Alef Aeronautics from October 2020 to April 2021. "
            "In this role, I contributed to the development of flight control software for a flying vehicle startup. My responsibilities included developing a user interface for monitoring "
            "vehicle systems diagnostics and managing the codebase using Git, ensuring version control and documenting changes and updates.\n\n"
            "I have also worked on several projects that demonstrate my technical skills and ability to develop complex software solutions. One notable project is 'Elevate,' a mobile application "
            "developed using React Native, Firebase, and Jest. This app supports the creation, sharing, and engagement of posts, with secure user authentication implemented through Firebase, ensuring "
            "data integrity and CRUD operations. I designed the user interface using JavaScript with React Native.\n\n"
            "Another significant project is the 'Workout Tracker,' developed using the MERN stack (MongoDB, Express.js, React.js, Node.js). I designed a user-friendly interface allowing users to input "
            "exercise details and implemented secure authentication for managing and tracking personal workouts. The project employed RESTful APIs for seamless communication between the frontend and backend components.\n\n"
            "I also developed a 'Slack Clone Mobile Application' using Kotlin, Swift, and React Native. This application included RESTful API integration for real-time messaging, authorization tokens for access, and "
            "collaboration features. I conducted unit tests and debugging to enhance the application's stability and reliability.\n\n"
            "In addition to these projects, I implemented a 'Web Proxy' in C, using socket programming and the HTTPS protocol. The proxy converted HTTP requests to HTTPS, handled concurrent client connections using multithreading, "
            "and featured a database of forbidden hosts that could be altered and reloaded upon a SIGINT signal.\n\n"
            "Another project, 'File Transfer,' involved developing a proxy reliable file transfer application in C, utilizing UDP. I designed and implemented a selective repeat protocol on top of UDP to ensure reliable and error-free file transfer, "
            "with error detection and correction mechanisms.\n\n"
            "Finally, I developed an IoT Obstacle Detection System using C++, Arduino Nano BLE 33, and IRAS sensors. This system integrated GPIO read/write for obstacle detection, triggering an external red LED, and displayed IRAS messages on an LCD. "
            "The Nano 33 BLE was configured as a peripheral device, enabling real-time updates via a BLE Cell Phone App or BLE.\n\n"
            "These experiences and projects have equipped me with a strong foundation in software development, system design, and real-time data processing, which I look forward to further developing in my upcoming master's program."
        )
    }
    return JsonResponse(data)

def generateFunFact(request):
    fun_facts = [
        {
            "name": "Fun Fact #1",
            "description": "I snowboard in the winter, and currently trying to learn to do flips"
        },
        {
            "name": "Fun Fact #2",
            "description": "I hike in the summer typicaly early morning to see the beautiful views"
        },
        {
            "name": "Fun Fact #3",
            "description": "I workout regularly, running a Push Pull Legs (PPL) split"
        },
        {
            "name": "Fun Fact #4",
            "description": "I used to DJ during undergrad of college"
        },
        {
            "name": "Fun Fact #5",
            "description": (
                "I like to play video games, the game I have played the most "
                "is called League of Legends"
            )

        },
    ]
    
    selected_fact = random.choice(fun_facts)
    
    return JsonResponse(selected_fact)
