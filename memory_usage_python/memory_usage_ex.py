from memory_profiler import profile

@profile
def process_start(n):
    for i in range(n):
        print ("Hello World")

    return n

process_start(10)
