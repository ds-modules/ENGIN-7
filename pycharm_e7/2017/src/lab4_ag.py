import numpy as np
import unittest


# Makes doubles and NaN values in tuples work
def assertTuple(self, t1, t2, err=""):
    for v1, v2 in zip(t1, t2):
        if np.isnan(v1):
            self.assertTrue(np.isnan(v2))
        elif type(v1) is float:
            self.assertAlmostEqual(v1, v2, 6, err)
        else:
            self.assertEquals(v1, v2, err)


# Dummy variables that we populate with the student function later
my_sin_approx_fixed, my_sin_approx_tolerance, my_minimum_index, my_sort, my_reverse_without_recursion, my_reverse_with_recursion, my_calculator_inverse, my_calculator_with_undo = [None]*9


class TestQ1(unittest.TestCase):
    def test_q1(self):
        ans1 = (0.8414709848078965, 0.84146825396825398, -2.7308396425285153e-06, -3.2453164658457615e-06)
        ans2 = (-0.9589242746631385, -5.2926587301587276, -4.3337344554955894, 4.5193708929915157)
        ans3 = (0.9589242746631385, 5.2926587301587276, 4.3337344554955894, 4.5193708929915157)
        ans4 = (0.0, 0.0, 0.0, np.nan)
        assertTuple(self, my_sin_approx_fixed(1), ans1)
        assertTuple(self, my_sin_approx_fixed(5), ans2)
        assertTuple(self, my_sin_approx_fixed(-5), ans3)
        assertTuple(self, my_sin_approx_fixed(0), ans4)
        print('Question 1 Passed!')


class TestQ2(unittest.TestCase):
    def test_q2(self):
        ans1 = (2.3069118253280294, 1.7273022154697975, 0.3472924432974147)
        ans2 = (2.588190451025207, 3.6602540378443864, 2.4519052838329003)
        ans3 = (2.5482634414508505, 7.5673626291675875, 90.60344067910721)
        assertTuple(self, my_sin_approx_tolerance(1, 3, 35, 50), ans1)
        assertTuple(self, my_sin_approx_tolerance(1, 5, 45, 30), ans2)
        assertTuple(self, my_sin_approx_tolerance(5, 10, 15, 5), ans3)
        print('Question 2 Passed!')


class TestQ3(unittest.TestCase):
    def test_q3(self):
        ans1 = (
            6.018150231520484, 7.986355100472928, 0, -9.81, 9.81, 6.018150231520484, -5.747644899527072,
            8.321872030992163,
            8.425410324128677, 1.5670971406620993, 8.569908551332706, -1.628206952186122, 3.250859724304279)
        ans2 = (
            6.018150231520484, 7.986355100472928, 0, -9.81, 9.81, 6.018150231520484, -1.8236448995270722,
            6.288387148444437,
            6.018150231520484, 3.081355100472928, 6.761130191348232, -1.628206952186122, 3.250859724304279)
        ans3 = (16.383040885779835, 11.471528727020921, 0, -9.81, 9.81, 16.383040885779835, 1.6615287270209205,
                16.467079473174635, 16.383040885779835, 6.566528727020921, 17.650023461398703, -2.3387418403712377,
                6.707236051726107)
        ans4 = (12.020815280171309, 12.020815280171309, 0, -9.81, 9.81, 12.020815280171309, -7.599184719828692,
                14.221378569114806, 24.041630560342618, 4.421630560342617, 24.44485256270031, -2.4507268664977184,
                7.364933741080531)
        ans5 = (1.307336141214872, 14.942920471376183, 0, -9.81, 9.81, 1.307336141214872, -14.487079528623816,
                14.545947925618249, 3.922008423644616, 0.6837614141285471, 3.981165626621228, -3.0464669666414235,
                11.38077840029936)
        assertTuple(self, my_minimum_index(10, 53, 1.4), ans1)
        assertTuple(self, my_minimum_index(10, 53, 1), ans2)
        assertTuple(self, my_minimum_index(20, 35, 1), ans3)
        assertTuple(self, my_minimum_index(17, 45, 2), ans4)
        assertTuple(self, my_minimum_index(15, 85, 3), ans5)
        print('Question 3 Passed!')


