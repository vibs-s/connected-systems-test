from behave import given
from test.utils.api_client import create_pet

@given('I create a new pet in the inventory system')
def step_create_pet(context):
    pet = create_pet()
    context.pet_id = pet["id"]
    context.pet_name = pet["name"]