def person(name, age, sex, job):
    data = {
        'name': name,
        'age': age,
        'sex': sex,
        'job': job
    }
    return data


def dog(dog, dog_type):
    data = {
        'dog': dog,
        'dog_type': dog_type
    }
    return data


d1 = dog("李磊", "京巴")

p1 = person("严帅", 36, "F", "运维")

p2 = person("林海峰", 27, "F", "Teacher")
