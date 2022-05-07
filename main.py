from queue import Queue
import time

process1_number = 2
process2_number = 3
process3_number = 5
process_potency = 1000000

quantum1 = 0.001
quantum2 = 0.01
quantum3 = 0.1
quantum4 = 1

def main():
    # Get time when starts
    initial_time = time.time()
    # Insert the desirable quantum below
    run_all_processes(quantum1)
    # Get time when finishes
    execution_time = time.time() - initial_time
    print('Tempo Final: ' + str(execution_time) + ' segundos')

# Process Functions
def process1(number = 1, potency = 1, quantum = 1):
    process_initial_time = time.time()
    multiplier = 2
    while(time.time() - process_initial_time < quantum) and (potency <= 1000000):
        number *= multiplier
        potency += 1
    return [number, potency]

def process2(number = 1, potency = 1, quantum = 1):
    process_initial_time = time.time()
    multiplier = 3
    while(time.time() - process_initial_time < quantum) and (potency <= 1000000):
        number *= multiplier
        potency += 1
    return [number, potency]
    
def process3(number = 1, potency = 1, quantum = 1):
    process_initial_time = time.time()
    multiplier = 5
    while(time.time() - process_initial_time < quantum) and (potency <= 1000000):
        number *= multiplier
        potency += 1
    return [number, potency]

def run_all_processes(quantum = 1):
    process1_numbers = [1,1]
    process2_numbers = [1,1]
    process3_numbers = [1,1]

    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    # Whenever a process ends, it will not more be in the queue, therefore won't run anymore
    while not queue.empty():
        process = queue.get()
        print("Inside While. Process: " + str(process))
        if process == 1:
            process1_numbers = process1(process1_numbers[0], process1_numbers[1], quantum)
            if process1_numbers[1] <= 1000000 :
                queue.put(1)
                print('Process 1 potency:' + str(process1_numbers[1]))
        
        elif process == 2:
            process2_numbers = process2(process2_numbers[0], process2_numbers[1], quantum)
            if process2_numbers[1] <= 1000000 :
                queue.put(2)
                print('Process 2 potency:' + str(process2_numbers[1]))

        elif process == 3:
            process3_numbers = process1(process3_numbers[0], process3_numbers[1], quantum)
            if process3_numbers[1] <= 1000000 :
                queue.put(3)
                print('Process 3 potency:' + str(process3_numbers[1]))

main()