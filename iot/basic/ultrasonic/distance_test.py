import unittest

# Returns the distance between the sensor and the object in centimeters
def distance(delta: float) ->float:
  # Halfing the time taken
  delta *= 0.5
  speed = 330 #  330m/s

  # Converting the distance to centimeters
  return (delta * speed) * 100

class TestCalDistance(unittest.TestCase):
  def test_basicCheck(self):
    result = distance(4)
    self.assertEqual(result, 66000)

if __name__ == '__main__' :
  unittest.main()