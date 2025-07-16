from plyer import notification
import time

if __name__ == '__main__':
  while True:
     notification.notify(
          title= "Time to Take a Break ! ",
          message ="You've been working for a while. Stretch, hydrate, and rest your eyes 😊",
          timeout= 10)
     time.sleep(3600)