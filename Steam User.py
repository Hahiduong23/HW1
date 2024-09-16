class SteamUser:
    def __init__(self, username, games):
        self.username = username  
        self.games = games        
        self.played_hours = 0     #số giờ chơi mặc định là 0
    
    def play(self, game, hours):
        if game in self.games:          #kiểm tra xem trò chơi chọn có nằm trong danh sách hay ko
            self.played_hours += hours  #nếu có thì cộng số giờ chơi vào tổng số giờ chơi
            return f"{self.username} is playing {game}"     
        else:
            return f"{game} is not in library"              #nếu ko trả về kq trò chơi ko nằm trong thư viện
    
    def buy_game(self, game):
        if game not in self.games:                   #ktra xem trò chơi đã có trong danh sách chưa
            self.games.append(game)                  #nếu có thì thêm trò chơi vào danh sách
            return f"{self.username} bought {game}"  #trả về là người dùng đã mua game
        else:
            return f"{game} is already in your library"  #nếu có rồi thì tả về game đã có trong danh sách
    
    def status(self):
        games_count = len(self.games)          
        return f"{self.username} has {games_count} games. Total play time: {self.played_hours}"    
    
    
user = SteamUser("Peter", ["Rainbow SixSiege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())