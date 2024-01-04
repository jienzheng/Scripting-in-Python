# Scripting in Python

Using python script (wrapper.py) to manipulate mickey.png image

## Description

Using Python to integrate all the codes written in C, Haskell, Prolog, and MATLAB to leverage the image processing capabilities of MATLAB.

### Notes

* Only MacOS can run this code because Windows machine are not able to accept such a large file unless you change the dimensions.
* For Window in MATLAB, change the dimension size to be 50-75 pixels by 50-75 pixels. This image will be smaller, but able to run this code fine. This will be the easiest method.
* A harder work around would be changing the python code to accept the bits row by row instead of all the bits at once.

## Getting Started

### Dependencies

* MacOS
* gcc compiler
* glasgow haskell compiler
* swi prolog
* python 3+
* MATLAB R2023b

### Installing
* Download provided code
* Install required dependencies
* Make sure dependencies are installed properly by running:
  ```
  gcc --version
  ghc --version
  swipl --version
  python --version
  matlab
  ```

### Executing program using cmd

* In cmd, navigate to the directory where the code is installed:
```
python3 wrapper.py
```

## Contact

Jien Zheng

Project Link: [https://github.com/jienzheng/Scripting-in-Python](https://github.com/jienzheng/Scripting-in-Python)

San Diego State University Computer Science

## Acknowledgements

* [StackOverFlow](https://stackoverflow.com/)

