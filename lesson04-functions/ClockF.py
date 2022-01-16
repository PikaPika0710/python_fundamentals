from time import process_time, perf_counter

start = perf_counter()
print("Enter a value: ")
x = input()
print("X = ", x)
end = perf_counter()
print("Duration: ", end-start)



