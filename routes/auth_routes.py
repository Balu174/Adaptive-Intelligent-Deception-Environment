from flask import Blueprint, request, redirect, session
from utils.security import is_sql_injection
from services.logger_service import log_attack

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if is_sql_injection(username, password):

            log_attack({
                "type": "SQL Injection Attempt",
                "severity": "High"
            })

            return redirect("/fake_system")

        if username == "mohith" and password == "12345":
            session["is_admin"] = True
            return redirect("/dashboard")

    return "Login Page"