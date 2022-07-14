from itertools import combinations

class Team:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
        

class Field:
    def __init__(self, name, available_times):
        self.name = name
        self.available_times = available_times
    def __str__(self):
        return self.name

class Game:
    def __init__(self, team1, team2, field, time):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.time = time
    def __str__(self):
        return f"{self.time} - {self.field.name} - {self.team1.name} vs {self.team2.name} "
        
class Scheduler:
    def __init__(self, teams, fields):
        self.teams = teams
        self.fields = fields
        self.schedule = []
        
    def schedule_games(self):
        for t1, t2 in combinations(set(self.teams), 2):
            field, game_time = self.get_next_available_time()
            self.schedule.append(Game(t1, t2, field, game_time))
        return self.schedule

    def get_next_available_time(self):
        for f in self.fields:
            if len(f.available_times) > 0:
                return f, f.available_times.pop(0)
        raise Exception("No more available timeslots!")



if __name__ == "__main__":
    
    teams = (
        Team("Marlins"),
        Team("Brewers"),
        Team("Reds"),
        Team("Cubs"),
    )

    base_schedule = [  
        "2022-07-10 17:30", 
        "2022-07-10 19:30",
        "2022-07-11 17:30", 
        "2022-07-11 19:30",
        "2022-07-12 17:30", 
        "2022-07-12 19:30",
        "2022-07-13 17:30",
        "2022-07-13 19:30",
        "2022-07-14 17:30",
        "2022-07-14 19:30",
        ]

    fields = (
        Field("Field 1", base_schedule),
        Field("Field 2", base_schedule),
        Field("Field 3", base_schedule),
    )

    scheduler = Scheduler(teams, fields)
    schedule = scheduler.schedule_games()
    for game in schedule:
        print(game)
  
