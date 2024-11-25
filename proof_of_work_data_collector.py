import hashlib
import time
import argparse

def proof_of_work(difficulty):
    prefix = '0' * difficulty
    nonce = 0
    while True:
        text = f"i am a fuck up {nonce}"
        hash_result = hashlib.sha256(text.encode()).hexdigest()
        if hash_result.startswith(prefix):
            return nonce, hash_result
        nonce += 1

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("difficulty", type=int)
    args = parser.parse_args()

    difficulty = args.difficulty

    start_time = time.time()
    nonce, hash_result = proof_of_work(difficulty)
    elapsed_time = time.time() - start_time

    print(f"Difficulty Level: {difficulty}")
    print(f"Nonce: {nonce}")
    print(f"Hash: {hash_result}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
