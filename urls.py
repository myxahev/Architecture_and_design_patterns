
from datetime import date

from views import Index, About, Courses, Feedback, NotFound, Course, \
    StudyPrograms, CoursesList, CreateCourse, CreateCategory, CategoryList, \
    CopyCourse, IndexAdmin


# routes = {
#     '/': Index(),
#     '/courses/': Courses(),
#     '/courses/course/': Course(),
#     '/about/': About(),
#     '/feedback/': Feedback(),
#     '/admin/': IndexAdmin(),
#     '/study-programs/': StudyPrograms(),
#     '/courses-list/': CoursesList(),
#     '/create-course/': CreateCourse(),
#     '/create-category/': CreateCategory(),
#     '/category-list/': CategoryList(),
#     '/copy-course/': CopyCourse(),
#     '404_not_found': NotFound(),
# }

# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]