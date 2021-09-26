import random

def satrt_match():
	"""" 
	probabilty matrix.
	-1 = Wicket
	1 = Single and so onn.....

	"""
	sachin = [-1,1,1,1,2,2,3,4,4,6]
	vivan = [-1,1,2,2,3,3,4,4,6,6]

	batsman = [sachin, vivan]
	striker = 0
	balls = ['First', 'Second', 'Third', 'Fourth',
	'Fifth', 'Sixth']

	for ball in balls:
		cur_bat = batsman[striker]
		batsman_name = "Vivan" if striker else "Sachin"
		res = random.choice(cur_bat)
		if res == -1:
			commentry = f"{ball} ball of the over, {batsman_name} at strike. He got out. Khel khatam pisa hajam. Are nahi ye to trial ball thi na?? Ooh no."
			print(commentry)
			break
		elif res in [1,3]:
			striker = 0 if striker else 1
			commentry = f"{ball} ball of the over, {batsman_name} at strike. He plays it for {res}. IPL hota to 6 marta."
		elif res == 2:
			commentry = f"{ball} ball of the over, {batsman_name} at strike. He plays it for Two. Ye banda strike nahi dega. Pura daam le kar chodega"
		elif res in [4, 6]:
			commentry = f"{ball} ball of the over, {batsman_name} at strike. He plays it for {res}. {batsman_name} jab khelte hai to darshak fielder ban jate hai."
		print(commentry)

if __name__ == "__main__":
	satrt_match()
