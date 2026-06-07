# Determinant Value Finder

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Repository](https://img.shields.io/badge/repo-active-brightgreen.svg)](https://github.com/TROJAN1HAMMER/determinant-value-finder)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#license)

---

## Overview

**Determinant Value Finder** is a mathematical computation tool designed to calculate determinants for square matrices of orders 2×2 and 3×3. The application provides an interactive command-line interface that enables users to input matrix elements, compute determinant values, and derive related matrix properties including adjoints and inverses.

This project demonstrates core principles of computational mathematics, algorithm design, and user-centric interface development suitable for educational, academic, and professional mathematical applications.

### Business Value
- **Educational Purpose**: Serves as an excellent learning tool for linear algebra students and professionals
- **Mathematical Accuracy**: Eliminates manual calculation errors inherent in hand-computed determinants
- **Extended Computations**: Beyond determinant calculation, provides adjoint and inverse matrix computations
- **User Verification**: Implements input validation and correction mechanisms to ensure data accuracy

---

## Features

### Core Functionality
- ✅ **2×2 Matrix Determinant Calculation**
  - Supports determinant computation using the formula: `det = (p×s) - (q×r)`
  - Calculates determinant squared (matrix multiplication result)
  - Computes adjoint matrix
  - Derives inverse matrix with precision handling

- ✅ **3×3 Matrix Determinant Calculation**
  - Implements cofactor expansion along the first row
  - Handles multi-step sub-determinant calculations
  - Supports complex matrix operations

### User Experience Features
- 🔄 **Interactive Input Validation**: Users can review and correct matrix values before computation
- 📊 **Clear Matrix Display**: Visual representation of matrix structure and results
- 🎯 **Recursive Error Handling**: Allows users to restart calculations without program termination
- ✨ **Formatted Output**: Well-organized presentation of results and auxiliary computations

---

## Tech Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Language** | Python 3.x | Cross-platform compatibility, rapid prototyping, mathematical libraries support |
| **Interface** | CLI (Command-Line) | Lightweight, platform-independent, suitable for mathematical workflows |
| **Architecture** | Functional Programming | Recursive functions for iterative computations and user feedback loops |
| **Input Handling** | stdin/input() | Direct user engagement, real-time validation capabilities |

---

## Architecture

### Design Patterns

#### 1. **Recursive Function Pattern**
```
User Input → Validation → Computation → Result Display
                  ↑                           ↓
                  └─── Correction Loop ───────┘
```
The application uses recursion to handle user corrections without requiring external state management.

#### 2. **Conditional Branching Architecture**
The program implements a tree-based decision structure:
- **Root Decision**: Matrix order selection (2×2 or 3×3)
- **Processing Branch**: Order-specific calculation algorithms
- **Validation Branch**: Input verification and correction mechanisms

#### 3. **Separation of Concerns**
- **Input Layer**: User input collection and normalization (`lower()` for case-insensitive input)
- **Computation Layer**: Mathematical operations (determinant, adjoint, inverse calculations)
- **Output Layer**: Result formatting and presentation

### Computational Algorithm

#### 2×2 Determinant Algorithm
```
For matrix [[p, q], [r, s]]:
  determinant = (p × s) - (q × r)
  
Extended operations:
  - determinant² = matrix multiplication
  - adjoint = [[s, -q], [-r, p]]
  - inverse = adjoint / determinant
```

#### 3×3 Determinant Algorithm (Cofactor Expansion)
```
For matrix [[a, b, c], [d, e, f], [g, h, i]]:
  minor_a = (e × i) - (h × f)
  minor_b = (d × i) - (g × f)
  minor_c = (d × h) - (g × e)
  
  determinant = a×minor_a - b×minor_b + c×minor_c
```

---

## Folder Structure

```
determinant-value-finder/
│
└── main.py                 # Primary application module
    ├── Initialization      # Welcome and order selection
    ├── 2×2 Matrix Handler  # Second-order determinant computation
    ├── 3×3 Matrix Handler  # Third-order determinant computation
    └── Termination         # Thank you message
```

### File Specifications
- **main.py** (3,186 bytes)
  - Single-entry point application
  - Modular function definitions for each matrix order
  - Approximately 112 lines of code with comprehensive logic

---

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- Terminal/Command Prompt access

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TROJAN1HAMMER/determinant-value-finder.git
   cd determinant-value-finder
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # Expected output: Python 3.x.x or higher
   ```

3. **No External Dependencies**
   This project utilizes only Python's built-in libraries, so no additional installations are required.

---

## Usage

### Running the Application

```bash
python main.py
```

### Interactive Workflow

#### Example: 2×2 Matrix Determinant

```
Hello!
Welcome to determinant .py calculator
For which order determinant, do you want to find the determinant value
Is it 2*2? yes

Since it is a 2 * 2 matrices...
! p q !
! r s !
What is the value of p: 1
What is the value of q: 2
What is the value of r: 3
What is the value of s: 4

Given matrices is:
! 1 2 !
! 3 4 !
Is there any corrections? no

The value of the given determinant is: -2
determinant squared is:
! 7 10 !
! 15 22 !
The adjoint of the given matrices is: 
! -4 2 !
! 1 3 -1 !
The inverse of the given matrices is: 
! 2.0 -1.0 !
! -1.5 0.5 !
Thank you for using determinant .py calculator.
```

#### Example: 3×3 Matrix Determinant

```
Is it 2*2? no
Then since it is a 3 * 3 matrices..
! a b c !
! d e f !
! g h i !
What is the value of a: 1
What is the value of b: 2
What is the value of c: 3
... (additional input prompts) ...

Given matrices is: 
! 1 2 3 !
! 0 1 4 !
! 5 1 3 !

Is there any correction? no
The value of the give determinant is: 1
Thank you for using determinant .py calculator.
```

### Input Parameters

| Matrix Size | Input Parameters | Formula | Example |
|-------------|-----------------|---------|---------|
| 2×2 | p, q, r, s | det = ps - qr | -2 |
| 3×3 | a-i (9 values) | Cofactor expansion | Variable |

---

## Challenges Solved

### 1. **User Input Validation**
**Challenge**: Ensuring data accuracy in manual matrix entry  
**Solution**: Implemented input review mechanism allowing users to correct values before computation

### 2. **Numerical Precision**
**Challenge**: Handling floating-point arithmetic for inverse matrix calculations  
**Solution**: Direct division operations maintain precision for most practical applications

### 3. **Algorithm Correctness**
**Challenge**: Implementing accurate determinant calculations for different matrix orders  
**Solution**: Utilized well-established mathematical formulas (Sarrus' rule for 3×3, direct formula for 2×2)

### 4. **User Experience**
**Challenge**: Making mathematical computation accessible to non-technical users  
**Solution**: Intuitive prompts, clear matrix visualization, and recursive correction loops

### 5. **Code Organization**
**Challenge**: Managing logic for multiple matrix orders within a monolithic script  
**Solution**: Modular function definitions with order-specific handling

---

## Future Improvements

### Planned Enhancements

1. **Expanded Matrix Support**
   - [ ] Support for n×n matrices using Gaussian elimination
   - [ ] LU decomposition for computational efficiency
   - [ ] Support for complex numbers

2. **Performance Optimization**
   - [ ] Implement NumPy for vectorized operations
   - [ ] Caching mechanisms for repeated calculations
   - [ ] Algorithm optimization for large matrices

3. **Extended Functionality**
   - [ ] Eigenvalue and eigenvector computation
   - [ ] Matrix decomposition methods (QR, SVD)
   - [ ] Rank and nullspace calculations

4. **User Interface Enhancement**
   - [ ] GUI implementation (Tkinter/PyQt)
   - [ ] Graphical matrix visualization
   - [ ] Export results to CSV/PDF formats

5. **Code Quality**
   - [ ] Comprehensive unit testing suite
   - [ ] Type hints and documentation strings
   - [ ] Error handling and exception management
   - [ ] Input sanitization and validation

6. **Professional Features**
   - [ ] Batch processing for multiple matrices
   - [ ] Configuration files for advanced users
   - [ ] Logging and computation history tracking

---

## Author

**Developed by:**
- **TROJAN1HAMMER/Harshith B** - Primary Developer

### Contact & Contributions
For inquiries, contributions, or feature requests, please open an issue on the [GitHub repository](https://github.com/TROJAN1HAMMER/determinant-value-finder).

---

## License

This project is open-source and available under the [MIT License](LICENSE).

### Terms
- ✅ Free to use, modify, and distribute
- ✅ Suitable for educational and commercial purposes
- ✅ Requires attribution to original authors

---

## Acknowledgments

This project demonstrates fundamental principles in:
- **Linear Algebra**: Determinant theory and matrix properties
- **Software Engineering**: Algorithm design and user interface patterns
- **Python Development**: Functional programming and interactive application development

---

## Getting Help

### FAQ

**Q: What happens if I enter non-integer values?**  
A: The program expects integer inputs. Non-integer values will cause a runtime error. Future versions should implement input sanitization.

**Q: Can I compute determinants for matrices larger than 3×3?**  
A: Currently, the application supports only 2×2 and 3×3 matrices. See [Future Improvements](#future-improvements) for planned expansion.

**Q: How is the inverse matrix calculated?**  
A: For 2×2 matrices: `Inverse = Adjoint / Determinant`. Ensure the determinant is non-zero.

---

**Last Updated**: 2022  
**Repository**: [TROJAN1HAMMER/determinant-value-finder](https://github.com/TROJAN1HAMMER/determinant-value-finder)  
**Status**: Active & Maintained
