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

  # минимальное число файлов, реализующих одно требование
  def with_min_traced_files(self, n):
    self.min_traced_files = n

  # максимальное число файлов, реализующих одно требований
  def with_max_traced_files(self, n):
    self.max_traced_files = n

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

    if min_count_useful_requirements < 0:
      raise Exception('too little min count of useful requirements')
    if min_count_useful_requirements > count_requirements:
      raise Exception('too much min count of useful requirements')
    if min_count_useful_requirements > max_count_useful_requirements:
      raise Exception('min count of useful requirements more then max count of useful requirements')
    if max_count_useful_requirements > count_requirements:
      raise Exception('too much max count of useful requirements')

    equipments = []
    for equipment_number in range(count_equipments):
      total_count_useful_requirements = randint(min_count_useful_requirements, max_count_useful_requirements)
      requirements = np.zeros(count_requirements)
      count_useful_requirements = 0
      for requirement_number in range(count_requirements):
        if count_useful_requirements < total_count_useful_requirements:
          requirements[requirement_number] = 1
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
    # Здесь сумма элементов в каждой строке равна 1
    # Размерность матрицы: count_source_files x count_equipments
    result = []

    count_source_files = self.count_source_files
    count_requirements = self.count_requirements

    for number_source_file in range(count_source_files):
      traced_data = self.__get_traced_data()
      traced_files = traced_data[0]
      traceability_share = traced_data[1]

      traced_list = np.zeros(count_requirements)
      count_traced = 0
      for number_requirement in range(count_requirements):
        if count_traced < traced_files:
          traced_list[number_requirement] = traceability_share
        count_traced += 1
      shuffle(traced_list)
      result.append(traced_list)

    return np.array(result)

  def __get_traced_data(self):
    min_traced_files = self.min_traced_files
    max_traced_files = self.max_traced_files

    traced_files = 0
    traceability_share = 0

    boo = True
    while boo:
      traced_files = randint(min_traced_files, max_traced_files)
      traceability_share = 1 / traced_files
      if traced_files * traceability_share == 1:
        boo = False

    return (traced_files, traceability_share)

  # генерировать матрицу зависимостей между файлами исходного кода
  def generate_d(self):
    count_source_files = self.count_source_files
    min_count_dependencies = self.min_count_dependencies
    max_count_dependencies = self.max_count_dependencies

    if min_count_dependencies < 0:
      raise Exception('too little min count of dependencies')
    if min_count_dependencies > count_source_files:
      raise Exception('too much min count of dependencies')
    if min_count_dependencies > max_count_dependencies:
      raise Exception('min count of dependencies more then max count of dependencies')
    if max_count_dependencies > count_source_files:
      raise Exception('too much max count of dependencies')

    result = []
    for number_source_file in range(count_source_files):
      count_dependencies = randint(min_count_dependencies, max_count_dependencies)
      dependencies = np.zeros(count_source_files)
      count_active_dependencies = 0
      for number_dependency in range(count_source_files):
        if count_active_dependencies < count_dependencies:
          dependencies[number_dependency] = 1
        count_active_dependencies += 1
      shuffle(dependencies)
      result.append(dependencies)

    return np.array(result)
