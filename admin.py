from flask import Blueprint, render_template, redirect, url_for, request, session


admin_bp = Blueprint('admin',__name__,url_prefix="/admin")

ADMIN_USERNAME = "ranajit"
ADMIN_PASSWORD = "842073"


@admin_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("admin/admin.html")
    else:
        return render_template("")
                
        

