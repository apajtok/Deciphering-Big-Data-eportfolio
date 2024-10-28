
import multiprocessing

def process_data(data):
    # Replace this with your data processing logic
    result = data * 2  
    return result

if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5] 

    # Create a pool of processes (using the number of CPU cores)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    # Process the data in parallel using the 'map' function
    results = pool.map(process_data, data_list)

    # Close the pool and wait for processes to finish
    pool.close()
    pool.join()

    # Print the results
    print(results)
