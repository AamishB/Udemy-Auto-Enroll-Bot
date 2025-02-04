import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("7929716021:AAEaI7raT7JE0q0ICsuH7qyBPVPJQKrWS1M")
TELEGRAM_CHAT_ID = os.getenv("6057513600")

def send_notification(message):
    """Sends a message to Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

def enroll_in_course(course_url):
    """Automates course enrollment using stored cookies."""
    driver = webdriver.Chrome()
    load_cookies(driver)

    driver.get(course_url)
    time.sleep(3)

    try:
        enroll_button = driver.find_element("xpath", "//button[contains(text(), 'Enroll now')]")
        enroll_button.click()
        message = f"✅ Enrolled in: {course_url}"
        send_notification(message)
    except Exception as e:
        message = f"❌ Failed to enroll in {course_url}: {e}"
        send_notification(message)

    driver.quit()
