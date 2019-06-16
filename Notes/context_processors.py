from Notes.forms import SearchBarForm


def SearchBarContext(request):
    """
    Produces a context variable for the searchbar that's available across
    all pages.
    :param request:
    :return:
    """
    return {'searchbar':SearchBarForm()}

def SetCurrentCourses(request):
    """
    Produces a context variable for all a user's current courses that's
    available across all pages
    :param request:
    :return:
    """
    user = request.user

    try:
        current_term = user.terms.all().filter(user=user, current = True)[0]
        current_courses = current_term.course.all()
    except(AttributeError,IndexError):
        current_courses = None

    return {'current_course': current_courses}