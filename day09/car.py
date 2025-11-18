# Vehicle 클래스 정의
class Vehicle:
    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price
    def show(self):


# Car 클래스 (Vehicle의 서브클래스)
class Car(Vehicle):
    def __init__(self, color, weight, price, engine, passengers):
        super().__init__(color, weight, price)
        self.engine = engine
        self.passengers = passengers
    def show(self):

# Truck 클래스 (Vehicle의 서브클래스)
class Truck(Vehicle):
    def __init__(self, color, weight, price, wheels, load_weight):
        super().__init__(color, weight, price)
        self.wheels = wheels
        self.load_weight = load_weight
    def show(self):

if __name__ == '__main__': # p.471 참조
    # Car 객체 5개 생성
    car_list = [
        Car("Red", 1500, 20000, "V6", 4),
        Car("Blue", 1400, 25000, "V8", 5),
        Car("Black", 1600, 30000, "Electric", 4),
        Car("White", 1200, 18000, "Hybrid", 4),
        Car("Green", 1300, 22000, "V6", 5)
    ]

    # Truck 객체 5개 생성
    truck_list = [
        Truck("Yellow", 3000, 40000, 8, 10000),
        Truck("Blue", 3200, 45000, 10, 12000),
        Truck("White", 2800, 35000, 6, 8000),
        Truck("Black", 3500, 50000, 12, 15000),
        Truck("Red", 3400, 48000, 10, 14000)
    ]

    # 생성된 객체들 출력 - show()를 사용한 출력 코딩 
    print("Cars:")
    for car in carList:
        car.


    print("\nTrucks:")
