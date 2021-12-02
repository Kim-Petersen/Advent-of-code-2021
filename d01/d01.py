from sys import argv

def count_number_of_times_depth_measurement_increases(measurements):
    return sum(
        [x[1] > x[0]
        for x in
        zip(measurements[0:-1], measurements[1:])
        ]
    )

if __name__ == '__main__':
    try:
        with open(argv[-1], 'r') as f:
            measurements = [int(x) for x in f.read().split()]

        print(count_number_of_times_depth_measurement_increases(measurements))
        
        three_sliding_window_measurements = list(map(
            sum,
            zip(measurements[0:-2], measurements[1:-1], measurements[2:])
            ))
        
        print(count_number_of_times_depth_measurement_increases(three_sliding_window_measurements))


    except:
        print(argv[0])