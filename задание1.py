#14. Ввести список А из 10 элементов, найти разность положительных элементов кратных 11, их количество и вывести результаты на экран.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
  A = list(map(int, input("Введите элементы:").split()))
  if len(A) != 10:
    print("Неверный размер списка")
  else:
      count=0
      c=0
      s = sum([a for a in A if a>0 and a//11])
      for a in A:
          if a>0 and a//11:
              b=(max(A))
              if a<b:
                  count+=a
                  c=b-count
      print("Разность элементов:",c,)
      print("Сумма элементов:",s,)

