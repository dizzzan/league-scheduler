
from itertools import combinations

class Team:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
        

class Location:
    def __init__(self, name, available_times):
        self.name = name
        self.available_times = available_times
    def __str__(self):
        return self.name

class Game:
    def __init__(self, team1, team2, location, time):
        self.team1 = team1
        self.team2 = team2
        self.location = location
        self.time = time
    def __str__(self):
        return f"{self.time} - {self.location.name} - {self.team1.name} vs {self.team2.name} "
        
class Scheduler:
    def __init__(self, teams, location):
        self.teams = teams
        self.location = location
        self.schedule = []
        
    def schedule_games(self):
        for t1, t2 in combinations(set(self.teams), 2):
            location, game_time = self.get_next_available_time()
            self.schedule.append(Game(t1, t2, location, game_time))
        return self.schedule

    def get_next_available_time(self):
        for l in self.location:
            if len(l.available_times) > 0:
                return l, l.available_times.pop(0)
        raise Exception("No more available timeslots!")

