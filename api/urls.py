# from django.urls import path

# from .views import StudentListView

# urlpatterns=[
#     path("students/",StudentListView.as_view(),name= "student_list_view")
# ]
from django.urls import path
from .views import StudentListView
from.views import StudentDetailView

rom django.urls import path
from .views import PeriodListViews
from .views import  CourseListViews
from .views import ClassRoomListViews
from .views import StudentListView
from .views import TeacherListViews
urlpatterns = [
    path('student/', StudentListView.as_view(), name = 'student_list_view'),
     path('Teacher/',TeacherListViews.as_view(),name = "teachers_list_view"),
    path('Courses/',CourseListViews.as_view(),name = "course_list_view"),
   path('ClassRoom/',ClassRoomListViews.as_view(),name = "class_room_list_view"),
 path('Period/',PeriodListViews.as_view(),name = "class_period_list_view"),
path('student/<int:id>/',StudentDetailView.as_view(),name='student_list_view')
]