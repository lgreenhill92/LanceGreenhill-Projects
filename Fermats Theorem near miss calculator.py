import tkinter as tk

"""
FEB 2024

The 17th century mathematician Pierre Fermat’s sparked 400 years of nightmares for mathematicians by claiming he had a proof for his “last theorem,”
but then not providing the proof.
Fermat’s last theorem states that there are no natural numbers (1, 2, 3,…) x, y, and z such that xn + yn = zn, in which n is a natural number greater than 2.
After mathematicians spent centuries of futility trying to devise a proof,
the English mathematician Andrew Wiles published a proof of Fermat’s last theorem in 1995,
a proof that is generally believed to be correct (though at about 130 pages, it is pretty difficult to understand).
If you’d like to know more about Fermat’s Last Theorem,
and pop culture references to it (like by the Simpson’s and Star Trek), please see  https://www.youtube.com/watch?v=ReOQ300AcSU.

This application helps an interactive user search for 
“near misses” of the form (x, y, z, n, k) in the formula xn + yn = zn,
where x, y, z, n, k are positive integers, where 2< n <12,
where 10 <= x <= k, and where 10 <= y <= k.

"""



def calculate_result():
    try:
        n = int(n_entry.get())
        k = int(k_entry.get())

        # Validate n so it is in desired range
        while n <= 2 or n >= 12:
            # print("Please enter n between 2 and 12")
            # n = int(input("Enter n (power):"))
            raise ValueError
            

        # Validate k so it is in desired range
        #k = int(input("Enter k (upper limit on x/y values):")) # upper limit on values x,y
        while k < 10 or k > 80:
            # print("Please enter k between 10 and 80")
            # k = int(input("Enter k (upper limit on x/y values):"))
            raise ValueError
            

        z_arr = [0, 0] # initialize array

        # calulate values for 2-100^n, traverse this array
        for i in range(2,101):
            z_arr.append(i**n)
        # print(z_arr)

        x = 10 # 10 <= x <= k
        y = 10 # 10 <= y <= k
        x_count = 11 # used to help increment
        smallest_miss = 999999999999
        smallest_relative_miss = 9999999999999


        while x <= k and y <= k:
            result = (x**n + y**n) # (x^n + y^n)
            p1, p2 = 0, 1 # use two pointers to traverse z_arr
            for i in z_arr:
                if z_arr[p1] < result and z_arr[p2] > result: #  find "bracket" using pointers
                    # calculate miss
                    current_miss = min((result-z_arr[p1]),(z_arr[p2]-result))
                    current_relative_miss = (current_miss/result)
                    if current_relative_miss < smallest_relative_miss:
                        smallest_relative_miss = current_relative_miss
                        smallest_miss = current_miss
                        limits = 'lower: {0}, upper: {1}'.format(z_arr[p1],z_arr[p2])
                    # check all combinations while incrementing x
                    if x < k:
                        x+=1
                    else:
                        # increment y and x and continue calculating combinations
                        x = x_count
                        x_count+=1
                        y+=1
                p1+=1
                p2+=1

        # Perform your calculations here based on the input values
        # For demonstration purposes, let's just print the input values:
        print(f"n: {n}, k: {k}")

        # Update the results display
        results_label.config(text=f"Results:\nn: {n}\nk: {k}\n" +
                             
                             '\n{0}^{2} + {1}^{2} = {3}\n'.format(x,y,n, result) +
                            #  'lower: {0}, upper: {1}'.format(z_arr[p1],z_arr[p2]) +
                            limits + 
                             '\nMiss: {0}'.format(current_miss) +
                             '\nSmallest relative miss found: {:.8%}'.format(smallest_relative_miss))

    except ValueError:
        results_label.config(text="Please enter n between 2 and 12"+"\nPlease enter k between 10 and 80")

def reset_fields():
    n_entry.delete(0, tk.END)
    k_entry.delete(0, tk.END)
    results_label.config(text="Results:")

# Create the main window
window = tk.Tk()
window.title("Power Calculator")
window.geometry("400x400")

# Input for n
n_label = tk.Label(window, text="Enter n:")
n_label.pack()
n_entry = tk.Entry(window)
n_entry.pack()

# Input for k
k_label = tk.Label(window, text="Enter k:")
k_label.pack()
k_entry = tk.Entry(window)
k_entry.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_result)
calculate_button.pack()

# Results display
results_label = tk.Label(window, text="Results:")
results_label.pack()

# Reset button
reset_button = tk.Button(window, text="Reset", command=reset_fields)
reset_button.pack()

# Start the event loop
window.mainloop()

