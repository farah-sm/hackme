
from apps.course_topics.models import CourseTopic
from apps.user_progress.models import UserExercises, UserLessons, UserCourses


def create_user_lesson(user, lesson, progress=0, completed=False):
    user_lesson, created = UserLessons.objects.get_or_create(
        user=user,
        lesson=lesson,
        defaults={'progress': progress,
                  'completed': completed}
    )
    return user_lesson, created


def create_user_exercise(user, exercise, solution='', progress=0, completed=False):
    user_exercise, created = UserExercises.objects.get_or_create(
        user=user,
        exercise=exercise,
        defaults={'solution': solution,
                  'progress': progress,
                  'completed': completed}
    )
    return user_exercise, created


def get_completed_lessons_count(user, course_id):
    """
    Calculate the count of completed lessons for each course topic for a given user.

    :param user: The user for whom to calculate the completed lessons count
    :param course_id: The id of the course
    :return: A dictionary with course_topic IDs as keys and completed lessons count as values
    """
    course_topics = CourseTopic.objects.filter(course_id=course_id)
    user_completed_lessons = UserLessons.objects.filter(
        user=user, completed=True)
    completed_lessons_count = {}

    for course_topic in course_topics:
        # Get all lesson IDs for the current course topic
        lesson_ids = course_topic.lessons.values_list('id', flat=True)

        # Count how many of these lessons are completed by the user
        completed_count = user_completed_lessons.filter(
            lesson_id__in=lesson_ids).count()

        # Store the count in the dictionary with the course_topic ID as the key
        completed_lessons_count[course_topic.id] = completed_count

    return completed_lessons_count


def get_user_lesson_dict(user):
    """
    Fetches the UserLessons for a given user and returns a dictionary with lesson IDs as keys and UserLessons as values.

    :param user: The user for whom to fetch the UserLessons
    :return: A dictionary with lesson IDs as keys and UserLessons as values
    """
    user_lessons = UserLessons.objects.filter(user=user)
    user_lesson_dict = {
        user_lesson.lesson_id: user_lesson for user_lesson in user_lessons}
    return user_lesson_dict


def get_registered_courses(user):
    """
    Fetches all courses registered by a given user along with their completion status.

    :param user: The user for whom to fetch the registered courses
    :return: A dictionary with course IDs as keys and a tuple (registered, completed) as values
    """
    user_courses = UserCourses.objects.filter(user=user)
    registered_courses = {
        user_course.course_id: user_course.completed for user_course in user_courses}
    return registered_courses


def count_users_registered_for_course(course_id):
    """
    Returns the number of users registered for a given course.
    """
    return UserCourses.objects.filter(course_id=course_id).count()


def format_number(num):
    """
    Formats a number to include 'k' for thousands and 'm' for millions.
    """
    if num >= 1_000_000:
        return f'{num / 1_000_000:.2f}m'
    elif num >= 1000:
        return f'{num / 1000:.2f}k'
    return str(num)
