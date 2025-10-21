temperature = float(input("Введите температуру на улице "))

if 20 < temperature < 30:
    
    is_rainy_in = input("На улице идет дождь? (да\нет): ")
    is_rainy = (is_rainy_in == "да")
    
    if is_rainy:
        print("Футболка, шорты и дождевик")
    else:
        print("Футболка и шорты")

elif temperature <= 0:
    print("Пуховик")

else:
    
    is_rainy_in = input("На улице идет дождь? (да\нет): ")
    is_rainy = (is_rainy_in == "да")
    
    if is_rainy:
        
        is_raining_heavily_in = input("Дождь сильный? (да\нет): ")
        is_raining_heavily = (is_raining_heavily_in == "да")
        
        if is_raining_heavily:
            print("Пальто, резиновые сапоги и зонт")
        else:
            print("Пальто и дождевик")
    
    else:
        print("Пальто")