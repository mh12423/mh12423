#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 10:03:56 2024

@author: Programming
"""
import math
from sympy import randprime
import random
    
class Encrypt:
    def __init__(self, message):
        self.message = message
        self.keys = self.generate()
    
    def generate(self):
        def sum_lengths(m):
            l = 0
            for i in range(m):
                l += 25*(26**i)
            return l
        def generate_coprime(n):
            candidate = random.randint(2, m)
            while True:
                if math.gcd(n, candidate) == 1:
                    return candidate
                else:
                    candidate = random.randint(2, m)
        
        max_num = sum_lengths(len(self.message))
        p = randprime(1, max_num)
        q = randprime(1, max_num)
        m = (p-1)*(q-1)
        while p == q:
            q = randprime(1, max_num)
        N = p*q
        e = generate_coprime(m)
        return [N, e, p, q]
    
    def encrypt(self):
        numbers = [(ord(char.lower()) - ord('a') +1 ) for char in self.message]
        def generate_number(numbers):
            m = 0
            for i in range(len(numbers)):
                m += numbers[i]*(26**i)
            return m
        N = self.keys[0]
        e = self.keys[1]
        p = self.keys[2]
        q = self.keys[3]
        m = generate_number(numbers)
        c = pow(m, e, N)
        print('The message converted into numbers is', m) 
        print('N is', N)
        print('p is', p)
        print('q is', q)
        print('e is', e)
        print('The encoded message is', c)
        return c
    
class Decrypt:
    def __init__(self, p, q, e, encoded_message):
        self.p = p
        self.q = q
        self.e = e
        self.encoded_message = encoded_message
        self.keys = self.generate()
        
    def generate(self):
        d = pow(self.e, -1, int((self.p-1)*(self.q-1)))
        return d
        
    def decrypt(self):
        N = self.p*self.q
        decoded_number = pow(self.encoded_message, self.keys, N)
        def generate_letters(c):
            letters_powers = []
            next_step = c
            while next_step != 0:
                remainder = int(next_step%26)
                next_step = int(math.floor(next_step/26))
                if remainder == 0:
                    remainder = 26
                    next_step -= 1
                letters_powers.append(remainder)
            letters = ''.join([chr(num + 96) for num in letters_powers])
            return letters
        letters = generate_letters(decoded_number)
        print('d is', self.keys)
        print('The decoded number is', decoded_number)
        print('The decoded message is', letters)
        return letters

initial_values = Encrypt('')
initial_values.encrypt()
initial_values2 = Decrypt(, , , )
initial_values2.decrypt()
