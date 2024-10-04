import subprocess
import threading
import time
import os

# Configure number of threads and number of commits per thread
NUM_THREADS = 15
COMMITS_PER_THREAD = 100000000000000
# Set the path to the local Git repository
REPO_PATH = "/home/dam/commit-test"

def make_commit(thread_id):
    for i in range(COMMITS_PER_THREAD):
        commit_message = "Commit"
        try:
            # Create an empty commit
            subprocess.run(['git', 'commit', '--allow-empty', '-m', commit_message], check=True)
            print(f"Thread {thread_id}: Created commit {i}")
        except subprocess.CalledProcessError as e:
            print(f"Error in thread {thread_id} during commit {i}: {e}")

def run_commit_farm():
    threads = []

    # Change to the specified repository directory
    os.chdir(REPO_PATH)

    # Create threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=make_commit, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    run_commit_farm()
    end_time = time.time()
    print(f"Commit farm completed in {end_time - start_time} seconds.")
