# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ocean"
app_title = "Ocean"
app_publisher = "bobzz.zone@gmail.com"
app_description = "ocean"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"
website_context = {
	"splash_image": "/assets/angel/images/ms-icon-310x310.png",
	"favicon"     :	"/assets/angel/images/favicon-16x16.png"
}
# Includes in <head>
# ------------------
after_install = "angel.install.after_install"
# include js, css files in header of desk.html
# app_include_css = "/assets/ocean/css/ocean.css"
# app_include_js = "/assets/ocean/js/ocean.js"

# include js, css files in header of web template
# web_include_css = "/assets/ocean/css/ocean.css"
# web_include_js = "/assets/ocean/js/ocean.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ocean.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ocean.install.before_install"
# after_install = "ocean.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ocean.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ocean.tasks.all"
# 	],
# 	"daily": [
# 		"ocean.tasks.daily"
# 	],
# 	"hourly": [
# 		"ocean.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ocean.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ocean.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ocean.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ocean.event.get_events"
# }

