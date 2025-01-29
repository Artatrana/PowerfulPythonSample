# pickling and unpickling example

import pickle

# Object to pickle
def pickle_data_test():
    data = {'name': 'Ramesh', 'role': 'Data Engineer', 'experience': 20}

    with open('data.pkl', 'wb') as file:
        pickle.dump(data,file)

    print("Data has been pickled.")

def unpickle_data():
    with open('data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)

    print("Data has been unpickled:", loaded_data)

if __name__ == '__main__':
    #pickle_data_test()
    unpickle_data()

