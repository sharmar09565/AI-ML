# We have to search if there exist a word python in the file sample.txt

data = True
line = 1
word = "Python" 
with open("sample.txt", "r") as f:

    while(data):
        data = f.readline()
        
        if(word in data):
            print(f"data found at {line}")
            break
        line+=1
        