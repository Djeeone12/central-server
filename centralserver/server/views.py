from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.http import JsonResponse
import requests
import json
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def nodesqlStudents(request):
    return render(request, '1.html')



def nodesqlStudentsGET(request):
    ID = request.GET['GetID']
    url = "https://crud-nodejs-1.herokuapp.com/students/"
    pokeURL = url+ID
    r = requests.get(pokeURL).json()
    return JsonResponse(r, safe=False)


def nodesqlStudentsPOST(request):
    MODEL = request.POST.get('PostMODEL')
    JMODEL = json.loads(MODEL)
    url = "https://crud-nodejs-1.herokuapp.com/students/add"
    pokeURL = url
    r = requests.post(url=pokeURL,json=JMODEL)
    return HttpResponse(r)


def nodesqlStudentsPUT(request):
    ID = request.GET['PutID']
    MODEL = request.GET['PutMODEL']
    JMODEL = json.loads(MODEL)
    url = "https://crud-nodejs-1.herokuapp.com/students/modify/"
    pokeURL = url+ID
    r = requests.put(url=pokeURL, json=JMODEL)
    return HttpResponse(r)


def nodesqlStudentsDEL(request):
    ID = request.GET['DeleteID']
    url = "https://crud-nodejs-1.herokuapp.com/students/del/"
    pokeURL = url+ID
    r = requests.delete(pokeURL)
    return HttpResponse(r)

def nodesqlTeachers(request):
    return render(request, '2.html')



def nodesqlTeachersGET(request):
    ID = request.GET['GetID']
    url = "https://crud-nodejs-1.herokuapp.com/teachers/"
    pokeURL = url+ID
    r = requests.get(pokeURL).json()
    return JsonResponse(r, safe=False)


def nodesqlTeachersPOST(request):
    MODEL = request.POST.get('PostMODEL')
    JMODEL = json.loads(MODEL)
    url = "https://crud-nodejs-1.herokuapp.com/teachers/add"
    pokeURL = url
    r = requests.post(url=pokeURL,json=JMODEL)
    return HttpResponse(r)


def nodesqlTeachersPUT(request):
    ID = request.GET['PutID']
    MODEL = request.GET['PutMODEL']
    JMODEL = json.loads(MODEL)
    url = "https://crud-nodejs-1.herokuapp.com/teachers/modify/"
    pokeURL = url+ID
    r = requests.put(url=pokeURL, json=JMODEL)
    return HttpResponse(r)


def nodesqlTeachersDEL(request):
    ID = request.GET['DeleteID']
    url = "https://crud-nodejs-1.herokuapp.com/teachers/del/"
    pokeURL = url+ID
    r = requests.delete(pokeURL)
    return HttpResponse(r)


def flaskmysqlSemesters(request):
    return render(request, '3.html')



def flaskmysqlSemestersGET(request):
    ID = request.GET['GetID']
    url = "http://app-flask-mysql.herokuapp.com/semester/"
    pokeURL = url+ID
    r = requests.get(pokeURL).json()
    return JsonResponse(r, safe=False)


def flaskmysqlSemestersPOST(request):
    MODEL = request.POST.get('PostMODEL')
    MODEL = MODEL
    print(MODEL)
    JMODEL = json.loads(MODEL)
    print(JMODEL)
    url = "http://app-flask-mysql.herokuapp.com/semester"
    pokeURL = url
    r = requests.post(url=pokeURL,json=JMODEL)
    print(r)
    return HttpResponse(r)


def flaskmysqlSemestersPUT(request):
    ID = request.GET['PutID']
    print(ID)
    MODEL = request.GET['PutMODEL']
    JMODEL = json.loads(MODEL)
    print(MODEL)
    print(JMODEL)
    url = "http://app-flask-mysql.herokuapp.com/semester/"
    pokeURL = url+ID
    r = requests.put(url=pokeURL, json=JMODEL)
    print(r)
    return HttpResponse(r)


def flaskmysqlSemestersDEL(request):
    ID = request.GET['DeleteID']
    url = "http://app-flask-mysql.herokuapp.com/semester/"
    pokeURL = url+ID
    r = requests.delete(pokeURL)
    return HttpResponse(r)


