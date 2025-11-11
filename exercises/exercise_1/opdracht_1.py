def likes(team: list) -> str:
    if team == []: 
        return "no one likes this"
    elif len(team)==1:
        return f"{team[0]} likes this"
    elif len(team)==2:
        return f"{team[0]} and {team[1]} like this"
    elif len(team)==3:
        return f"{team[0]}, {team[1]} and {team[2]} like this"
    elif len(team)>=4:
        return f"{team[0]}, {team[1]} and {len(team)-2} others like this"
    else: 
        return "something went wrong, oopsie"