import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

@timing_decorator
def get_even_numbers(start,end):
    return [i for i in range(start, end+1) if i%2 == 0]

start_range = int(input("Введіть число для початку списку: "))
end_range = int(input("Введіть число для кінця списку: "))
even_numbers = get_even_numbers(start_range,end_range)
print(even_numbers)
