# import smtplib
# from email.message import EmailMessage

# def send_email_alert(subject, body, recipients):
#     msg = EmailMessage()
#     msg["Subject"] = subject
#     msg["From"] = "tempmail09726@gmail.com"
#     msg["To"] = ", ".join(recipients)
#     msg.set_content(body)

#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#         smtp.login("tempmail09726@gmail.com", "oftw jtqa tloj xuwm")  # Use App Password
#         smtp.send_message(msg)

# def alert_authorities(df):
#     for _, row in df.iterrows():
#         severity = row["severity"]
#         recipients = []

#         if severity == "Small":
#             recipients = ["maheshvengala4321@gmail.com"]
#         elif severity == "Medium":
#             recipients = ["satyakarthikvelivela@gmail.com"]
#         elif severity == "Huge":
#             recipients = ["projects.aravind@gmail.com"]

#         subject = f"[{severity}] {row['title'][:60]}"
#         body = f"{row['title']}\n\nSource: {row['source']}\nLink: {row['url']}"
#         send_email_alert(subject, body, recipients)

import smtplib
from email.message import EmailMessage
import traceback

def send_report_email(attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "📰 Andhra Pradesh Daily News Report"
    msg["From"] = "Web Scraping"
    msg["To"] = "satyakarthikvelivela@gmail.com, maheshvengala4321@gmail.com, projects.aravind@gmail.com"

    msg.set_content("Attached is today's news report for Andhra Pradesh with categorized severity.")

    try:
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.wordprocessingml.document', filename=file_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("tempmail09726@gmail.com", "oftw jtqa tloj xuwm")
            smtp.send_message(msg)

        print("✅ Email sent with Word report.")

    except Exception:
        print("❌ Failed to send email:")
        traceback.print_exc()
