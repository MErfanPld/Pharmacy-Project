from rest_framework import permissions

class HasCategoryDrugPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return request.user.has_perm('app.category_drug_list')
        if view.action in ['create']:
            return request.user.has_perm('app.category_drug_create')
        if view.action in ['update', 'partial_update']:
            return request.user.has_perm('app.category_drug_edit')
        if view.action in ['destroy']:
            return request.user.has_perm('app.category_drug_delete')
        return True

class HasDrugPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list']:
            return request.user.has_perm('app.drugs_list')
        if view.action in ['create']:
            return request.user.has_perm('app.drugs_create')
        if view.action in ['update', 'partial_update']:
            return request.user.has_perm('app.drugs_edit')
        if view.action in ['destroy']:
            return request.user.has_perm('app.drugs_delete')
        return True
