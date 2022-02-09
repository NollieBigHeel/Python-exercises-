students_name = str(input("Please enter students Name: "))
homework_score = int(input("Please enter students homework score /25: "))
assessment_score = int(input("Please enter students assessment score /50: "))
final_exam_score = int(input("Please enter students final exam score /100: "))
 
def score() :
    return(homework_score + assessment_score + final_exam_score)

percent = round(score() / 175 * 100)
    


if 85 < percent <= 100:
    print(f"{students_name}'s final ICT grade is an A, {percent}%")
elif 70 < percent <= 85:
    print(f"{students_name}'s final ICT grade is a B, {percent}%")
elif 60 < percent <= 70:
    print(f"{students_name}'s final ICT grade is a C, {percent}%")
elif 40 < percent <= 60:
    print(f"{students_name}'s final ICT grade is a D, {percent}%")
elif 25 < percent <= 40:
   print(f"{students_name}'s final ICT grade is E , {percent}%")
else:
    print(f"{students_name}'s final ICT grade is a F, {percent}%")