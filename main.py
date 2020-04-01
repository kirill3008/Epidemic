import random

CITY_SIZE = 10000
POPULATION = 10000
TRACK_LENGTH = 1

class Person(object):
    # Надо добавить варианты Random, Average, Exect(с приложенным словарем парметров)
    """
    Person parametrs:
        age -- возраст
        disease -- наличие болезней повышающих шансы умереть
        sex -- пол
        nationality -- национальность (может влиять на вероятность заболеть)
        elitism ("poor" : 1, "av" : 2, "rich" : 3) -- эллитарность? влияет на возможности по лечению болезни и другие параметры связанные с доходом
    """
    def __init__(self,p_id,person_type = "Random"):
        if person_type == "Random":
            self.age = random.randint(1,128)
            self.sex = random.randint(0,1)
            self.disease = random.randint(0,1)
            self.nationality = None
            self.elitism = random.randint(1,3)

        self.contagiousness = 0
        self.id = p_id

    def create_daily_track(self):
        return [random.randint(0,CITY_SIZE-1) for i in range(TRACK_LENGTH)]

    def update(self,dose):
        if dose > 0:
            if random.uniform(0,1) >= 1/((dose**0.5)*1.2):
                self.contagiousness = 1
        


def create_average_population():
    pass
    return population


#переделать, все болеют это не дело
def epidemic_end(people):
    for person in people:
        if person.contagiousness == 0:
            return False
    return True
    


def main():
    """
    Стартовые процедуры
    """
    id_people = {}
    for i in range(POPULATION):
        id_people[i] = Person(i)
    id_people[random.randint(0,POPULATION-1)].contagiousness = 1
    people = id_people.values()
    """
    Основой цикл
    """
    while not epidemic_end(people):
        id_track = {}
        for person in people:         
            id_track[person.id] = person.create_daily_track()

        for point_num in range(TRACK_LENGTH):
            on_points = [[] for j in range(CITY_SIZE)]
            for person in people:
                on_points[id_track[person.id][point_num]].append(person.id)
            for point in on_points:
                dose = sum([id_people[j].contagiousness for j in point])
                for person_id in point:
                    id_people[person_id].update(dose)
        ill = 0
        for person in people:
            if person.contagiousness > 0:
                ill += 1
        print("All: {0}, Infected: {1}, Healthy: {2}".format(POPULATION, ill, POPULATION - ill))





if __name__ == "__main__":
    main()


        
