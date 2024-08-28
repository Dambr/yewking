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

if __name__ == "__main__":
  datagenerator = DataGenerator()
  test_generate_p(datagenerator)
