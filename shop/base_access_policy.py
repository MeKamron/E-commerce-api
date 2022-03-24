from rest_access_policy import AccessPolicy


class BaseAccessPolicy(AccessPolicy):
    def is_administrator(self, request, view, action) -> bool:
        """
        Check if user from request is a staff member
        :param request:
        :param view:
        :param action:
        :return:
        """
        return request.user.is_staff
