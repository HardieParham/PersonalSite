import math
import csv
import matplotlib.pyplot as plt



def return_dynamics_results():

    ### Problem Statement Values
    # General
    W = 518.086 #kips
    g = 386.1 # in/sec^2

    # Columns
    Fy_column = 50 #ksi
    E_column = 29000 #ksi
    I_column = 577 #in^4
    A_column = 18.7 #in^2
    d_column = 14.00 #in

    # Brace
    Fy_brace = 55 #ksi
    diameter_brace = 3 #in
    E_brace = 29000 #ksi
    A_brace = 7.06858 #in^2

    # Frame
    H_frame = (55 * 12) #in
    L_frame = (31.5 * 12) #in



    ### Problem Set
    # a) Derive the mass in units of kip/(in/sec^2)
    M = W / g  #Mass = Weight / gravity
    print(f'a) Derive the mass: {round(M, 2)} kip/(in/sec^2)') # I use round (x, 2) often to round to 2 decimal points.

    # b) Find Equivalent Stiffness
    L_brace = math.sqrt((H_frame ** 2) + (L_frame ** 2))
    k_brace = ((A_brace * E_brace) / L_brace) * math.atan(L_brace/H_frame) #K_frame translated to x direction via arc-tan
    k_column = (3 * E_column * I_column)/(H_frame ** 3)
    k_frame_1 = (2 * k_column) + k_brace #Only 1 brace is added to stiffness. Cables provide no resistance in compression.
    k_eq = 2 * k_frame_1 #k_frame_1 and k_frame_2 are equal
    print(f'b) Derive k equivalent: k_eq = {round(k_eq, 2 )} kip/in')

    # 3) Compute Natural Frequencies
    wn = math.sqrt(k_eq / M)
    T = 2 * math.pi / wn
    f = 1 / T
    print(f'c) Compute natural frequencies:w = {round(wn, 2)} Hz, f = {round(f, 2)} Hz, T = {round(T, 2)} sec')

    # 4) Load and Plot Ground Acceleration
    ground_data = get_ground_data()
    plt.plot(ground_data[0], ground_data[1])
    plt.xlabel("time (sec)")
    plt.ylabel("acceleration (G)")
    plt.show() # See Graph 1
    print('d) ground data plotted')

    # 5) Plot F(t)
    h = 0.01
    forcing_x_data = []
    forcing_y_data = []
    i = 0.00
    j = 0
    while i < 20.01:
        force = ground_data[1][j] * M
        forcing_x_data.append(i)
        forcing_y_data.append(force)
        i += h

        forcing_x_data.append(i)
        forcing_y_data.append(force)
        i += h
        j += 1

    plt.plot(forcing_x_data, forcing_y_data)
    plt.xlabel("time (sec)")
    plt.ylabel("Force (kip)")
    plt.show() # See Graph 2
    print('e) Forcing Function Plotted')


    def get_displacements(damping):
        wd = wn * math.sqrt(1 - (damping ** 2))
        u_data = [0]
        A = [0]
        B = [0]

        t = 0.00
        j = 0
        dt = 0.01

        # Note, instead of i and i-1, im using i+1 and i
        while t < 20.01:
            A_d = A[j] + ((dt / 2) * ((forcing_y_data[j] * math.e ** (damping * wn * t) * math.cos(wd * t)) + (forcing_y_data[j + 1] * math.e ** (damping * wn * (t+dt)) * math.cos(wd * (t+dt)))))
            A.append(A_d)
            
            B_d = B[j] + ((dt / 2) * ((forcing_y_data[j] * math.e ** (damping * wn * t) * math.sin(wd * t)) + (forcing_y_data[j + 1] * math.e ** (damping * wn * (t+dt)) * math.sin(wd * (t+dt)))))
            B.append(B_d)

            u_d = (math.e ** (-damping * wn * (t+dt)) / (M * wn)) * ((A_d * math.sin(wd * (t+dt))) - (B_d * math.cos(wd * (t+dt))))
            u_data.append(u_d)

            t += dt
            j += 1 

        return u_data

    # 6) Find u(t), Damping = 0
    zero_damping_data = get_displacements(damping = 0.00)
    print(f'f) damping = 0% plotted. Max u = {round(max(zero_damping_data), 2)} in. Min u = {round(min(zero_damping_data), 2)}')
    plt.plot(forcing_x_data, zero_damping_data)
    plt.xlabel("time (sec)")
    plt.ylabel("Displacement (in)")
    plt.show() # See Graph 3

    # 7) Find u(t), Damping = 0.10
    ten_damping_data = get_displacements(damping = 0.10)
    print(f'g) damping = 10% plotted. Max u = {round(max(ten_damping_data), 2)} in. Min u = {round(min(ten_damping_data), 2)}')
    plt.plot(forcing_x_data, ten_damping_data)
    plt.xlabel("time (sec)")
    plt.ylabel("Displacement (in)")
    plt.show() # See Graph 4

    # 8) Find u(t), Damping = 0.05
    five_damping_data = get_displacements(damping = 0.05)
    print(f'h) damping = 5% plotted. Max u = {round(max(five_damping_data), 2)} in. Min u = {round(min(five_damping_data), 2)}')
    plt.plot(forcing_x_data, five_damping_data)
    plt.xlabel("time (sec)")
    plt.ylabel("Displacement (in)")
    plt.show() # See Graph 5


    # 9) Comment on previous displacement data
    print('i) comment on displacement data: Zero damping causes the largest deflections as expected. 0.1 and 0.05 dampings behave very similarly, with 0.1 having slightly smaller displacements. Also it is interesting that the largest deflections occur when the forcing function has the largest amplitude (at 2, 5, and 10 seconds) for the damped cases, but not for the undamped, deflections actually decrease after the forcing spike at 5 sec.')


    # 10) find max stresses in columns and braces
    u_max_five = round(max(five_damping_data), 2)
    u_min_five = round(min(five_damping_data), 2)
    u_max = max( u_max_five, abs(u_min_five))

    stress_column = u_max * E_column / H_frame
    stress_brace = u_max * E_brace / L_brace

    print(f'j) The max stress in the columns is: {round(stress_column, 2)} ksi, and the braces is: {round(stress_brace, 2)} ksi. Linear-elastic analysis is valid for the displacement and stresses proved to be relatively small for the forces applied.')



def get_ground_data():
    x_values = []
    y_values = []
    with open('src/static/files/data.txt') as file: # accerleration data taken from: https://www.vibrationdata.com/elcentro.htm
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            x_values.append(float(row[0]))
            y_values.append(float(row[1]) * 1000)

    return (x_values, y_values)



if __name__ == "__main__":
    x= return_dynamics_results()