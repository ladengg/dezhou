

#build a player, which is a neural network


while 1:
	game_num += 1
	player_state = []
	for idx in range(0, 6):
		#initial money is random
		#initial active state is random
		game_state = GameState()
		player_state.append(game_state)
	cards = np.zeros(1, 52)

	#initial: two cards
	#distribute the cards
	for idx in range(0, 6):
		if(player_state[idx].IsActive()):
			card_idx = get_card(cards)
			player_state.cards.append(card_idx)
			cards[card_idx] = 1
	#allocate the boss
	boss_idx = 0
	while 1:
		boss_idx = int(rand() * 6)
		if(player_state[boss_idx].IsActive()):
			break
	#from the next of the boss is the small bb and big bb
	#then is the player who begins the bets/follow/giveup
	#every player will decide the actions until the first round is finished
	while 1:
		#the (boss_idx+2)%6
		raise_flag = 0
		for idx in range(0, 6):
			cur_player_idx = (boss_idx+idx+2)%6
			valid_actions = GetValidAction()
			pred = s.run()
			act = GetAction(valid_actions, pred, player_state[cur_player_idx])
			player_state[cur_player_idx] = GetPlayerState(act)
			if(is_raise(act)):
				raise_flag = 1
		if(raise_flag == 0):	#no raise
			break
	
	#second: three cards
	get_card(cards)
	get_card(cards)
	get_card(cards)
	while 1:
		#the (boss_idx+2)%6
		raise_flag = 0
		for idx in range(0, 6):
			cur_player_idx = (boss_idx+idx+2)%6
			valid_actions = GetValidAction()
			pred = s.run()
			act = GetAction(valid_actions, pred, player_state[cur_player_idx])
			player_state[cur_player_idx] = GetPlayerState(act)
			if(is_raise(act)):
				raise_flag = 1
		if(raise_flag == 0):	#no raise
			break

	
	#third: one card
	get_card(cards)
	while 1:
		#the (boss_idx+2)%6
		raise_flag = 0
		for idx in range(0, 6):
			cur_player_idx = (boss_idx+idx+2)%6
			valid_actions = GetValidAction()
			pred = s.run()
			act = GetAction(valid_actions, pred, player_state[cur_player_idx])
			player_state[cur_player_idx] = GetPlayerState(act)
			if(is_raise(act)):
				raise_flag = 1
		if(raise_flag == 0):	#no raise
			break



	#fourth: one card
	get_card(cards)
	while 1:
		#the (boss_idx+2)%6
		raise_flag = 0
		for idx in range(0, 6):
			cur_player_idx = (boss_idx+idx+2)%6
			valid_actions = GetValidAction()
			pred = s.run()
			act = GetAction(valid_actions, pred, player_state[cur_player_idx])
			player_state[cur_player_idx] = GetPlayerState(act)
			if(is_raise(act)):
				raise_flag = 1
		if(raise_flag == 0):	#no raise
			break

	#decide the winner
	win_idx = GetWinner()
	for idx in range(0, 6):
		player_state[idx].UpdatePlayerState(win_idx)
	
	#for each player, get the optimal action under the given state, with the final result known
	for player_idx, state in StateSequence:
		act = GetOptimalAction()
		s.run(opt, feed_dict = {state, act})
	



	
	
