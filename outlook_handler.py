import win32com.client
import pythoncom  # Add this

def fetch_filtered_emails(allowed_senders, max_emails=100):
    pythoncom.CoInitialize()  # <-- This is the fix

    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    inbox = namespace.GetDefaultFolder(6)  # Inbox
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)

    filtered = []

    for message in messages:
        try:
            sender = message.SenderEmailAddress.lower()
            if sender in allowed_senders:
                filtered.append({
                    "Sender": sender,
                    "Subject": message.Subject,
                    "Received": message.ReceivedTime.strftime("%Y-%m-%d %H:%M"),
                    "Preview": message.Body[:150]
                })
            if len(filtered) >= max_emails:
                break
        except Exception:
            continue

    return filtered
