import os

def load_input_data(filename):
    if os.path.isfile(filename):
        try:
            input_file_handle = open(filename, mode='r')

            return input_file_handle
        except Exception as e:
            print("Something went wrong loading the input file : " + str(e))
    else:
        print('File does not exist.')