def flaskmysqlCareer(request):
    return render(request, '4.html')



def flaskmysqlCareerGET(request):
    ID = request.GET['GetID']
    url = "http://app-flask-mysql.herokuapp.com/career/"
    pokeURL = url+ID
    r = requests.get(pokeURL).json()
    return JsonResponse(r, safe=False)


def flaskmysqlCareerPOST(request):
    MODEL = request.POST.get('PostMODEL')
    MODEL = MODEL
    print(MODEL)
    JMODEL = json.loads(MODEL)
    print(JMODEL)
    url = "http://app-flask-mysql.herokuapp.com/career"
    pokeURL = url
    r = requests.post(url=pokeURL, json=JMODEL)
    print(r)
    return HttpResponse(r)


def flaskmysqlCareerPUT(request):
    ID = request.GET['PutID']
    print(ID)
    MODEL = request.GET['PutMODEL']
    JMODEL = json.loads(MODEL)
    print(MODEL)
    print(JMODEL)
    url = "http://app-flask-mysql.herokuapp.com/career/"
    pokeURL = url + ID
    r = requests.put(url=pokeURL, json=JMODEL)
    print(r)
    return HttpResponse(r)


def flaskmysqlCareerDEL(request):
    ID = request.GET['DeleteID']
    url = "http://app-flask-mysql.herokuapp.com/career/"
    pokeURL = url+ID
    r = requests.delete(pokeURL)
    return HttpResponse(r)

def nodemongoGrades(request):
    return render(request, '5.html')



def nodemongoGradesGET(request):
    ID = request.GET['GetID']
    url = "https://api-nodejs-mongod.herokuapp.com/grades/"
    pokeURL = url+ID
    r = requests.get(pokeURL)
    return HttpResponse(r)


def nodemongoGradesPOST(request):
    MODEL = request.POST.get('PostMODEL')
    JMODEL = json.loads(MODEL)
    url = "https://api-nodejs-mongod.herokuapp.com/grades/add"
    pokeURL = url
    r = requests.post(url=pokeURL,data=JMODEL)
    return HttpResponse(r)


def nodemongoGradesPUT(request):
    ID = request.GET['PutID']
    MODEL = request.GET['PutMODEL']
    JMODEL = json.loads(MODEL)
    url = "https://api-nodejs-mongod.herokuapp.com/grades/edit/"
    pokeURL = url+ID
    r = requests.put(url=pokeURL, data=JMODEL)
    return HttpResponse(r)


def nodemongoGradesDEL(request):
    ID = request.GET['DeleteID']
    url = "https://api-nodejs-mongod.herokuapp.com/grades/delete/"
    pokeURL = url+ID
    r = requests.delete(pokeURL)
    return HttpResponse(r)

def nodemongoSubjects(request):
    return render(request, '6.html')



def nodemongoSubjectsGET(request):
    ID = request.GET['GetID']
    url = "https://api-nodejs-mongod.herokuapp.com/subjects/"
    pokeURL = url+ID
    r = requests.get(pokeURL).json()
    return JsonResponse(r, safe=False)


def nodemongoSubjectsPOST(request):
    MODEL = request.POST.get('PostMODEL')
    JMODEL = json.loads(MODEL)
    url = "https://api-nodejs-mongod.herokuapp.com/subjects/add"
    pokeURL = url
    r = requests.post(url=pokeURL, data=JMODEL)
    return HttpResponse(r)


def nodemongoSubjectsPUT(request):
    ID = request.GET['PutID']
    MODEL = request.GET['PutMODEL']
    JMODEL = json.loads(MODEL)
    url = "https://api-nodejs-mongod.herokuapp.com/subjects/edit/"
    pokeURL = url + ID
    r = requests.put(url=pokeURL, data=JMODEL)
    return HttpResponse(r)


def nodemongoSubjectsDEL(request):
    ID = request.GET['DeleteID']
    url = "https://api-nodejs-mongod.herokuapp.com/subjects/delete/"
    pokeURL = url+ID
    r = requests.delete(pokeURL)
    return HttpResponse(r)


# Create your views here.
