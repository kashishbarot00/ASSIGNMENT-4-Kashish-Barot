#input
fname = input("Enter your first name: ")
num_steps = int(input("Enter the number of steps you walked in a day: "))

#process
calories_burned = num_steps * 0.25

#output
print(fname, "burned", calories_burned, "calories by walking", num_steps, "steps today.")
