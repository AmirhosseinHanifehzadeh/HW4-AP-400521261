# ------------------- importing modules -------------------
import unittest


# ------------------- integer class ------------------- 
class Integer:
    def __init__(self, num):
        self.num = num

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, val):
        if not isinstance(val, int):
            raise TypeError("num should be int!")
        self._num = val

    def __add__(self, other):
        if type(other) is Matrix:
            return other + self
        elif type(other) is Complex:
            return Complex(other.real + self.num, other.complex)
        elif type(other) is Integer:
            return Integer(self.num + other.num)

    def __mul__(self, other):
        if type(other) is Matrix:
            return other * self
        elif type(other) is Complex:
            return Complex(other.real * self.num , other.complex * self.num) 
        elif type(other) is Integer:
            return Integer(self.num * other.num)

    def __repr__(self):
        return str(self._num)

    def __eq__(self, other):
        if type(other) is Integer:
            if self.num == other.num:
                return True
            else:
                return False
        return False


# ------------------- Complex class -------------------
class Complex:
    def __init__(self, real, complex):
        self.real = real
        self.complex = complex

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, num):
        if not isinstance(num, int):
            raise TypeError("real part should be int")
        self._real = num

    @property
    def complex(self):
        return self._complex

    @complex.setter
    def complex(self, num):
        if not isinstance(num, int):
            raise TypeError('Imaginary part should be imaginary part!')

        self._complex = num

    def __add__(self, other):
        if type(other) is Matrix:
            return other + self
        elif type(other) is Integer:
            return Complex(self._real + other._num, self._complex)
        elif type(other) is Complex:
            return Complex(self._real + other._real, self._complex + other._complex)
        else:
            raise TypeError

    def __eq__(self,other):
        if type(other) is Complex:
            if self.real == other.real:
                if self.complex == other.complex:
                    return True
        return False

    def __repr__(self):
        return str(f"Complex({self.real}, {self.complex})")

# ------------------- Matrix class -------------------
class Matrix:
    def __init__(self, row, col, *components):
        if not isinstance(row, int) or not isinstance(col, int):
            raise TypeError('row and column both should be integer.')
        self.row = row
        self.col = col
        self.matrix = matrixPack(components, self.row, self.col)
        

    @staticmethod
    def make_unit_matrix(n):
        unit_matrix = []
        if not isinstance(n, int):
            raise TypeError('you should enter an integer.')
        for i in range(n):
            unit_matrix.append([])
            for j in range(n):
                if i == j:
                    unit_matrix[i].append(1)
                else:
                    unit_matrix[i].append(0)
        return unit_matrix

    @staticmethod
    def get_ith_row(matrix, row, col,  i):
        if not isinstance(row, int) or not isinstance(col, int) or not isinstance(i, int):
            return TypeError
        if i > row:
            return ValueError(f"your matrix deosn't have {i} row!")

        return matrix[(i - 1) * col: i * col]

    @staticmethod
    def get_ith_col(matrix, row, col, i):
        if not isinstance(row, int) or not isinstance(col, int) or not isinstance(i, int):
            return TypeError
        elif i > col:
            return ValueError(f"your matrix deosn't have {i} row!")

        else:
            return matrix[i - 1::col]

    @staticmethod
    def is_zero_matrix(matrix):
        if not all(matrix):
            return True
        return False

    @staticmethod
    def is_unit_matrix(matrix, row, col):
        if not isinstance(row, int) or not isinstance(col, int):
            return TypeError
        if row == col:
            count = -1
            if matrix[0] == 1:
                for i in range(row * col):
                    count += 1
                    if count == row + 1:
                        if matrix[i] == 1:
                            count = 0
                        else:
                            return False
                    else:
                        if i != 0:
                            if matrix[i] != 0:
                                return False
                return True
            else:
                return False
        else:
            return False


    @staticmethod
    def is_top_triangle_matrix(matrix, row, col):
        start_point = col            
        if matrix[start_point] == 0:
            for i in range(row - 1):
                start_point += col
                for j in range(i):
                    if matrix[start_point + j] != 0:
                        return False
        return True


    @staticmethod
    def is_bottom_triangle_matrix(matrix, row, col):
        start_point = 1
        if matrix[start_point] == 0:
            for i in range(row - 1):
                start_point += col + 1
                for j in range(row - 1,0, -1):
                    if matrix[start_point + j] != 0:
                        return False

        return False


    @classmethod
    def make_matrix_from_string(cls, elements):
        rows_element = elements.split(',')
        cols_element = rows_element.split(' ')
        element_list = []

        for element in elements:
            irreal = 0
            real = 0
            if 'i' in element:
                if cols_element.index('i') - 1 > 0:
                    irreal = cols_element[cols_element.index('i') - 1]
                else:
                    irreal = 1

                if '+' in element:
                    real = cols_element[cols_element.index('+') + 1]
                
                Complex(real, irreal)
            else:
                element_list.append(Integer(element))


        return cls(element_list)
    

    def __mul__(self, other):
        result_matrix = []
        
        if type(other) is Integer:
            for row_matrix in self.matrix:
                for element in row_matrix:
                    if type(element) is Complex:
                        result_matrix.append(Complex(element.real * other._num, element.complex * other._num))
                    elif type(element) is Integer:
                        result_matrix.append(Integer(element.num * other._num))
            return result_matrix


        elif type(other) is Complex:
            for row_matrix in self.matrix:
                for element in row_matrix:
                    if type(element) is Complex:
                        result_matrix.append(Complex((element.real * other.real) - (other.complex * element.complex), (element.complex * other.real) + (element.complex * other.complex)))
                    elif type(element) is Integer:
                        result_matrix.append(Complex(other.real * element._num, other.complex * element._num))
            return result_matrix

        elif type(other) is Matrix:
            if self.col == other.row and self.row == other.col:
                for i in range(1, self.row + 1):
                    value = Complex(0,0)
                    row_first_matrix = Matrix.get_ith_row(self.matrix, self.row, self.col, i)
                    for j in range(1, other.col + 1):
                        col_second_matrix = Matrix.get_ith_col(other.matrix, other.row, other.col, j)
                        for i in range(len(col_second_matrix)):
                            value = row_first_matrix[i] * col_second_matrix[i] + value

                        result_matrix.append(value)
                return result_matrix
            else:
                raise ValueError("you can't multiply these two matrixes.")

        else:
            raise TypeError


    def __add__(self, other):
        result_matrix = []
        first_matrix = matrixUnpack(self.matrix)

        if type(other) is Matrix:
            second_matrix = matrixUnpack(other.matrix)
            if self.row == other.row and self.col == other.col:
                for (element1, element2) in zip(first_matrix, second_matrix):
                    result_matrix.append(element1 + element2)
                return matrixPack(result_matrix, self.row, self.col)

            return ValueError('these two matrix cannot add two each other.')
        
        elif type(other) is Integer:
            for component in first_matrix:
                if type(component) is Integer:
                    result_matrix.append(Integer(component.num + other.num))
                elif type(component) is Complex:
                    result_matrix.append(Complex(component.real + other.num, component.complex))
            return matrixPack(result_matrix, self.row, self.col)

        elif type(other) is Complex:
            for component in first_matrix:
                if type(component) is Integer:
                    result_matrix.append(Complex(other.real + component.num, other.complex))
                elif type(component) is Complex:
                    result_matrix.append(Complex(other.real + component.real, other.complex + component.complex))
            return matrixPack(result_matrix, self.row, self.col)


# ------------------- packing matrix accoriding to row and column  -------------------
def matrixPack(li, row, col):
    finall_matrix = []
    for i in range(row):
        finall_matrix.append(li[i * col: i * col + col])
    return finall_matrix

# ------------------- create a one dimention list of component in matrix  -------------------
def matrixUnpack(li):
    finall_matrix = []

    for i in li:
        for j in i:
            finall_matrix.append(j)
    return finall_matrix

# ------------------- running test function --------------------------------
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


# ------------------- testing ... -------------------------
class Test(unittest.TestCase):
    def test_Class_matrix_1(self):
        a = Complex(12,23)
        self.assertEqual(a.real, 12)
        self.assertEqual(a.complex, 23)

    def test_matrix_2(self):
        real = 'hello'
        Imaginary = 12
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)

    def test_matrix_3(self):
        real = ' '
        Imaginary = 12
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)   

    def test_complex_4(self):
        real = ''
        Imaginary = 12
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)     


    def test_complex_5(self):
        real = None
        Imaginary = 12
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)

    def test_complex_6(self):
        real = 2
        Imaginary = '12'
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)

    def test_complex_7(self):
        real = 2
        Imaginary = ' '
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)

    def test_complex_8(self):
        real = 2
        Imaginary = None
        with self.assertRaises(TypeError):
            a = Complex(real, Imaginary)


    def test_Integer_1(self):
        value = 12
        a = Integer(value)
        self.assertEqual(a.num, 12)

    def test_Integer_2(self):
        value = ' '

        with self.assertRaises(TypeError):
            a = Integer(value)

    def test_Integer_3(self):
        value = None

        with self.assertRaises(TypeError):
            a = Integer(value)    

    def test_Integer_4(self):
        value = 'asdfasdf'

        with self.assertRaises(TypeError):
            a = Integer(value)

    def test_integer_5(self):
        value = [1,2]
        with self.assertRaises(TypeError):
            a = Integer(value)

    def test_matrix_1(self):
        pass

    def test_matrix_2(self):
        my_matrix = [Complex(0,2), Complex(1,2), Complex(2,3),
                        Integer(2), Integer(3), Complex(5,6),
                        Complex(2,0), Integer(9), Integer(0)]

        second_row = Matrix.get_ith_row(my_matrix, 3,3,2)
        self.assertEqual(second_row, [Integer(2), Integer(3), Complex(5,6)])

    def test_matrix_3(self):
        my_matrix = [Complex(0,2), Complex(1,2), Complex(2,3),
                        Integer(2), Integer(3), Complex(5,6),
                        Complex(2,0), Integer(9), Integer(0)]

        second_column = Matrix.get_ith_col(my_matrix,3,3,2)

        self.assertEqual(second_column, [Complex(1,2), Integer(3), Integer(9)])

    def test_matrix_4(self):
        my_matrix = Matrix.make_unit_matrix(2)
        
        self.assertEqual(my_matrix, [[1,0],[0,1]])

    def test_matrix_5(self):
        my_matrix = [0,0,0,0]
        is_zero = Matrix.is_zero_matrix(my_matrix)

        self.assertEqual(is_zero, True)

    def test_matrix_6(self):
        my_matrix = [1,0,0,3,3,0,1,-2,0]
        is_top_triangle = Matrix.is_top_triangle_matrix(my_matrix, 3,3)

    
    def test_matrix_7(self):
        my_matrix = [1,0,0,0,1,0,0,0,1]
        is_unit = Matrix.is_unit_matrix(my_matrix,3,3)

        self.assertEqual(is_unit, True)

    def test_matrix_8(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        my_integer = Integer(1)
        result = my_matrix + my_integer
        self.assertEqual(result, [[Complex(2,2), Integer(4)], [Integer(3), Complex(3,3)]])

    def test_matrix_9(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        my_complex = Complex(1,1)    
        result = my_matrix + my_complex

        self.assertEqual(result, [[Complex(2,3), Complex(4,1)], [Complex(3,1), Complex(3,4)]])

    def test_matrix_10(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        second_matrix = Matrix(2,2,Complex(1,3), Integer(4), Complex(0,1), Integer(1))

        result_matrix = my_matrix + second_matrix

        self.assertEqual(result_matrix,[[Complex(2,5), Integer(7)], [Complex(2,1), Complex(3,3)]])

    def test_mul_matrix_1(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        my_integer = Integer(2)

        result_matrix = my_matrix * my_integer

        self.assertEqual(result_matrix, [Complex(2,4), Integer(6), Integer(4), Complex(4,6)])

    def test_mul_matrix_2(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3))
        my_complex = Complex(2,2)

        result_matrix  = my_matrix * my_complex

        #!-----------------------

    def test_mul_matrix_3(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        second_matrix = Matrix(2,2,Complex(1,3), Integer(4), Complex(0,1), Integer(1))

        result_matrix = my_matrix * second_matrix

        
    def test_add_integer_1(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        my_integer = Integer(1)
        result = my_integer + my_matrix
        self.assertEqual(result, [[Complex(2,2), Integer(4)], [Integer(3), Complex(3,3)]])

    def test_add_integer_2(self):
        first_integer = Integer(3)       
        second_integer = Integer(4)
        result = first_integer + second_integer

        self.assertEqual(result, Integer(7))

    def test_add_integer_3(self):
        my_integer = Integer(2)
        my_complex = Complex(1,2)
        result = my_integer + my_complex

        self.assertEqual(result, Complex(3,2))

    def test_mul_integer_1(self):
        my_matrix = Matrix(2,2,Complex(1,2), Integer(3), Integer(2), Complex(2,3)) 
        my_integer = Integer(2)

        result_matrix = my_integer * my_matrix

        self.assertEqual(result_matrix, [Complex(2,4), Integer(6), Integer(4), Complex(4,6)])

    def test_mul_integer_2(self):
        my_integer = Integer(2)
        my_complex = Complex(1,2)
        result = my_integer * my_complex

        self.assertEqual(result, Complex(2,4))       


run_tests(Test)
