import numpy as np
from random import randint, shuffle

class DataGenerator():

  # число комплектаций
  def with_count_equipments(self, n):
    self.count_equipments = n

  # число требований
  def with_count_requirements(self, n):
    self.count_requirements = n

  # минимальное число полезных требований
  def with_min_count_useful_requirements(self, n):
    self.min_count_useful_requirements = n

  # максимальное число полезных требований
  def with_max_count_useful_requirements(self, n):
    self.max_count_useful_requirements = n

  # число файлов исходного кода
  def with_count_source_files(self, n):
    self.count_source_files = n

  # число плагинов
  def with_count_plugins(self, n):
    self.count_plugins = n

  # минимальное число зависимостей у файла исходного кода
  def with_min_count_dependencies(self, n):
    self.min_count_dependencies = n

  # макисмальное число зависимостей у файла исходного кода
  def with_max_count_dependencies(self, n):
    self.max_count_dependencies = n

  # минимальная цена сопровождения требования
  def with_min_price(self, n):
    self.min_price = n

  # максимальная цена сопровождения требования
  def with_max_price(self, n):
    self.max_price = n

  # генерировать комплектации
  def generate_e(self):
    count_equipments = self.count_equipments
    count_requirements = self.count_requirements
    min_count_useful_requirements = self.min_count_useful_requirements
    max_count_useful_requirements = self.max_count_useful_requirements

    if min_count_useful_requirements > count_requirements:
      raise Exception('too much min count of useful requirements')
    if max_count_useful_requirements > count_requirements:
      raise Exception('too much max count of useful requirements')

    equipments = []
    for equipment_number in range(count_equipments):
      total_count_useful_requirements = randint(min_count_useful_requirements, 
                                             max_count_useful_requirements)
      requirements = []
      count_useful_requirements = 0
      for requirement_number in range(count_requirements):
        use_requirement = 0
        if count_useful_requirements <= total_count_useful_requirements:
          use_requirement = 1
        requirements.append(use_requirement)
        count_useful_requirements += 1
      shuffle(requirements)
      equipments.append(requirements)
    return np.array(equipments)


  # генерировать матрицу цен
  def generate_p(self):
    count_requirements = self.count_requirements
    min_price = self.min_price
    max_price = self.max_price

    prices = [[randint(min_price, max_price) for i in range(count_requirements)] for j in range(count_requirements)]

    return np.array(prices)
    

  # генерировать матрицу трассируемости требований на файлы исходного кода
  def generate_t(self):
    pass

  # генерировать матрицу зависимостей между файлами исходного кода
  def generate_d(self):
    pass
