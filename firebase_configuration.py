import os
import firebase_admin
from firebase_admin import credentials, firestore

# Set this path in your environment:
# FIREBASE_SERVICE_ACCOUNT=path/to/serviceAccountKey.json

service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT")

if not firebase_admin._apps:
    if not service_account_path:
        raise ValueError(
            "FIREBASE_SERVICE_ACCOUNT environment variable is not set."
        )

    credential = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(credential)

db = firestore.client()