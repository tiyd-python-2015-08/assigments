# Vector and Matrix Math

## Description

Implement various vector and matrix math functions using no math libraries.

## Tasks

```markdown
* [ ] Blank slate
  * [ ] Create a GitHub repo called `vector-victor`
  * [ ] Put a `README.md` file in it and copy linear_algebra.py and test_linear_algebra.py into it from this repository
* [ ] Normal Mode (make sure you pass the tests for each of these functions)
  * [ ] shape (for vectors)
  * [ ] vector_add
  * [ ] vector_sub
  * [ ] vector_sum
  * [ ] dot
  * [ ] vector_multiply
  * [ ] vector_mean
  * [ ] magnitude
* [ ] Hard Mode (make sure you pass the tests for each of these functions)
  * [ ] shape (for vectors + matrices)
  * [ ] matrix_row
  * [ ] matrix_col
  * [ ] matrix_scalar_multiply
  * [ ] matrix_vector_multiply
  * [ ] matrix_matrix_multiply

```

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* List comprehensions
* Introductory linear algebra concepts

### Performance Objectives

After completing this assignment, you should be able to:

* Perform mathematical operations on complex list structures

## Details

### Deliverables

* A Git repo called vectors-victor containing at least:
  * `README.md` file explaining how to run your project
  * a module called `linear_algebra`
  * tests for `linear_algebra`

### Requirements

* Passing unit tests
* No use of third-party libraries - only built in `+ - / *` operators and the `math` module
* **No use of `for` or `while` loops**

## Normal Mode

Implement these linear algebra functions:

* vector addition and subtraction
* vector multiplication by a scalar
* mean of multiple vectors
* dot product
* magnitude

## Hard Mode

Implement these additional linear algebra functions:

* matrix addition and subtraction
* matrix multiplication by a scalar
* matrix multiplication by a vector
* matrix multiplication by a matrix

These functions are all defined in [the formulas notebook](Formulas.ipynb) included with this assignment as well as the [tests](test_linear_algebra.py).

These functions must:

* Check the shape of the incoming vector or matrix before any calculations
* Reuse any duplicated code

## Reading

* [List Comprehension documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [How to Use List Comprehensions By Example](http://howchoo.com/g/ngi2zddjzdf/how-to-use-list-comprehension-in-python)
* [Math Insight: Vector Algebra](http://mathinsight.org/thread/vector_algebra#matrices)
* [Khan Academy on Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
