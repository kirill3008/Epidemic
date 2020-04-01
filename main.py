import random
from math import *

CITY_SIZE = 10000
POPULATION_PARAMETRS = {
    "Type" : "Random",
    "Size" : 10000
}
TRACK_LENGTH = 24

class Person(object):
    """
    Надо добавить варианты Random, Average, Exect(с приложенным словарем парметров)
    Random -- случайный человек
    Average -- нормальный человек (нормальный в статистическом понимании)
    Exact -- человек с четкозаднными парметрами
    Person parametrs:
        age -- возраст
        imunity -- мощь имунитета
        disease -- наличие болезней повышающих шансы умереть
        sex -- пол
        nationality -- национальность (может влиять на вероятность заболеть)
        elitism ("poor" : 1, "av" : 2, "rich" : 3) -- эллитарность? влияет на возможности по лечению болезни и другие параметры связанные с доходом
        work_point -- место в городе где человек работает
        home_point -- место дома
    """
    def __init__(self,p_id,person_type = "Random",parametrs = None):
        if person_type == "Random":
            self.age = random.randint(1,128)
            self.sex = random.randint(0,1)
            self.disease = random.randint(0,1)
            self.nationality = None
            self.elitism = random.randint(1,3)
            self.imunity = random.uniform(0,1)
            self.home_point = random.randint(0,CITY_SIZE-1)
            self.work_point = random.randint(0,CITY_SIZE-1)

        self.contagiousness = 0
        self.id = p_id

    def create_daily_track(self):
        return [random.randint(0,CITY_SIZE-1) for i in range(TRACK_LENGTH)]

    def update(self,dose):
        if dose > 0:
            if random.uniform(0,1) >= 1-atan(dose/16)/pi:
                self.contagiousness = 1
        

#Add other types of population !!!
def create_population(population_parametrs):
    if population_parametrs["Type"] == "Random":
        population = [Person(i) for i in range(population_parametrs["Size"])]
    else:
        pass
    return population


#переделать, все болеют, а это не дело
def epidemic_end(people):
    for person in people:
        if person.contagiousness == 0:
            return False
    return True
    


def main():

    """
    Стартовые процедуры
    """

    people = create_population(POPULATION_PARAMETRS)
    id_people = dict([(person.id,person) for person in people]) 

    #создание нулевого пациента
    people[random.randint(0,POPULATION_PARAMETRS["Size"]-1)].contagiousness = 1




    """
    Основой цикл
    """
    day = 0
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
        day += 1
        print("Day: {0}, All: {1}, Infected: {2}, Healthy: {3}".format(day,POPULATION_PARAMETRS["Size"], ill, POPULATION_PARAMETRS["Size"] - ill))





if __name__ == "__main__":
    main()


        
