with open('artifacts.txt','r') as f:
    text = f.read()
with open('artifacts.txt','w') as f:
    text = f.write("I added one more line")
print(text)
print("Stage 3 was ended")

