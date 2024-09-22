import pandas as pd


accPlayers = pd.read_csv(r'C:\Users\bfkiw\Downloads\acc_players-2324F.csv', sep=',', skiprows=1)

print("\nACC Basketball Player Stats: ")
print(accPlayers.head(5))

totalPoints = accPlayers['PTS'].sum()
print("Total Points for All Players: " + str(totalPoints))

mostMinutes = accPlayers.Player.loc[accPlayers['MP'].idxmax()]
print("Most Minutes Played: " + str(mostMinutes))

top5rebounds = accPlayers[['Player', 'TRB']].sort_values(by='TRB', ascending=False).head(5)
print("Top 5 Rebounding Players: \n" + str(top5rebounds))

playersOver1000 = accPlayers[accPlayers['MP'] > 1000]

mostAssists = playersOver1000.Player.loc[playersOver1000['AST'].idxmax()]
print("Player with Most Assists and Over 1000 Minutes Played: " + str(mostAssists))

top3Assists = playersOver1000[['Player', 'AST']].sort_values(by='AST', ascending=False).head(3)
print("Top 3 Assisting Players: \n" + str(top3Assists))

top3Blocks = playersOver1000[['Player', 'BLK']].sort_values(by='BLK', ascending=False).head(3)
print("Top 3 Blocking Players: \n" + str(top3Blocks))

totalPointsBySchool = accPlayers.groupby('School')['PTS'].sum()
print("Total Points by School:\n", totalPointsBySchool)

totalAssistsBySchool = accPlayers.groupby('School')['AST'].sum()
print("Total Assists by School:\n", totalAssistsBySchool)

top3Schools = accPlayers[['School', 'PTS']].sort_values(by='PTS', ascending=False).head(3)
print("Top 3 Scoring Schools: \n" + str(top3Schools))
