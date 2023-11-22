import random
#input the number of groups and the number of teams
while True:
	total_groups=input('enter number of groups')
	total_teams=input('enter number of teams')
	total_groups=int(total_groups)
	total_teams=int(total_teams)
	if total_teams%total_groups==0:
		print('all set')
		break
	else:
		print('the number of teams must be divisible by groups')
		continue
#input the teams and groups
teams=[]
print('Enter "q" when you complete entering the number of teams')

while True:
	team_n=input('enter the team names: ')
	teams.append(team_n)
	if team_n== 'q':
		teams.remove('q')
		break
	
if len(teams) > total_teams:
	print('you have entered many teams')
elif len(teams) < total_teams:
	print('you have entered  few teams')
else:
	print('all set') 
	
groups=[]

print('Enter "q" when you complete entering the number of teams')
while True:
	group_n=input('enter the group names: ')
	groups.append(group_n)
	if group_n== 'q':
		groups.remove('q')
		break
	
if len(groups) > total_groups:
	print('you have entered many teams')
elif len(groups) < total_groups:
	print('you have entered  few teams')
else:
	print('all set')           
            
#shuffle the teams randomly
team=random.shuffle(teams)

#write a function to split the teams into equal parts
def split(teams, tpg):
    for i in range(0, len(teams), tpg):
        yield teams[i:i + tpg]
        
#define the number of teams needed per group        
tpg=int(total_teams/total_groups)

new_teams=(list(split(teams, tpg)))

#add the splitted teams to the groups
s_groups={}
for group in groups:
    for new_team in new_teams:
        s_groups[group]= new_team
        new_teams.remove(new_team)
        break
print('\nThese are the scheduled groups' + '\n' + str(s_groups))
