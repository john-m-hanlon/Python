buildingSF = 21018
officeSpace = 3500
avlBuildingSF = buildingSF - officeSpace
avgroomSF = 100
numberOfRooms = avlBuildingSF / avgroomSF
buildingRent = 12500
months = 12
yearlyRent = buildingRent * months
print('Yearly rent per company:',yearlyRent / numberOfRooms)
print('Number of rooms:',numberOfRooms)
hit1MM = 1000000/numberOfRooms
print('Price per company to hit 1MM in Rev:',hit1MM)
print('Price per company/month to hit 1MM in Rev:',hit1MM/months)
print('Price per sq ft/month to hit 1 MM in rev:',hit1MM/months/avgroomSF)

print(1000000/avlBuildingSF/months)

# Variables: rent per SF, crops that can grow in that SF, how much that can be sold for, what is electricity, what is water, gas, 
# strategic sourcing for fertilizers, etc.
#3x3 grower = 4 medium sized plants
print(avgroomSF*.75/9*4)
# 1 lb wholesale is approx $1500 to $3000
# 1 lb is approx 5-6 plans
# in a 100 SF room, with 75% dedicated to growing and 25% utilities, you can grow approx 33 plants
# with 33 plants you can grow approx 5-6 lbs
# wholesale that would cost $7500-18000
# need to come in around a couple of thousand -- 5k a customer
