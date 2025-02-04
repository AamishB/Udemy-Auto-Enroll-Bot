import schedule
import time

def job():
    courses = get_free_courses()
    for course in courses:
        enroll_in_course(course)

# Schedule to run every hour
schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
