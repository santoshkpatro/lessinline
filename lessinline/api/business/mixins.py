from lessinline.business.models import Business
from .exceptions import BusinessNotFound, BusinessPermission


class BusinessLookupMixins:
    def get_business(self):
        if not 'business_id' in self.request.query_params:
            raise BusinessNotFound
        business_id = self.request.query_params['business_id']
        try:
            business = Business.objects.get(id=business_id)
            if not business.owner == self.request.user:
                raise BusinessPermission
            self.business = business
        except Business.DoesNotExist:
            raise BusinessNotFound
