## 📨 Outlook Email Filter App (Windows Only)

A simple Streamlit app to filter and display Outlook emails based on a list of approved sender email addresses using the `win32com.client` COM interface.
**Works only on Windows** with the **Outlook desktop application installed and configured.**

---

### 💻 Features

* Connects to your local Outlook inbox
* Filters emails based on a list of allowed senders
* Displays subject, sender, date, and body preview in a web interface
* Uses a separate `email_list.txt` file to manage approved email addresses
* Built with Python + Streamlit + pywin32

---

## 🚀 Getting Started

### ✅ Prerequisites

* Windows 10/11
* Microsoft Outlook (desktop app, configured and logged in)
* Python 3.8+
* Virtual environment (recommended)

---

### 📁 Project Structure

```
email_filter_app/
├── app.py                 # Streamlit app (entry point)
├── outlook_handler.py     # Logic to connect to Outlook and filter emails
├── email_list.txt         # List of approved sender emails
├── utils.py               # Utility to load sender list
├── requirements.txt       # Dependencies
└── README.md              # This file
```

---

### 🔮 Installation

```bash
# Clone the repo or download it
cd email_filter_app

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### 📄 `email_list.txt` Example

List of sender emails to filter (one per line):

```
boss@company.com
alerts@service.com
news@updates.org
```

---

### ▶️ Run the App

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🛠 How It Works

* Uses `win32com.client.Dispatch("Outlook.Application")` to connect to Outlook
* Fetches emails from the inbox
* Filters them by sender using `SenderEmailAddress`
* Displays results in a user-friendly Streamlit UI

---

## 🤩 Requirements

### `requirements.txt`

```
streamlit
pywin32
```

Install with:

```bash
pip install -r requirements.txt
```

---

## ❗ Common Errors & Fixes

### `CoInitialize has not been called`

> ✅ Fix: Add `pythoncom.CoInitialize()` at the start of any thread using `win32com`.

```python
import pythoncom
pythoncom.CoInitialize()
```

### Outlook not installed or not logged in

> ✅ Make sure Outlook is installed and you're signed in to your account.

---

## 🔐 Security Note

* This app reads local Outlook emails only — no credentials or external access are used.
* If you plan to distribute it, **do not share your local environment or logs**.

---

## ✅ Future Plans

* Add support for saving attachments
* Export filtered emails to CSV
* Mark as read or move emails to a folder
* Add support for Microsoft Graph (for cross-platform use)

---

## 📬 Contact / Contributions

Feel free to fork or submit issues!
Want to use this for Gmail or Mac/Linux? Ask for the **IMAP version** — it's fully cross-platform.
