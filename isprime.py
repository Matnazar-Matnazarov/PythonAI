# isprime list range n optimize prime and composite numbers
from typing import List
from time import time
from unittest import TestCase, FunctionTestCase
import numpy as np
from math import isqrt


def isprime(n: int) -> List[int]:
    """
    Ultra-tezkor tub sonlar generatori.
    n gacha bo'lgan tub sonlar ro'yxatini qaytaradi.
    """
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]

    # NumPy array ishlatish
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0] = sieve[1] = False
    
    # Juft sonlarni bir yo'la belgilash
    sieve[4::2] = False
    
    # Optimallashtirilgan sqrt(n) gacha tekshirish
    for i in range(3, isqrt(n) + 1, 2):
        if sieve[i]:
            sieve[i*i::i] = False
    
    # int tipidagi natijani qaytarish
    return [i for i in range(2, n + 1) if sieve[i]]


def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Ultra-tezkor Eratosfen g'alviri.
    n gacha bo'lgan tub sonlar ro'yxatini qaytaradi.
    """
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]

    # NumPy array ishlatish
    sieve = np.ones(n + 1, dtype=bool)
    sieve[0] = sieve[1] = False
    
    # Juft sonlarni bir yo'la belgilash
    sieve[4::2] = False
    
    # Optimallashtirilgan sqrt(n) gacha tekshirish
    for i in range(3, isqrt(n) + 1, 2):
        if sieve[i]:
            sieve[i*i::i] = False
    
    # int tipidagi natijani qaytarish
    return [i for i in range(2, n + 1) if sieve[i]]


def segmented_sieve(n: int) -> List[int]:
    """
    Ultra-tezkor segmentli g'alvir.
    n gacha bo'lgan tub sonlar ro'yxatini qaytaradi.
    """
    if n < 2:
        return []
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    
    # Dastlabki tub sonlarni topish
    limit = isqrt(n)
    base_primes = sieve_of_eratosthenes(limit)
    
    # Natijalar uchun ro'yxat
    primes = []
    
    # Birinchi segmentni alohida ko'rib chiqish
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[0] = sieve[1] = False
    
    for prime in base_primes:
        sieve[prime*prime::prime] = False
    
    primes.extend(i for i in range(2, limit + 1) if sieve[i])
    
    # Qolgan segmentlar
    segment_size = limit
    
    for low in range(limit + 1, n + 1, segment_size):
        high = min(low + segment_size - 1, n)
        length = high - low + 1
        
        sieve = np.ones(length, dtype=bool)
        
        for prime in base_primes:
            start = (low + prime - 1) // prime * prime
            if start > high:
                continue
            
            start = max(start, prime * prime)
            sieve[(start-low)::prime] = False
        
        primes.extend(int(i + low) for i in range(length) if sieve[i])
    
    return primes


