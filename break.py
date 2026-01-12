for i in range(5):
    print( "Starting loop number" + str(i))
    
    stop = input("Stop the loop(y/n)? ")
    if stop=="y":
        print(stop)
        print( str(i))
        break
    else:
        continue
    print("Ending loop number"+ str(i))

print("Program finished")