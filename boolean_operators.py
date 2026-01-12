# and ,not,or

is_raining = True
is_windy = True

stay_inside = is_raining and is_windy

print("Stay inside: " + str(stay_inside))

take_coat = is_raining or is_windy

print("Take Coat: " + str( take_coat))

print("Not Windy:" + str( not is_windy))

take_umbrella = is_raining and not is_windy

print("Take Umbrella: "+ str(take_umbrella))