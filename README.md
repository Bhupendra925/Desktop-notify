# Desktop-notify
This is a simple Python script that uses the plyer library to send desktop notifications every hour reminding you to take a break, hydrate, stretch, and rest your eyes. Ideal for developers, students, or anyone working long hours on a computer.

# 🛎️ Break Reminder Notification (Python)

This Python script helps you maintain better health while working on a computer for long hours. It sends a reminder every hour to take a break — encouraging you to stretch, hydrate, and rest your eyes.

---

## 📌 Features

- Sends a system notification every 1 hour (3600 seconds)
- Simple and lightweight
- Runs infinitely in the background
- Customizable notification message and interval

---

## 🖥️ Requirements

- Python 3.x
- `plyer` library

##Install using pip:


## pip install plyer
🚀 How to Run
bash
Copy
Edit
python rest.py
Or double-click if packaged with .bat file for auto-start.

## 🛠️ Code Overview
python
Copy
Edit
from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Time to Take a Break!",
            message="You've been working for a while. Stretch, hydrate, and rest your eyes 😊",
            timeout=10
        )
        time.sleep(3600)  # 1 hour
##🧠 Use Case
Perfect for developers, designers, or students

Can be scheduled to auto-start with system using Windows Startup folder or Task Scheduler

##📂 Optional Enhancement
Add an .ico icon to customize the notification

Use .bat file to auto-start the script with system boot

##📃 License
This project is open-source and available under the MIT License.

##💡 Author
Made with ❤️ by [Bhupendra vishwakarma]



## 📝 Suggestion:
- Rename your file to `rest.py`
- Include this `README.md` in your GitHub repo
- Add a `requirements.txt` with this line:
