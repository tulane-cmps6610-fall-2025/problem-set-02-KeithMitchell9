"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    # Base cases
    if x.decimal_val == 0 or y.decimal_val == 0:
        return BinaryNumber(0)
    if x.decimal_val == 1:
        return y
    if y.decimal_val == 1:
        return x
    
    # Pad the binary vectors to same length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    
    # If single bit, return product
    if len(x_vec) == 1:
        return BinaryNumber(int(x_vec[0]) * int(y_vec[0]))
    
    # Split into left and right halves
    x_left, x_right = split_number(x_vec)
    y_left, y_right = split_number(y_vec)
    
    # Compute four products
    n = len(x_vec) // 2
    
    # x_left * y_left * 2^(2n) + x_left * y_right * 2^n + x_right * y_left * 2^n + x_right * y_right
    term1 = bit_shift(quadratic_multiply(x_left, y_left), 2 * n)
    term2 = bit_shift(quadratic_multiply(x_left, y_right), n)
    term3 = bit_shift(quadratic_multiply(x_right, y_left), n)
    term4 = quadratic_multiply(x_right, y_right)
    
    # Add all terms
    result = BinaryNumber(term1.decimal_val + term2.decimal_val + term3.decimal_val + term4.decimal_val)
    return result


def subquadratic_multiply(x, y):
    # Base cases
    if x.decimal_val == 0 or y.decimal_val == 0:
        return BinaryNumber(0)
    if x.decimal_val == 1:
        return y
    if y.decimal_val == 1:
        return x
    
    # Pad the binary vectors to same length
    x_vec, y_vec = pad(x.binary_vec, y.binary_vec)
    
    # If single bit, return product
    if len(x_vec) == 1:
        return BinaryNumber(int(x_vec[0]) * int(y_vec[0]))
    
    # Split into left and right halves
    x_left, x_right = split_number(x_vec)
    y_left, y_right = split_number(y_vec)
    
    n = len(x_vec) // 2
    
    z0 = subquadratic_multiply(x_right, y_right)
    z2 = subquadratic_multiply(x_left, y_left)
    
    # Compute sums for the middle term
    x_sum = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    y_sum = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
    z1 = subquadratic_multiply(x_sum, y_sum)
    
    # Compute final result: z2 * 2^(2n) + (z1 - z2 - z0) * 2^n + z0
    term1 = bit_shift(z2, 2 * n)
    middle_term = BinaryNumber(z1.decimal_val - z2.decimal_val - z0.decimal_val)
    term2 = bit_shift(middle_term, n)
    
    result = BinaryNumber(term1.decimal_val + term2.decimal_val + z0.decimal_val)
    return result

## Feel free to add your own tests here.
def test_multiply():
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))) == 2*2

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
## Testing
if __name__ == "__main__":
    test_multiply()
    
    # Run timing comparison
    print("\nRunning timing comparison...")
    compare_multiply()