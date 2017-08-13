import numpy as np

def generate_samples():
    with open('TensorFlow\\DCGAN\\sample_file.txt', 'w') as fout:
        sample = np.random.uniform(-1.0, 1.0, size=(64, 100))
        #sample = np.zeros(shape=(64, 100))
        #sample[0] = np.random.uniform(-1.0, 1.0, 100)
        #sample[63] = np.random.uniform(-1.0, 1.0, 100)
        #for idx in range(62):
        #    sample[idx+1] = float(idx / 63.0) * (sample[63] - sample[0]) + sample[0]

        for row in range(64):
            for col in range(100):
                fout.write(str(sample[row, col]) + " ")
            fout.write("\n")

def interpol_samples():
    with open('TensorFlow\\DCGAN\\sample_file.txt', 'w') as fout:
        sample = np.zeros(shape=(64, 100))
        sample[0] = np.random.uniform(-1.0, 1.0, 100)
        sample[63] = np.random.uniform(-1.0, 1.0, 100)
        for idx in range(62):
            sample[idx+1] = float(idx / 63.0) * (sample[63] - sample[0]) + sample[0]

        for row in range(64):
            for col in range(100):
                fout.write(str(sample[row, col]) + " ")
            fout.write("\n")

def alrithmetic_sample():
    with open('TensorFlow\\DCGAN\\sample_file.txt', 'w') as fout:
        sample = np.zeros(shape=(64, 100))
        vec_sample = np.zeros(shape=(3, 100))
        fin = open('TensorFlow\\DCGAN\\exemplar_vector.txt')
        vec_list = [[float(x) for x in line.split()] for line in fin]
        for row in range(3):
            for col in range(100):
                vec_sample[row, col] = vec_list[row][col]
        #rst_vector = (vec_sample[0] + vec_sample[1] + vec_sample[2]) / 3.0
        rst_vector = vec_sample[0] - vec_sample[1] + vec_sample[2]
        for idx in range(64):
            #sample[idx] = rst_vector + 0.5 * np.random.uniform(-1.0, 1.0, 100)
            sample[idx] = rst_vector

        for row in range(64):
            for col in range(100):
                fout.write(str(sample[row, col]) + " ")
            fout.write("\n")

if __name__ == '__main__':
    generate_samples()
    #interpol_samples()
    #alrithmetic_sample()
