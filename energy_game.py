import marshal
import random
import traceback

def make_blank_game():
    initial_game = {
        'game_step': 1,
        'round_number': 0,
        'phase': 1,
        #'phase_status': None,
        'players': [],
        'player_order': None,
        'resources_for_sale': [],
        'resources_backup': [],
        'plants_for_sale': [],
        'plants_backup': [],
        'plants_in_deck': [],
        'discarded_plants': [],
        'cities': [],
        'city_connection_matrix': [],
        'winner': None,
        #'history': []
        }

    return initial_game

def setup_deck(game):
    game['plants_for_sale'] = [
            make_plant(1, {'Oil': 1}, 1),
            make_plant(2, {'Coal': 1}, 1),
            make_plant(3, {'Coal': 1, 'Oil': 1}, 1),
            make_plant(4, {'Garbage': 1}, 3)
            ]
    game['plants_backup'] = [
            make_plant(5, {'Oil': 1}, 2),
            make_plant(6, {'Coal': 1}, 2),
            make_plant(7, {'Coal': 1, 'Oil': 1}, 2),
            make_plant(8, {'Garbage': 1}, 6)
            ]

    remaining_plants = [
            make_plant(10, {'Coal': 1, 'Oil': 1}, 4),
            make_plant(11, {}, 2),
            make_plant(12, {'Uranium': 1}, 6),
            make_plant(13, {'Oil': 1}, 6),
            make_plant(14, {'Coal': 1}, 6),
            make_plant(15, {'Uranium': 1}, 8),
            make_plant(16, {}, 6),
            ]
    random.shuffle(remaining_plants)

    remaining_plants = [make_plant(9, {}, 1)] + remaining_plants + ['STEP_3_BEGINS']

    game['plants_in_deck'] = remaining_plants

def setup_resources(game):
    game['resources_for_sale'] = [
            {'resource': 'Coal', 'price': 1, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 2, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 3, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 4, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 5, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 6, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 7, 'capacity': 3, 'quantity': 3},
            {'resource': 'Coal', 'price': 8, 'capacity': 3, 'quantity': 3},
            {'resource': 'Oil', 'price': 1, 'capacity': 3, 'quantity': 0},
            {'resource': 'Oil', 'price': 2, 'capacity': 3, 'quantity': 0},
            {'resource': 'Oil', 'price': 3, 'capacity': 3, 'quantity': 3},
            {'resource': 'Oil', 'price': 4, 'capacity': 3, 'quantity': 3},
            {'resource': 'Oil', 'price': 5, 'capacity': 3, 'quantity': 3},
            {'resource': 'Oil', 'price': 6, 'capacity': 3, 'quantity': 3},
            {'resource': 'Oil', 'price': 7, 'capacity': 3, 'quantity': 3},
            {'resource': 'Oil', 'price': 8, 'capacity': 3, 'quantity': 3},
            {'resource': 'Garbage', 'price': 1, 'capacity': 3, 'quantity': 0},
            {'resource': 'Garbage', 'price': 2, 'capacity': 3, 'quantity': 0},
            {'resource': 'Garbage', 'price': 3, 'capacity': 3, 'quantity': 0},
            {'resource': 'Garbage', 'price': 4, 'capacity': 3, 'quantity': 0},
            {'resource': 'Garbage', 'price': 5, 'capacity': 3, 'quantity': 0},
            {'resource': 'Garbage', 'price': 6, 'capacity': 3, 'quantity': 0},
            {'resource': 'Garbage', 'price': 7, 'capacity': 3, 'quantity': 3},
            {'resource': 'Garbage', 'price': 8, 'capacity': 3, 'quantity': 3},
            {'resource': 'Uranium', 'price': 1, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 2, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 3, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 4, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 5, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 6, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 7, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 8, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 10, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 12, 'capacity': 1, 'quantity': 0},
            {'resource': 'Uranium', 'price': 14, 'capacity': 1, 'quantity': 1},
            {'resource': 'Uranium', 'price': 16, 'capacity': 1, 'quantity': 1}
            ]
    game['resources_backup'] = {
        'Coal': 10,
        'Oil': 10,
        'Garbage': 10,
        'Uranium': 10
        }

