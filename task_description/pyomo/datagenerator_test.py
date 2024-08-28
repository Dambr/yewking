from datagenerator import DataGenerator

def test_generate_e(datagenerator):
  datagenerator.with_count_equipments(2)
  datagenerator.with_count_requirements(3)
  datagenerator.with_min_count_useful_requirements(1)
  datagenerator.with_max_count_useful_requirements(2)

  e = datagenerator.generate_e()
  print(e)

def test_generate_p(datagenerator):
  datagenerator.with_count_requirements(3)
  datagenerator.with_min_price(-5)
  datagenerator.with_max_price(10)

  p = datagenerator.generate_p()
  print(p)

def test_generate_t(datagenerator):
  datagenerator.with_count_source_files(4)
  datagenerator.with_count_requirements(3)
  datagenerator.with_min_traced_files(1)
  datagenerator.with_max_traced_files(2)

  t = datagenerator.generate_t()
  print(t)

def test_generate_d(datagenerator):
  datagenerator.with_count_source_files(4)
  datagenerator.with_min_count_dependencies(0)
  datagenerator.with_max_count_dependencies(2)

  d = datagenerator.generate_d()
  print(d)

if __name__ == "__main__":
  datagenerator = DataGenerator()
  test_generate_d(datagenerator)
