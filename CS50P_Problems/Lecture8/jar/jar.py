"""
Define a class that represents a jar of cookies.
"""

class Jar:
    # Constructor
    def __init__(self, capacity=12, n_cookies=0):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._n_cookies = n_cookies

    # str method
    def __str__(self):
        return "🍪" * self._n_cookies

    # put n cookies in the jar
    def deposit(self, n):
        new_n_cookies = self._n_cookies + n
        if new_n_cookies > self._capacity:
            raise ValueError
        else:
            self._n_cookies = new_n_cookies

    # get n cookies from the jar
    def withdraw(self, n):
        if n > self._n_cookies:
            raise ValueError
        self._n_cookies -= n

    # getter for capacity property
    @property
    def capacity(self):
        return self._capacity

    # getter for n_cookies property
    @property
    def size(self):
        return self._n_cookies

    # setter for capacity property
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    # setter for n_cookie property
    @size.setter
    def n_cookies(self, n_cookies):
        self._n_cookies = n_cookies