def setup_cities(game):
    game['cities'] = [
            make_city("Minneapolis",1,1),
            make_city("Saint Paul",2,2),
            make_city("San Francisco",1,2)
            ]
    game['city_connection_matrix'] = [
            [-1,0,15],
            [0,-1,-1],
            [15,-1,-1]
            ]
    
def make_player(name, color, money):
    return {'name': name, 'color': color, 'money': money, 'plants': []}

def make_plant(initial_bid, inputs, cities_powered):
    return {'initial_bid': initial_bid, 'inputs': inputs,
            'cities_powered': cities_powered, 'resources': {}}

def make_city(name, position_x, position_y):
    return {'name': name, 'position_x': position_x, 'position_y': position_y,
            'occupants': {}}

def game_loop(game):
    while(game['winner'] == None):
        run_game(game)

def print_game(game):
    for k, v in game.items():
        if(isinstance(v, list)):
            print k + ':\n\t' + '\n\t'.join([str(x) for x in v])
        else:
            print str(k) + ':\n\t' + str(v)

def run_game(game):
    #print_game(game)    # just for debugging

    if game['phase'] == 1:
        determine_order(game)
    elif game['phase'] == 2:
        auction_plants(game)
    elif game['phase'] == 3:
        buy_resources(game)
    elif game['phase'] == 4:
        build_cities(game)
    elif game['phase'] == 5:
        burn_resources(game)
    elif game['phase'] == 6:
        update_power_plants(game)
    else:
        raise Exception("Unrecognized phase: %s" % str(game['phase']))

    if(game['phase'] == 6):
        game['phase'] = 1
        game['round_number'] += 1
    else:
        game['phase'] += 1

def determine_order(game):
    if(game['round_number'] == 0 and game['phase'] == 1):
        order = range(len(game['players']))
        random.shuffle(order)
        assert(len(order) > 0)
        print "Random player order assigned initially: " + ', '.join( [game['players'][i]['name'] for i in order] )
        game['player_order'] = order
    else:
        players_unordered = [(len(cities_occupied_by(i, game)), highest_plant_owned_by(p), i, p) for i,p in enumerate(players)]
        players_ordered = sorted( players_unordered )
        order = [i for (num_cities,highest_plant,i,p) in players_ordered]
        print "New player order: " + ', '.join( [game['players'][i]['name'] for i in order] )
        game['player_order'] = order
    raw_input("Press Enter to continue. ")

def auction_plants(game):
    print "Plant-auctioning phase"

    if(game['round_number'] == 0):
        allow_total_pass = False  # in the first round of the game, everyone must buy one plant
    else:
        allow_total_pass = True

    potential_selectors_indices = [] + game['player_order']

    while(len(potential_selectors_indices) > 0):
        current_selector_index = potential_selectors_indices[0]
        current_selector_name = game['players'][current_selector_index]['name']

        print "Available plants: " 
        for i, p in enumerate(game['plants_for_sale'] ):
            print "%d: %s" % (i, str(p))

        selected_plant = None
        while selected_plant == None:
            selected_plant = raw_input(current_selector_name + ', select a plant or pass: ')

            if selected_plant == "pass":
                if not(allow_total_pass):
                    print "All players must purchase a plant this round"
                    selected_plant = None
                    continue
                else:
                    break

            # make sure entry is valid
            try:
                selected_plant = int(selected_plant)
            except:
                selected_plant = None
                print "Please input a number."
                continue

            if(selected_plant < 0 or selected_plant >= len(game['plants_for_sale'])):
                print "Please selecte a valid index."
                selected_plant = None
                continue
            
            current_bid = game['plants_for_sale'][selected_plant]['initial_bid']
            print "Initial bid: " + str(current_bid)

            # make sure player has enough money
            if game['players'][current_selector_index]['money'] < current_bid:
                print "You do not have enough money to buy that plant"
                selected_plant = None
                continue
            
        if selected_plant == "pass":
            potential_selectors_indices.remove( current_selector_index )

        else:
            potential_bidders_indices = [] + potential_selectors_indices

            bid_index = 1   # start with player after the selector
            bid_winner = None

            # go through bidding process until winner has been decided
            while bid_winner == None:
                if len(potential_bidders_indices) == 1:
                    bid_winner = 0
                    break
                else:
                    print "Remaining bidders: " + ', '.join([game['players'][b]['name'] for b in potential_bidders_indices])

                current_bidder_index = potential_bidders_indices[bid_index]
                current_bidder_name = game['players'][current_bidder_index]['name']
                new_bid = None

                while new_bid == None:
                    print "Current best bid: %d" % current_bid
                    new_bid = raw_input(current_bidder_name + ', please bid on the plant or pass: ')

                    if new_bid == "pass":
                        break

                    # make sure the bid is valid
                    try:
                        new_bid = int(new_bid)
                    except:
                        print "Please bid an amount (must be a number)."
                        new_bid = None
                        continue

                    if new_bid <= current_bid:
                        print "Bid must exceed current best bid (%d)" % current_bid
                        new_bid = None
                        continue

                    # make sure the player has enough money
                    if game['players'][current_bidder_index]['money'] < new_bid:
                        print "You do not have enough money to make that bid"
                        new_bid = None
                        continue

                if new_bid == 'pass':
                    potential_bidders_indices.remove( current_bidder_index )
                else:
                    bid_index += 1
                    current_bid = new_bid

                if bid_index >= len(potential_bidders_indices):
                    bid_index = 0

            # give plant to bid winner
            winning_player = game['players'][potential_bidders_indices[bid_winner]]
            print "Bid winner: %s at a price of %d" % (winning_player['name'], current_bid)
            winning_player['money'] -= current_bid
            winning_player['plants'] += [ game['plants_for_sale'][selected_plant] ]
            del ((game['plants_for_sale'])[selected_plant])

            # TODO: shift plants down from "backup" position?  (Check rules)

            potential_selectors_indices.remove( potential_bidders_indices[bid_winner] )

    # in first round, redetermine player order based on results of first auction
    if(game['round_number'] == 0):
        determine_order(game)

