import functools
import time


def slow_down_repeater(call_count = 5, start_sleep_time: int = 2, border_sleep_time: int = 10) -> object:
    print("Начало работы")
    def decorator(func) -> object:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t:int = start_sleep_time
            for i in range(call_count):
                t = start_sleep_time * 2 ** i if (t < border_sleep_time) else border_sleep_time
                time.sleep(t)
                val = func(*args, **kwargs)
                print(f"Запуск номер {i}. Ожидание: {t} секунд. результат функции = {val}")
            return val
        return wrapper
    return decorator


@slow_down_repeater(call_count = 5, start_sleep_time = 2 ,border_sleep_time = 10)
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(2))
