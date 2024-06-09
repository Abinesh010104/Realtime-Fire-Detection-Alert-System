from ultralytics import YOLO
import cv2
import pygame
import threading
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import GMAIL_USER, GMAIL_PASS


def alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alert_sound/alarm_sound.wav")
    pygame.mixer.music.play()
    time.sleep(5)


def detect_fire_with_alarm():
    model = YOLO("models/fire.pt")

    cap = cv2.VideoCapture(0)

    alarm_on = False

    last_detection_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        fire_detected = False
        for info in results:
            boxes = info.boxes
            if len(boxes) > 0:
                fire_detected = True
                break

        if fire_detected:
            if (
                not alarm_on or time.time() - last_detection_time > 10
            ):  # Add a delay of 10 seconds before triggering the alarm again
                alarm_on = True
                last_detection_time = time.time()
                threading.Thread(target=alarm_sound).start()
                print("Fire detected! Alarm activated.")

                # Send email with the image attached
                send_email_with_image(frame)
        else:
            alarm_on = False

        cv2.imshow("Fire Detection", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def send_email_with_image(frame):
    sender_email = GMAIL_USER
    password = GMAIL_PASS
    receiver_email = "abinesh6004@gmail.com"

    subject = "Fire Detected!!!!"
    body = "Fire has been detected! Please alert the fire service."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    _, img_encoded = cv2.imencode(".png", frame)
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(img_encoded.tobytes())
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment; filename=frame.png")
    msg.attach(attachment)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, msg.as_string())


detect_fire_with_alarm()
