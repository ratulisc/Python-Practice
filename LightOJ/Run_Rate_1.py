t = int(input())
for i in range(t):
    run_list = input().split()
    opponent_run = int(run_list[0])
    current_run = int(run_list[1])
    remaining_ball = int(run_list[2])
    present_run_rate = 0
    required_run_rate = 0
    remaining_over = remaining_ball / 6
    print(remaining_over)
    played_over = 50 - remaining_over
    present_run_rate = current_run / played_over
    required_run_rate = ((opponent_run - current_run) + 1) / remaining_over

    print("{:.2f}".format(present_run_rate)," ","{:.2f}".format(required_run_rate))
