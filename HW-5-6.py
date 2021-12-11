subj = {}
with open('test_6.txt', 'r') as school:
    print(school)
    for line in school:
        subject, lecture, practice, lab = line.split(' ')
        subj[subject.replace(':', '')] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество занятий в часах по предмету - \n {subj}')

