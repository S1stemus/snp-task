class NoSuchStrategyError(Exception):
    pass
class WrongNumberOfPlayersError(Exception):
    pass
def rps_game_winner(arr):
        elements="RPS"
        if len(arr)!=2:
            raise WrongNumberOfPlayersError()
        for element in arr:
            if element[1] not in elements:
                raise NoSuchStrategyError()
        if arr[0][1]==arr[1][1]:
            return arr[0][0]+" "+arr[0][1]
        if (arr[0][1]=="R" and arr[1][1]=="S") or (arr[0][1]=="S" and arr[1][1]=="P") or (arr[0][1]=="P" and arr[1][1]=="R"):
            return arr[0][0]+" "+arr[0][1]
        else:
            return arr[1][0]+" "+arr[1][1]
print(rps_game_winner([['player1', 'P'], ['player2', 'A'],]))
print(rps_game_winner([['player1', 'R'], ['player2', 'S'],]))
print(rps_game_winner([['player1', 'R'], ['player2', 'R'],]))
print(rps_game_winner([['player1', 'R'], ['player2', 'P'],[]]))