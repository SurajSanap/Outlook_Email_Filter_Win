
```markdown
# 📨 Email Filter App (Cross-Platform: Windows & macOS)

A Streamlit-powered Python app that connects to your email inbox via **IMAP**, filters messages from a list of approved sender addresses, and displays the results in a friendly web interface.

✅ Works on **Windows**, **macOS**, and **Linux**  
✅ Supports **Gmail** or any IMAP-compatible email provider  
✅ Modular and extendable Python code  
✅ Easily manage filter rules via `email_list.txt`  

---

## 📂 Project Structure

```

email\_filter\_app/
├── app.py                 # Streamlit UI (main entry point)
├── imap\_handler.py        # Core IMAP email fetch/filter logic
├── utils.py               # Helper to load email list
├── email\_list.txt         # Add sender emails to filter here
├── requirements.txt       # Streamlit and dependencies
└── README.md              # You're here!

````

---

## 🚀 Features

- Connects to your email inbox securely using IMAP
- Reads and parses the latest emails
- Filters only messages from approved senders
- Displays subject, sender, received date, and body preview
- Web UI built with **Streamlit**

---

## 🔧 Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/yourusername/email-filter-app.git
cd email_filter_app
````

### 2. Create and activate a virtual environment (optional but recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your sender list

Edit `email_list.txt` and add **one sender email per line**:

```txt
boss@gmail.com
alerts@example.com
news@dailyfeed.org
```

---

## 🔐 Gmail Setup Notes

> Gmail blocks basic username/password logins. You must:

* Enable **IMAP** in your Gmail settings (via [https://mail.google.com](https://mail.google.com) > Settings > See all settings > Forwarding and POP/IMAP)
* Create an **App Password** (if 2FA is on) via:
  [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

Use this app password in the login form.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the browser URL provided (usually [http://localhost:8501](http://localhost:8501)).

---

## 📦 Optional Features You Can Add

* Export filtered emails to CSV
* Download attachments
* Mark emails as read
* Add reply/send functionality
* Support multiple folders (e.g., Promotions, Social)
* Use Microsoft Outlook/Exchange via Graph API

---

## 🧠 Tech Stack

* [Streamlit](https://streamlit.io/) – Web interface
* `imaplib`, `email` – Built-in Python libraries for email parsing
* Compatible with Python 3.7+

---

## 🛠️ Troubleshooting

| Problem            | Solution                                                                          |
| ------------------ | --------------------------------------------------------------------------------- |
| IMAP login fails   | Use App Password instead of your Gmail password                                   |
| No emails found    | Make sure the sender exists and `email_list.txt` is correct                       |
| UnicodeDecodeError | We handle most encodings, but malformed emails may still fail. Let us know if so. |

---

## 📄 License

MIT – free to use, modify, and share.

---

