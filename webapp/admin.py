from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request
from flask_security import current_user


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass
