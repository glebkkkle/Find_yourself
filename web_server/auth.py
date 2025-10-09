#-------------------- IMPORTS ------------------------
import firebase_admin
from firebase_admin import credentials, auth, firestore
import requests
#-------------------- FRONT ------------------------

#-------------------- MAIN ------------------------
if not firebase_admin._apps:
    cred = credentials.Certificate(r"not_a_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
API_KEY = "AIzaSyD8GTlKmz_qQotCIic1ZmSrs_ZmZRDKFnw"
#-------------------- REGISTER ------------------------
def register_user(email,password):
    user = auth.create_user(
        email=email,
        password=password
    )
    db.collection("users").document(user.uid).set({
        "email":email,
    })
    return user.uid
#-------------------- LOGIN ------------------------
def login_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
    payload = {"email": email, "password": password, "returnSecureToken": True}
    response = requests.post(url, json=payload)
    return response.json()
# ---------------- SAVE QUIZ RESULT ----------------
def save_quiz_result(user_id, answers):
    db.collection("users").document(user_id).collection("results").document("quiz_id").set({
        "answers": answers,
        "timestamp": firestore.SERVER_TIMESTAMP
    })