from isprime import isprime, sieve_of_eratosthenes, segmented_sieve
import unittest
from time import time

class TestPrimeFunctions(unittest.TestCase):
    def setUp(self):
        """Test ma'lumotlarini tayyorlash"""
        # Kichik sonlar uchun test hollari (aniq natijalar)
        self.small_cases = {
            2: [2],
            3: [2, 3],
            5: [2, 3, 5],
            10: [2, 3, 5, 7],
            15: [2, 3, 5, 7, 11, 13],
            20: [2, 3, 5, 7, 11, 13, 17, 19],
            30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
            50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
            100: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        }
        
        # O'rta sonlar uchun test hollari (tub sonlar soni)
        self.medium_cases = {
            200: 46,     # 200 gacha 46 ta tub son
            500: 95,     # 500 gacha 95 ta tub son
            1000: 168,   # 1000 gacha 168 ta tub son
            2000: 303,   # 2000 gacha 303 ta tub son
            5000: 669    # 5000 gacha 669 ta tub son
        }
        
        # Chegaraviy holatlar
        self.edge_cases = [-1000, -100, -10, -1, 0, 1]
        
        # Ma'lum tub sonlar
        self.known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        
        # Murakkab sonlar
        self.composite_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25]

    def test_small_numbers(self):
        """Kichik sonlar uchun aniq natijalarni tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for method in methods:
            for n, expected in self.small_cases.items():
                with self.subTest(method=method.__name__, n=n):
                    result = method(n)
                    self.assertEqual(result, expected)
                    self.assertTrue(all(isinstance(x, int) for x in result))
                    self.assertTrue(all(x > 0 for x in result))
                    self.assertEqual(result, sorted(result))

    def test_medium_numbers(self):
        """O'rta sonlar uchun tub sonlar sonini tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for method in methods:
            for n, expected_count in self.medium_cases.items():
                with self.subTest(method=method.__name__, n=n):
                    result = method(n)
                    self.assertEqual(len(result), expected_count)
                    self.assertTrue(all(result[i] < result[i+1] for i in range(len(result)-1)))

    def test_edge_cases(self):
        """Chegaraviy holatlarni tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for method in methods:
            for n in self.edge_cases:
                with self.subTest(method=method.__name__, n=n):
                    result = method(n)
                    self.assertEqual(result, [])

    def test_consecutive_numbers(self):
        """Ketma-ket sonlar uchun test"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for method in methods:
            for i in range(2, 30):
                with self.subTest(method=method.__name__, n=i):
                    result1 = method(i)
                    result2 = method(i + 1)
                    self.assertTrue(len(result2) >= len(result1))
                    self.assertTrue(all(x in result2 for x in result1))

    def test_known_primes(self):
        """Ma'lum tub sonlarni tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for method in methods:
            for prime in self.known_primes:
                with self.subTest(method=method.__name__, prime=prime):
                    result = method(prime)
                    self.assertIn(prime, result)

    def test_composite_numbers(self):
        """Murakkab sonlarni tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for method in methods:
            for n in self.composite_numbers:
                with self.subTest(method=method.__name__, n=n):
                    result = method(n)
                    self.assertNotIn(n, result)

    def test_method_consistency(self):
        """Barcha metodlar bir xil natija qaytarishini tekshirish"""
        test_numbers = [100, 200, 500, 1000]
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        
        for n in test_numbers:
            results = [method(n) for method in methods]
            for i in range(1, len(results)):
                with self.subTest(n=n, method_index=i):
                    self.assertEqual(results[0], results[i])

    def test_result_properties(self):
        """Natijalarning umumiy xususiyatlarini tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        test_numbers = [50, 100, 200]
        
        for method in methods:
            for n in test_numbers:
                result = method(n)
                with self.subTest(method=method.__name__, n=n):
                    # Barcha elementlar butun son
                    self.assertTrue(all(isinstance(x, int) for x in result))
                    # Barcha elementlar musbat
                    self.assertTrue(all(x > 0 for x in result))
                    # O'sish tartibida joylashgan
                    self.assertEqual(result, sorted(result))
                    # Takrorlanishlar yo'q
                    self.assertEqual(len(result), len(set(result)))
                    # Har bir element n dan kichik yoki teng
                    self.assertTrue(all(x <= n for x in result))

    def test_performance(self):
        """Metodlarning ishlash tezligini tekshirish"""
        test_sizes = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8]
        methods = [
            ('isprime', isprime),
            ('sieve_of_eratosthenes', sieve_of_eratosthenes),
            ('segmented_sieve', segmented_sieve)
        ]
        
        for n in test_sizes:
            print(f"\nPerformance test for n={n}:")
            results = {}
            
            for name, method in methods:
                start = time()
                result = method(n)
                elapsed = time() - start
                results[name] = (result, elapsed)
                print(f"{name}: {elapsed:.4f} seconds")
                
            # Natijalar bir xilligini tekshirish
            base_result = results[methods[0][0]][0]
            for name, (result, _) in results.items():
                with self.subTest(n=n, method=name):
                    self.assertEqual(result, base_result)

    def test_incremental_consistency(self):
        """Har bir keyingi natija oldingi natijani o'z ichiga olishini tekshirish"""
        methods = [isprime, sieve_of_eratosthenes, segmented_sieve]
        test_ranges = [(10, 20), (20, 50), (50, 100)]
        
        for method in methods:
            for start, end in test_ranges:
                with self.subTest(method=method.__name__, range=(start,end)):
                    result_start = method(start)
                    result_end = method(end)
                    self.assertTrue(all(x in result_end for x in result_start))

if __name__ == '__main__':
    unittest.main(verbosity=2)