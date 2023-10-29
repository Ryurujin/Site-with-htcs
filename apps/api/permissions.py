from rest_framework.permissions import BasePermission

#user
class UserPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET":
            return request.user.is_staff
        
        elif request.method == "POST":
            return request.user.is_staff
        
class UserDetailPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated
        
#post
class PostPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return request.user.is_staff
        
        elif request.method == 'POST':
            return request.user.is_staff
        
class PostDetailPermission(BasePermission):
    def has_permission(self, request, view):
        
        if request.method in ['GET', 'PUT', 'DELETE']:
            return request.user.is_authenticated 
