import re
email = "demo@gmail.com"
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{2,5}")

if EMAIL_REGEX.match(email):
  # whatever
    print("es email")
else:
    print("no es email")
