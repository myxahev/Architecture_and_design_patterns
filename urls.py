from views import Index, About, Courses, Feedback, NotFound, Course, \
    StudyPrograms, CoursesList, CreateCourse, CreateCategory, CategoryList, \
    CopyCourse, IndexAdmin


routes = {
    '/': Index(),
    '/courses/': Courses(),
    '/courses/course/': Course(),
    '/about/': About(),
    '/feedback/': Feedback(),
    '/admin/': IndexAdmin(),
    '/study-programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse(),
    '404_not_found': NotFound(),
}