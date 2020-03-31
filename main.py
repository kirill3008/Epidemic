import random

CITY_SIZE = 100
POPULATIONS = 10000

TRACK_LENGTH = 24

class Person(object):
    def __init__():
        self.contagiousness = 0

    def create_daily_track():
        return [random.randint(0,CITY_SIZE) for i in TRACK_LENGTH]

    def update(dose):
        pass


def epidemic_end():
    pass
def main():
    """
    Стартовые процедуры
    """
    id_people = {}
    people = id_people.values()
    """
    Основой цикл
    """
    while epidemic_end():
        for person in people:         
            id_track[person.id] = person.create_daily_track()

        for i in range(TRACK_LENGTH):
            on_points = [[] for i in range(CITY_SIZE)]
            for person in people:
                on_points[id_track[person.id]] = person.id
            for point in on_points:
                sum_on_point = sum([id_people[i].contagiousness for i in point])
                for person_id in point:
                    id_people[person_id].update(dose)








        
