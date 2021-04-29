import frappe
import frappe.utils
from frappe.utils.oauth import get_oauth2_authorize_url, get_oauth_keys, login_via_oauth2, login_oauth_user as _login_oauth_user, redirect_post_login
import json
from frappe import _
from frappe.auth import LoginManager

@frappe.whitelist()
def login(user_name, user_password):
    doc = frappe.get_doc("Ehire Register", user_name)
    if doc.password == user_password:
        #frappe.local.flags.redirect_location = frappe.local.response.location
        frappe.local.flags.redirect_location = "/desk"
        raise frappe.Redirect
        except frappe.Redirect:
    else:
        frappe.msgprint("Please check your Username or pasword!")
    
@frappe.whitelist()
def register(user_name, user_password, user_email):
    doc = frappe.get_doc({
        "doctype": "Ehire Register",
        "username":user_name,
        "password": user_password,
        "email_address": user_email
    })
    doc.flags.ignore_permission = True
    doc.insert()
    frappe.msgprint("Done!")