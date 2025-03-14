import time
# These tests simulate tasks that take time (e.g., waiting for network responses, I/O operations).
# They are designed to demonstrate the difference between sequential, parallel, and concurrent execution.

def test_result_1_completes_as_expected():
    time.sleep(2)
    print("Result 1 has completed!")


def test_result_2_completes_as_expected():
    time.sleep(3)
    print("Result 2 has completed!")


def test_result_3_completes_as_expected():
    time.sleep(5)
    print("Result 3 has completed!")


def test_result_4_completes_as_expected():
    time.sleep(5)
    print("Result 4 has completed!")


def test_result_5_completes_as_expected():
    time.sleep(3)
    print("Result 5 has completed!")


def test_result_6_completes_as_expected():
    time.sleep(2)
    print("Result 6 has completed!")


def test_result_7_completes_as_expected():
    time.sleep(5)
    print("Result 7 has completed!")

# Key Concepts:
#
# 1. Sequential Execution (Default pytest behavior):
#    - Tests run one after another.
#    - Total execution time is the sum of individual test times.
#    - In this case, it would take approximately 25 seconds.
#
# 2. Parallel Execution (using pytest-xdist):
#    - Tests run simultaneously on multiple CPU cores.
#    - Achieved using the 'pytest-xdist' plugin and the '-n' flag (e.g., 'pytest -n 4', 'pytest -n auto').
#    - Reduces the overall execution time significantly, ideally to the time of the longest single test.
#    - Requires tests to be completely isolated (no shared state or dependencies).
#    - Uses multiprocessing, creating separate python processes.
#
# 3. Concurrent Execution:
#    - Multiple tasks are managed by switching between them when one is waiting (e.g., for I/O).
#    - Improves responsiveness and efficiency for I/O-bound tasks.
#    - Does NOT provide true simultaneous execution on multiple cores (due to the GIL).
#    - Managed by the python interpreter within a single process.
#    - Uses the asyncio library.
#
# Important Note:
#    - Ensure your tests are 100% isolated. Sharing state or dependencies
#      between tests can lead to unpredictable results when running in parallel.
#    - If your tests are I/O bound, then you will see a large improvement in test time.
#      If your tests are CPU bound, the improvement will be less dramatic.