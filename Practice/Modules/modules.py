import converters
from converters import lbs_to_kg
from find_max import find_max
# import ecommerce.shipping
from ecommerce.shipping import calc_shipping
from ecommerce import shipping

shipping.calc_shipping()
calc_shipping()
print(lbs_to_kg(155))

print(converters.kg_to_lbs(70))

print(find_max([5, 10, 20, 30, 50]))
