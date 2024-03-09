app_name = "mansico_meta_integration"
app_title = "Mansico Meta Integration"
app_publisher = "Mansy"
app_description = "This project is about syncing Facebook leads with ERPnext, When Clients fill Facebook ads instant forms app automatic fetch new created leads and create lead automatic in Lead doctype. Also on changing the Lead Status the new status sent to meta Pixel."
app_email = "ahmedmansy265@gmail.com"
app_license = "mit"
required_apps = ["erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mansico_meta_integration/css/mansico_meta_integration.css"
# app_include_js = "/assets/mansico_meta_integration/js/mansico_meta_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/mansico_meta_integration/css/mansico_meta_integration.css"
# web_include_js = "/assets/mansico_meta_integration/js/mansico_meta_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mansico_meta_integration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mansico_meta_integration/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mansico_meta_integration.utils.jinja_methods",
# 	"filters": "mansico_meta_integration.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mansico_meta_integration.install.before_install"
# after_install = "mansico_meta_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mansico_meta_integration.uninstall.before_uninstall"
# after_uninstall = "mansico_meta_integration.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mansico_meta_integration.utils.before_app_install"
# after_app_install = "mansico_meta_integration.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mansico_meta_integration.utils.before_app_uninstall"
# after_app_uninstall = "mansico_meta_integration.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mansico_meta_integration.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
    "Lead": {
        # will run before a ToDo record is inserted into database
        "validate": "mansico_meta_integration.overrides.validate_lead",
    }
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mansico_meta_integration.tasks.all"
# 	],
# 	"daily": [
# 		"mansico_meta_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"mansico_meta_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mansico_meta_integration.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mansico_meta_integration.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mansico_meta_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mansico_meta_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mansico_meta_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mansico_meta_integration.utils.before_request"]
# after_request = ["mansico_meta_integration.utils.after_request"]

# Job Events
# ----------
# before_job = ["mansico_meta_integration.utils.before_job"]
# after_job = ["mansico_meta_integration.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mansico_meta_integration.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

import frappe.utils.safe_exec as _frappe_safe_exec
import mansico_meta_integration.overrides as _mansico_meta_integration_overrides
_frappe_safe_exec.safe_exec = _mansico_meta_integration_overrides.safe_exec