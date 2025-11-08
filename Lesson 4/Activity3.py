print("Please enter your marks")
maths= int(input("math:"))
science= int(input("science:"))
english= int(input("english:"))
civics= int(input("civics:"))
history= int(input("history:"))
sum = maths+science+english+civics+history

print("After the given marks, your overall percent of this academic year is-")
percent= (sum/500)*100
print(end="Percent-")
print(percent)
