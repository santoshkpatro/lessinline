from lessinline.business.models import Business
from lessinline.services.models import Service
from .exceptions import BusinessNotFound, InvalidPermission, ServiceNotFound


class BusinessLookupMixins:
    def get_business(self):
        if not 'business_id' in self.request.query_params:
            raise BusinessNotFound
        business_id = self.request.query_params['business_id']
        try:
            business = Business.objects.get(id=business_id)
            if not business.owner == self.request.user:
                raise InvalidPermission
            self.business = business
        except Business.DoesNotExist:
            raise BusinessNotFound


class ServiceLookupMixins:
    def get_service(self):
        if not 'service_id' in self.request.query_params:
            raise ServiceNotFound
        service_id = self.request.query_params['service_id']
        try:
            service = Service.objects.get(id=service_id)
            if not service.business.owner == self.request.user:
                raise InvalidPermission
            self.service = service
        except Service.DoesNotExist:
            raise ServiceNotFound
