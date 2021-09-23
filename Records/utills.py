import uuid
from Customers.models import customer
from Profiles.models import TRUCK_OWNWER



def generate_code():
    code = str(uuid.uuid4()).replace('-', '').upper()[:12]
    return code


def get_truck_owners_from_id(val):
    truck_owner= TRUCK_OWNWER.objects.get(id=val)
    return truck_owner.user.username

def get_customer_from_id(val):
    third_party_owners = customer.objects.get(id=val)
    return third_party_owners