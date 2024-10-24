from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_delete():
    bst = CarInventory()

    car1 = Car("Honda", "CRV", 2007, 6500)
    car2 = Car("BMW", "M4", 2024, 77000)
    car3 = Car("Toyota", "RAV4", 2023, 28275)
    car4 = Car("Mercedes", "Sprinter", 2022, 40000)
    car5 = Car("Mercedes", "Sprinter", 2014, 24500)
    car6 = Car("Audi", "A4", 2021, 32000)
    car7 = Car("Ford", "Ranger", 2021, 23000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)
    bst.addCar(car6)
    bst.addCar(car7)

    assert bst.getSuccessor("Honda", "CRV") == car4
    assert bst.getSuccessor("Toyota", "RAV4") is None
    assert bst.getSuccessor("Audi", "A4") == car2
    assert bst.getSuccessor("Ford", "Ranger") == car1

    assert bst.inOrder() ==\
                      """\
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
Make: HONDA, Model: CRV, Year: 2007, Price: $6500
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $24500
Make: TOYOTA, Model: RAV4, Year: 2023, Price: $28275
"""
    
    bst.removeCar("Mercedes", "Sprinter", 2022, 40000)
    assert bst.inOrder() == \
           """\
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
Make: HONDA, Model: CRV, Year: 2007, Price: $6500
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $24500
Make: TOYOTA, Model: RAV4, Year: 2023, Price: $28275
"""
    assert bst.preOrder() ==\
                      """\
Make: HONDA, Model: CRV, Year: 2007, Price: $6500
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
Make: TOYOTA, Model: RAV4, Year: 2023, Price: $28275
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $24500
"""
    assert bst.postOrder() ==\
                      """\
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $24500
Make: TOYOTA, Model: RAV4, Year: 2023, Price: $28275
Make: HONDA, Model: CRV, Year: 2007, Price: $6500
"""
    
    bst.removeCar("Mercedes", "Sprinter", 2014, 24500)
    assert bst.inOrder() == \
           """\
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
Make: HONDA, Model: CRV, Year: 2007, Price: $6500
Make: TOYOTA, Model: RAV4, Year: 2023, Price: $28275
"""
    
    bst.removeCar("Honda", "CRV", 2007, 6500)
    assert bst.inOrder() == \
           """\
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
Make: TOYOTA, Model: RAV4, Year: 2023, Price: $28275
"""

    bst.removeCar("Toyota", "RAV4", 2023, 28275)
    assert bst.inOrder() == \
           """\
Make: AUDI, Model: A4, Year: 2021, Price: $32000
Make: BMW, Model: M4, Year: 2024, Price: $77000
Make: FORD, Model: RANGER, Year: 2021, Price: $23000
"""
