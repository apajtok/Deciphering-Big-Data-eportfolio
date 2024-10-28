import dask
import dask.distributed

# Create a Dask client (connects to a local cluster by default)
client = dask.distributed.Client()  

# Define a function to be executed in parallel
def process_data(data):
    # Replace this with your data processing logic
    result = data * 2  
    return result

if __name__ == '__main__':
    data_list = [1, 2, 3, 4, 5]  

    # Create Dask delayed objects for each data item
    delayed_results = [dask.delayed(process_data)(data) for data in data_list] 

    # Compute the results in parallel
    results = dask.compute(*delayed_results)  

    # Print the results
    print(
