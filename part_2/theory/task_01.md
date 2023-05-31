1. Задача на циклический итератор. Секция статьи "1. Задача на циклический итератор."
Надо написать класс CyclicIterator.
Итератор должен итерироваться по итерируемому объекту 
(list, tuple, set, range, Range2, и т. д.), 
и когда достигнет последнего элемента, начинать сначала.

cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)

Скопировать
Основа:

class CyclicIterator:
    def __iter__(self):
        pass

    def __next__(self):
        pass

Скопировать
Для проверки. Ожидаемый вывод программы:

0
1
2
0
1
2
0
1
2
....