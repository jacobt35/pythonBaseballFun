 # Find Clayton Kershaw's player id
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
kershawData = playerid_lookup('kershaw', 'clayton')
# print(kershawData.to_string())
whatIs = kershawData.loc[0, ["key_mlbam", "name_last"]]
# object indexed with column values cool!
#print(whatIs.key_mlbam)

verlander = playerid_lookup('verlander', 'justin')
vID = verlander.loc[0, 'key_mlbam']
print(vID)
verlander_df = statcast_pitcher(start_dt="")