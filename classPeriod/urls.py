from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, ClassroomViewSet, ClassPeriodViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'class-periods', ClassPeriodViewSet)

urlpatterns = router.urls