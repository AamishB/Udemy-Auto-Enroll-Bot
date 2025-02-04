import requests
from bs4 import BeautifulSoup

def get_free_courses():
    url = "https://real.discount/filter/?category=Udemy"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    courses = []

    for link in soup.find_all("a", class_="card-title"):
        course_url = link["href"]
        if "udemy.com/course" in course_url:
            courses.append(course_url)
    
    return courses