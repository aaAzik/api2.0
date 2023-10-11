from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class UserDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated

class ProductPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class ProductDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated

class CategoryPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class CategoryDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff