from rest_framework.exceptions import APIException


class BusinessNotFound(APIException):
    status_code = 404
    default_detail = 'Business ID not found'


class BusinessPermission(APIException):
    status_code = 401
    default_detail = 'Invalid permissions'
