import numpy as np

def zombie(n, k, init_pos):
    rand_dir = np.random.uniform(low = 0, high = 1, size = n)
    len_dir = len(rand_dir)
    direction = [None] * len_dir
    future_pos = [None] * len_dir

    """Initialize the direction"""
    for i in range(len_dir):
        if rand_dir[i] <= 0.5:
          direction[i] = -1
        else:
          direction[i] = 1

    stat = [None] * n
    step_pos = [None] * n
    step_pos = init_pos[:]
    future_pos = np.array(step_pos) + np.array(direction)
    #print("step_pos : " + str(step_pos) + "\t" + " || direction : " + str(direction))
    i=0
    while True:
        temp_direction = direction[:]
        for j in range(n):
          id_match=np.where(future_pos[j]==step_pos)[0]

          if len(id_match > 0):
            dir_match = temp_direction[id_match[0]]

          """Change the direction"""
          next_future_pos = future_pos[j] + direction[j]
          if future_pos[j] in step_pos:
            if dir_match != direction[j] and direction[j] == temp_direction[j]:
              direction[j] = -1 * direction[j]
              future_pos[j] = step_pos[j]

            if dir_match == direction[j] and next_future_pos in step_pos:
              future_pos[j] = step_pos[j]

          if step_pos[j] < 1 or step_pos[j] > (k-2):
            stat[j] = "Pass"

        """Update the step"""
        step_pos = future_pos
        future_pos = np.array(step_pos) + np.array(direction)

        #print("step_pos : " + str(step_pos) + "\t" + " || direction : " + str(direction) + "\t" + " || status : " + str(stat))
        i = i+1
        if None not in stat:
          break

    return(i)

def main():
    n = input("The number of zombies : ")
    k = input("The length of the bridge (meters) : ")
    init = raw_input("Initial position (separated by space): ")
    init_pos = [int(i) for i in init.split(" ")]

    if(len(init_pos) > n):
        init_pos = init_pos[:n]

    ntest = 1000
    time = [None] * ntest
    print("\n" + "Calculating...")
    for i in range(ntest):
        time[i] = zombie(n, k, init_pos)
        if i%100 == 0:
            print(str(i))
    max_time = max(time)
    min_time = min(time)

    print("\n" + "Result : ")
    print("Max. time : " + str(max_time) + "\t" + " || Min. time : " + str(min_time))
    return(time, max_time, min_time)

main()
