# import schedule
# import time
# import traceback
# from generate_report import generate_combined_report

# generate_combined_report()

# def job():
#     print("🔄 Running scheduled task: generate_combined_report()")
#     try:
#         generate_combined_report()
#         print("✅ Report generated successfully.\n")
#     except Exception as e:
#         print("❌ Error while generating report:")
#         traceback.print_exc()

# # Schedule the job every 1 minute
# schedule.every(1).minutes.do(job)

# print("⏰ Scheduler started. Task will run every 1 minute.")

# # Main loop
# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(1)  # Check every second for higher responsiveness
# except KeyboardInterrupt:
#     print("\n🛑 Scheduler stopped manually.")

# import schedule
# import time
# import traceback
# from generate_report import generate_combined_report
# from alert_dispatcher import alert_authorities

# def job():
#     print("🔄 Running scheduled task: generate_combined_report()")
#     try:
#         df = generate_combined_report()
#         alert_authorities(df)
#         print("✅ Report and alerts complete.")
#     except Exception as e:
#         print("❌ Error while generating report:")
#         traceback.print_exc()

# schedule.every(1).minutes.do(job)

# print("⏰ Scheduler started. Task will run every 1 minute.")

# try:
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("\n🛑 Scheduler stopped manually.")

import schedule
import time
import traceback
from generate_report import generate_combined_report
from alert_dispatcher import send_report_email

def job():
    print("\n🔄 Running scheduled task...")
    try:
        df, report_path = generate_combined_report()
        if report_path:
            send_report_email(report_path)
        else:
            print("ℹ️ No new news today.")
    except Exception:
        print("❌ Error in scheduled task:")
        traceback.print_exc()

# Run on start + every 1 minute
job()
schedule.every(1).minutes.do(job)

print("⏰ Scheduler started. Checking every 1 minute.")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Scheduler stopped.")
