from lessinline.business.models import Business
from .exceptions import BusinessNotFound, BusinessPermission


class BusinessLookupMixins:
    def get_business(self):
        if not 'b' in self.request.query_params:
            raise BusinessNotFound
        try:
            business = Business.objects.get(id=self.request.query_params['b'])
            if business.owner != self.request.user:
                raise BusinessPermission
        except Business.DoesNotExist:
            raise BusinessNotFound
