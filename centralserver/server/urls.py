from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('node-sql-students/', views.nodesqlStudents, name='index'),
    path('node-sql-students-get/', views.nodesqlStudentsGET, name='index'),
    path('node-sql-students-post/', views.nodesqlStudentsPOST, name='index'),
    path('node-sql-students-put/', views.nodesqlStudentsPUT, name='index'),
    path('node-sql-students-del/', views.nodesqlStudentsDEL, name='index'),
    path('node-sql-teachers/', views.nodesqlTeachers, name='index'),
    path('node-sql-teachers-get/', views.nodesqlTeachersGET, name='index'),
    path('node-sql-teachers-post/', views.nodesqlTeachersPOST, name='index'),
    path('node-sql-teachers-put/', views.nodesqlTeachersPUT, name='index'),
    path('node-sql-teachers-del/', views.nodesqlTeachersDEL, name='index'),
    path('flask-mysql-semester/', views.flaskmysqlSemesters, name='index'),
    path('flask-mysql-semester-get/', views.flaskmysqlSemestersGET, name='index'),
    path('flask-mysql-semester-post/', views.flaskmysqlSemestersPOST, name='index'),
    path('flask-mysql-semester-put/', views.flaskmysqlSemestersPUT, name='index'),
    path('flask-mysql-semester-del/', views.flaskmysqlSemestersDEL, name='index'),
    path('flask-mysql-career/', views.flaskmysqlCareer, name='index'),
    path('flask-mysql-career-get/', views.flaskmysqlCareerGET, name='index'),
    path('flask-mysql-career-post/', views.flaskmysqlCareerPOST, name='index'),
    path('flask-mysql-career-put/', views.flaskmysqlCareerPUT, name='index'),
    path('flask-mysql-career-del/', views.flaskmysqlCareerDEL, name='index'),
    path('node-mongo-grades/', views.nodemongoGrades, name='index'),
    path('node-mongo-grades-get/', views.nodemongoGradesGET, name='index'),
    path('node-mongo-grades-post/', views.nodemongoGradesPOST, name='index'),
    path('node-mongo-grades-put/', views.nodemongoGradesPUT, name='index'),
    path('node-mongo-grades-del/', views.nodemongoGradesDEL, name='index'),
    path('node-mongo-subjects/', views.nodemongoSubjects, name='index'),
    path('node-mongo-subjects-get/', views.nodemongoSubjectsGET, name='index'),
    path('node-mongo-subjects-post/', views.nodemongoSubjectsPOST, name='index'),
    path('node-mongo-subjects-put/', views.nodemongoSubjectsPUT, name='index'),
    path('node-mongo-subjects-del/', views.nodemongoSubjectsDEL, name='index'),
]