def buy_resources(game):
    print "Resource-buying phase"

    # NOTE: this phase is played in reverse order
    resource_order = [game['players'][i] for i in reversed( game['player_order'] ) ]

    for p in resource_order:
        raw_input(p['name'] + ', buy resources: ')

def build_cities(game):
    print "City-building phase"

    # NOTE: this phase is played in reverse order
    resource_order = [game['players'][i] for i in reversed( game['player_order'] ) ]

    for p in resource_order:
        raw_input(p['name'] + ', build cities: ')

def burn_resources(game):
    print "Resource-burning phase"

    # NOTE: this phase is played in reverse order
    resource_order = [game['players'][i] for i in reversed( game['player_order'] ) ]

    for p in resource_order:
        raw_input(p['name'] + ', burn resources: ')

def update_power_plants(game):
    print "Plant update phase"
    raw_input("Press Enter to continue. ")

def cities_occupied_by(player_index, game):
    result = []
    for city in game['cities']:
        for value, occupant in city['occupants']:
            if occupant == player_index:
                result.append(city)
    return result

def highest_plant_owned_by(player):
    if len(player['plants']) == 0:
        return -1
    else:
        return max( [plant['initial_bid'] for plant in player['plants']] )

if __name__ == '__main__':
    test_game = make_blank_game()

    setup_deck(test_game)
    setup_resources(test_game)
    setup_cities(test_game)

    players = [
        make_player("player A", "FF0000", 100),
        make_player("player B", "00FF00", 100),
        make_player("player C", "0000FF", 100)
    ]
    test_game['players'] = players

    try:
        game_loop( test_game )
    except Exception, e:
        print_game(test_game)
        traceback.print_exc()





"""
game
    view? (public|private[player])
    game_step = 1|2|3
    turn_phase = 1 cpu determines order, 2 auction plants, 3 buy resources, 4 build cities, 5 burn resources
    phase_status? = e.g. player 1's turn to (build, select plant for auction, bid on auction); remaining auctioners
    player_order = list of indices
    players
        list of: (info, state)
            where info = name, color
                state = money, plants
                where plants = list of plant, resources
                    where resources = map of resource type, resource amount
    resources for sale
    backup resources
    plants for sale
    backup plants
    plants in deck
    discarded plants
    cities
        list of: name, location, spots occupied
            where spots_occupied = map of building cost vs (player|none)
    city_connection_matrix
        square array of (None|Connection[Amount])
    winner = player index or None
    history?
        list of: actor, modified_property, old_value, new_value
            where actor = None|Player
"""
