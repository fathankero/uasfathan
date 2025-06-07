import os

path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print("GOOGLE_APPLICATION_CREDENTIALS =", path)
print("File exists:", os.path.exists(path) if path else False)
