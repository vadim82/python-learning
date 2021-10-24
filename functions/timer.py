import time

def make_timer():
    last_called = None
    def elapsed():
        now = time.time()
        nonlocal last_called
        if last_called is None:
            last_called = now
        result = now - last_called
        last_called = now
        return result
    return elapsed

if __name__ == "__main__":
    t = make_timer()
    print(t())
    print(t())
    time.sleep(2)
    print(t())