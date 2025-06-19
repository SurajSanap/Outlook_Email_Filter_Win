def load_email_list(file_path="email_list.txt"):
    with open(file_path, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]