class TestQ4(unittest.TestCase):
    def test_q4(self):
        ans1 = [0., 4.]
        ans2 = [0., 0.]
        ans3 = [4.4615384615384617, 6.692307692308]
        ans4 = [0.690909090909  , 1.036363636364, 1.381818181818, 3.109090909091]
        np.testing.assert_array_almost_equal(my_sort(np.array([0, 1]), np.array([2, 4])), ans1)
        np.testing.assert_array_almost_equal(my_sort(np.array([2, 0]), np.array([0, 1])), ans2)
        np.testing.assert_array_almost_equal(my_sort(np.array([2, 3]), np.array([7, 5])), ans3)
        np.testing.assert_array_almost_equal(my_sort(np.array([2, 3, 4, 9]), np.array([7, 5, 0, 1])), ans4)
        print('Question 4 Passed!')


class TestQ5(unittest.TestCase):
    def test_q51(self):
        ans1 = (3, 1, 2, 0)
        ans2 = (2, 2, 1, 2)
        assertTuple(self, my_reverse_without_recursion(np.array([[5, 0, 0], [1, -1, 7]])), ans1)
        assertTuple(self, my_reverse_without_recursion(np.array([[float('-inf'), 5, -1], [0, np.nan, 3]])), ans2)
        print('Question 5.1 Passed!')

    def test_q52(self):
        ans1 = [True, False, False, False]
        ans2 = [True, True, True, False]
        ans3 = [True, True, True, True]
        assertTuple(self, my_reverse_with_recursion(np.array([10])), ans1)
        assertTuple(self, my_reverse_with_recursion(np.array([[5, 0, 0], [1, -1, 7]])), ans2)
        assertTuple(self, my_reverse_with_recursion(np.array([[float('-inf'), 5, -1], [0, np.nan, 3]])), ans3)
        print('Question 5.2 Passed!')


class TestQ6(unittest.TestCase):
    def test_q6(self):
        ans1 = 8.0
        ans2 = 16.0
        ans3 = 23.161934708304955
        self.assertAlmostEqual(my_parser(np.array([0, 0, 2, 2]), np.array([0, 2, 2, 0])), ans1)
        self.assertAlmostEqual(my_parser(np.array([1, 4, 7]), np.array([1, 5, 1])), ans2)
        self.assertAlmostEqual(my_parser(np.array([3, 2, 4, 6, 7, 5]), np.array([1, 10, 6, 5, 2, 1])), ans3)
        print('Question 6 Passed!')


def run_q1(f1):
    global my_sin_approx_fixed
    my_sin_approx_fixed = f1
    q1 = unittest.TestLoader().loadTestsFromTestCase(TestQ1)
    unittest.TextTestRunner().run(q1)


def run_q2(f2):
    global my_sin_approx_tolerance
    my_sin_approx_tolerance = f2
    q2 = unittest.TestLoader().loadTestsFromTestCase(TestQ2)
    unittest.TextTestRunner().run(q2)


def run_q3(f3):
    global my_minimum_index
    my_minimum_index = f3
    q3 = unittest.TestLoader().loadTestsFromTestCase(TestQ3)
    unittest.TextTestRunner().run(q3)


def run_q4(f4):
    global my_sort
    my_sort = f4
    q4 = unittest.TestLoader().loadTestsFromTestCase(TestQ4)
    unittest.TextTestRunner().run(q4)


def run_q51(f5):
    global my_reverse_without_recursion
    my_reverse_without_recursion = f5
    q5 = unittest.TestSuite()
    q5.addTest(TestQ5("test_q51"))
    unittest.TextTestRunner().run(q5)


def run_q52(f5):
    global my_reverse_with_recursion
    my_reverse_with_recursion = f5
    q5 = unittest.TestSuite()
    q5.addTest(TestQ5("test_q52"))
    unittest.TextTestRunner().run(q5)


def run_q6(f6):
    global my_parser
    my_parser = f6
    q6 = unittest.TestLoader().loadTestsFromTestCase(TestQ6)
    unittest.TextTestRunner().run(q6)


def run_all():
    unittest.main()


if __name__ == '__main__':
    print("loaded autograder!")
