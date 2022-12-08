# Упражнение 8.14

def make_car(model, brand, **car_info):
    car_info['model'] = model
    car_info['brand'] = brand
    return car_info


car = make_car('creta', 'hyndai', color='white', power=149.6)

print(car)
