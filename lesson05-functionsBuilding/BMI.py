def BMI(height, weight):
    return weight/(height**2)


def classify(BMI):
    if BMI <= 18.5:
        print("Gầy! Nguy cơ phát bệnh thấp!")
    elif 18.5 < BMI <= 24.9:
        print("Bình thường! Nguy cơ phát bệnh trung bình!")
    elif 25 < BMI <= 29.9:
        print("Hơi béo! Nguy cơ phát bệnh cao!")
    elif 29.9 < BMI <= 34.9:
        print("Béo phì cấp độ 1! Nguy cơ phát bệnh cao!")
    elif 34.9 < BMI <= 39.9:
        print("Béo phì cấp độ 2! Nguy cơ phát bệnh rất cao!")
    elif BMI > 40.0:
        print("Béo phì cấp độ 3! Nguy cơ phát bệnh nguy hiểm!")


height, weight = eval(input("Input height and weight: "))
bmi = BMI(height, weight)
classify(bmi)


