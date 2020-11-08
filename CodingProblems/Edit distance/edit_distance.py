
# * Pass the initial word and target word

def edit_distance(initial, target):
    
    # ? Finding which word is smaller
    initial_len = len(initial)
    target_len = len(target)

    # ? Getting their difference , since thats the no. of letters that we have to edit to get target word
 
    distance = abs(initial_len - target_len)

    if initial_len < target_len : smaller = initial_len 
    else : smaller = target_len

    # ? Comparing all the letters at respective positions of both words to find whether we should change it or keep it 
    for pos in range(smaller):
        if initial[pos] != target[pos]:
            distance += 1
        
    # ! The edit distance is the sum of all the difference we got from above
    return distance

if __name__ == '__main__':

    initial = input("Enter the initial word : ")    # The original word
    target = input("Enter the target word : ")        # The word into which the original must be changed

    distance = edit_distance(initial,target)

    print("Edit distance : ", distance)
