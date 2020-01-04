# Why the numpy implementation is faster

Firstly, numpy arrays are much more efficient than native python lists. This is as numpy arrays are optimised to contain information of the same type (which are packed close together) while python lists store pointers to objects, which allows for greater flexiblity but is less efficient. This allows for performance improvements through the use of techniques such as caching due to locality of reference. Furthermore, numpy operations are frequently implemented in C, which has significantly faster loops than python.

Additionally, the implementation in python uses the trivial O(N^3) algorithm for matrix multiplication although there exists faster algorithms for matrix multiplication, especially for special cases such as multiplication of square matrices. In contrast, numpy uses highly optimised implementations of those faster algorithms, i.e. BLAS method for matrix multiplcation.
