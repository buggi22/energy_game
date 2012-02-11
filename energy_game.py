import marshal
import random
import traceback
import itertools

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
    add_city(game, "Minneapolis",1,1),
    add_city(game, "Saint Paul",2,2),
    add_city(game, "San Francisco",1,2)
    add_city(game, "San Diego",1,2)
    add_city(game, "Los Angeles",1,2)
    add_city(game, "Portland",1,2)
    add_city(game, "Seattle",1,2)
    add_city(game, "Boise",1,2)
    add_city(game, "Cheyenne",1,2)
    add_city(game, "Saint Louis",1,2)
    add_city(game, "Chicago",1,2)
    add_city(game, "New York",1,2)
    add_city(game, "Charlotte",1,2)
    add_city(game, "Washington, D.C.",1,2)
    add_city(game, "Miami",1,2)
    add_city(game, "Memphis",1,2)
    add_city(game, "New Orleans",1,2)
    add_city(game, "Louisville",1,2)
    add_city(game, "Atlanta",1,2)
    add_city(game, "Phoenix",1,2)
    add_city(game, "Houston",1,2)
    add_city(game, "Austin",1,2)
    add_city(game, "Dallas",1,2)
    add_city(game, "Fargo",1,2)
    add_city(game, "Albuquerque",1,2)
    add_city(game, "Santa Fe",1,2)
    add_city(game, "Denver",1,2)
    add_city(game, "Detroit",1,2)
    add_city(game, "Boston",1,2)
    add_city(game, "Cincinatti",1,2)

    game['city_connection_matrix'] = make_connection_matrix(game, [
        ("Minneapolis", "Saint Paul", 0),
        ("Los Angeles", "San Francisco", 15),
        ("Los Angeles", "San Diego", 15),
        ("Phoenix", "San Diego", 15),
        ("Phoenix", "Santa Fe", 15),
        ("Albuquerque", "Santa Fe", 15),
        ("Santa Fe", "Denver", 15),
        ("Santa Fe", "Austin", 15),
        ("Austin", "Dallas", 15),
        ("Austin", "Houston", 15),
        ("Dallas", "Houston", 15),
        ("New Orleans", "Houston", 15),
        ("New Orleans", "Memphis", 15),
        ("Portland", "San Francisco", 15),
        ("Portland", "Seattle", 15),
        ("Seattle", "Boise", 15),
        ("Portland", "Boise", 15),
        ("Boise", "Cheyenne", 15),
        ("Cheyenne", "Fargo", 15),
        ("Fargo", "Minneapolis", 15),
        ("Saint Paul", "Chicago", 15),
        ("Saint Paul", "Saint Louis", 15),
        ("Saint Louis", "Chicago", 15),
        ("Detroit", "Chicago", 15),
        ("Detroit", "Cincinatti", 15),
        ("Louisville", "Cincinatti", 15),
        ("Louisville", "Memphis", 15),
        ("Memphis", "Atlanta", 15),
        ("Memphis", "Charlotte", 15),
        ("Atlanta", "Miami", 15),
        ("Charlotte", "Washington, D.C.", 15),
        ("New York", "Washington, D.C.", 15),
        ("New York", "Boston", 15),
        ] )

def show_all_neighbors(game):
    for i in range(len(game['cities'])):
        show_neighbors_of(i, game)

def show_neighbors_of(city_index, game):
    city = game['cities'][city_index]
    print "%s (city_index = %d) has the following neighbors:" % (city['name'], city_index)

    row = game['city_connection_matrix'][city_index]

    for i, conn in enumerate(row):
        if conn != -1:
            print "  %s (%d)" % (game['cities'][i]['name'], conn)

def make_connection_matrix(game, connections):
    num_cities = len(game['cities'])
    city_names = [city['name'] for city in game['cities']]
    connection_matrix = []

    for i in range(num_cities):
        connection_matrix.append( [] )
        for j in range(num_cities):
            connection_matrix[i].append( -1 )

    for from_city, to_city, cost in connections:
        from_index = city_names.index(from_city)
        to_index = city_names.index(to_city)
        connection_matrix[from_index][to_index] = cost
        connection_matrix[to_index][from_index] = cost

    return connection_matrix

def add_player(game, name, color, money):
    id = len(game['players'])
    game['players'].append( {'name': name, 'id': id, 'color': color, 'money': money, 'plants': []} )

def make_plant(initial_bid, inputs, cities_powered):
    return {'initial_bid': initial_bid, 'inputs': inputs,
            'cities_powered': cities_powered, 'resources': {}}

def add_city(game, name, position_x, position_y):
    id = len( game['cities'] )
    game['cities'].append( {'name': name, 'id': id, 'position_x': position_x, 'position_y': position_y,
            'occupants': {}} )

def game_loop(game):
    while(game['winner'] == None):
        run_game(game)

    print "Game Over.  Winner is %s" % game['players'][ game['winner'] ]

def print_game(game):
    for k, v in game.items():
        if(isinstance(v, list)):
            print k + ':\n\t' + '\n\t'.join([str(x) for x in v])
        else:
            print str(k) + ':\n\t' + str(v)

def run_game(game):
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
        replenish_resources(game)
    elif game['phase'] == 7:
        update_power_plants(game)
    else:
        raise Exception("Unrecognized phase: %s" % str(game['phase']))

    if(game['phase'] == 7):
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
        players_unordered = [(len(cities_occupied_by(i, game)), highest_plant_owned_by(p), i, p) for i,p in enumerate(game['players'])]
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
    num_plants_sold = 0

    while(len(potential_selectors_indices) > 0):
        current_selector_index = potential_selectors_indices[0]
        current_selector_name = game['players'][current_selector_index]['name']

        print "Backup plants: "
        for i, p in enumerate(game['plants_backup'] ):
            print "  %s" % (str(p))

        print "Plants for sale: " 
        for i, p in enumerate(game['plants_for_sale'] ):
            print "  %d: %s" % (i, str(p))

        selected_plant = None
        while selected_plant == None:
            selected_plant = raw_input(current_selector_name + ', select a plant or pass: ')

            if selected_plant == "pass" or selected_plant == "":
                selected_plant = "pass"

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

                    if new_bid == "pass" or new_bid == "":
                        new_bid = "pass"
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
            winning_player['plants'].append( game['plants_for_sale'][selected_plant] )
            del game['plants_for_sale'][selected_plant]
            num_plants_sold += 1
            potential_selectors_indices.remove( potential_bidders_indices[bid_winner] )

            # draw new plant
            next_plant = game['plants_in_deck'][0]

            if next_plant == 'STEP_3_BEGINS':
                game['game_step'] = 3
                del ((game['plants_for_sale'])[0])
            else:
                game['plants_backup'].append(next_plant)
                game['plants_backup'].sort( key = lambda plant: plant['initial_bid'] )
            
            game['plants_in_deck'].remove(next_plant)

            # shift plant(s) down from "backup" position
            if game['game_step'] == 3:
                game['plants_for_sale'].extend(game['plants_backup'])
                game['plants_backup'] = []
            else:
                game['plants_for_sale'].append( game['plants_backup'][0] )
                del ((game['plants_backup'])[0])
                
            game['plants_for_sale'].sort( key = lambda plant: plant['initial_bid'] )

    # in first round, redetermine player order based on results of first auction
    if(game['round_number'] == 0):
        determine_order(game)

def buy_resources(game):
    print "Resource-buying phase (player order reversed)"

    # NOTE: this phase is played in reverse order
    reverse_order = [game['players'][i] for i in reversed( game['player_order'] ) ]

    for p in reverse_order:
        buy_resources_single_player(game, p)

def buy_resources_single_player(game, p):
    print "%s, it is your turn to buy resources" % p['name']

    # get unique resource names
    resource_names = sorted(list(set( [r['resource'] for r in game['resources_for_sale'] ] )))

    # print availability of resources
    resource_groups = itertools.groupby(game['resources_for_sale'], key = lambda r: r['resource'])
    prices = {}
    for resource_name, entries in resource_groups:
        available = [x for x in entries if x['quantity'] > 0]
        available.sort(key=lambda r: r['price'])

        cumulative_price = 0
        cumulative_count = 0
        price_map = {}

        for a in available:
            for i in range(a['quantity']):
                cumulative_price += a['price']
                cumulative_count += 1
                price_map[cumulative_count] = cumulative_price

        if len(price_map) > 0:
            prices[resource_name] = price_map

    if len(prices) == 0:
        print "No resources of any kind available to purchase"
        raw_input("Press Enter to continue. ")
        return

    for resource_name, price_map in prices.items():
        if len(price_map) <= 0: 
            print "No %s available to purchase"
            continue

        print "Prices for %s:" % resource_name
        for count, price in price_map.items():
            print "  %5d: total price = %5d" % (count, price)

        amount = None
        while amount == None: 
            amount = raw_input(p['name'] + ', how much ' + resource_name + ' would you like to buy? ')

            if amount == "" or amount == "0":
                amount = 0
                break

            try:
                amount = int(amount)
            except:
                print "Amount must be a number"
                amount = None
                continue

            cost = price_map.get(amount)

            if cost == None:
                print "Requested quantity is not available"
                amount = None
                continue

            if p['money'] < cost:
                print "You do not have enough money for that purchase"
                amount = None
                continue

            # make sure player's plants have enough capacity to hold the requested amount

            plants_accepting_resource = [plant for plant in p['plants'] if resource_name in plant['inputs']]
            max_purchase = 0

            valid_destinations = []

            for plant in plants_accepting_resource:
                current_stock = sum( [ plant['resources'].get(r, 0) for r in resource_names ] )
                capacity = 2*plant['inputs'].get(resource_name, 0)
                availability = capacity - current_stock
                if availability > 0:
                    valid_destinations.append((plant,availability))
                max_purchase += availability

            if amount > max_purchase:
                print "Your plants do not have enough capacity for that purchase"
                amount = None
                continue

        if amount <= 0:
            continue

        print "Purchasing %d units of %s.  Cost = %d" % (amount, resource_name, cost)
        
        # pay for the transaction and reduce supplies
        total_cost = 0
        amount_to_purchase = amount
        while amount_to_purchase > 0:
            best_price_entry = min([r for r in game['resources_for_sale'] if \
                    r['quantity'] > 0 and r['resource'] == resource_name], key=lambda r: r['price'])
            print "DEBUGGING: best_price_entry = %s" % str(best_price_entry)
            amount_to_purchase -= 1
            best_price_entry['quantity'] -= 1
            p['money'] -= best_price_entry['price']
            total_cost += best_price_entry['price']

        assert(cost == total_cost)

        # decide how to assign resources to plants
        # if there is any ambiguity, let the player choose which plant to assign the resources to
        possible_divisions = get_possible_divisions(amount, valid_destinations)

        assert len(possible_divisions) > 0

        if len(possible_divisions) == 1:
            division = possible_divisions[0]
        else:
            division = None

            print "Possible divisions:"
            for i, div in enumerate(possible_divisions):
                print "  %d:" % i
                for dest_plant, transfer_amount in division:
                    print "    %d %s to %s" % (transfer_amount, resource_name, str(dest_plant))

        while division == None:
            division = raw_input(p['name'] + ', select a division of resources from the above list: ')

            try:
                division = int(division)
            except:
                print "Selection must be a number"
                division = None
                continue

            if division < 0 or division >= len(possible_divisions):
                print "Selection must be in the valid range"
                division = None
                continue

            division = possible_divisions[division]

        # actually assign the resources to plants, according to the chosen scheme
        print "Assigning resources:"
        for dest_plant, transfer_amount in division:
            print "    %d %s to %s" % (transfer_amount, resource_name, str(dest_plant))
            if not(resource_name in dest_plant['resources']):
                dest_plant['resources'][resource_name] = 0
            dest_plant['resources'][resource_name] += transfer_amount

def get_possible_divisions(amount, destinations):
    (first_plant, first_availability) = destinations[0]

    if len(destinations) == 0:
        return []
    elif len(destinations) == 1:
        if first_availability < amount:
            return []
        else:
            return [ [ (first_plant, amount) ] ]

    divisions = []

    for i in range( min(first_availability, amount) + 1 ):
        divisions += [ [(first_plant, i)] + div for div in get_possible_divisions(amount - i, destinations[1:]) ]

    return divisions

def build_cities(game):
    print "City-building phase (player order reversed)"

    # NOTE: this phase is played in reverse order
    reverse_order = [game['players'][i] for i in reversed( game['player_order'] ) ]

    for p in reverse_order:
        print "%s's turn to build cities" % p['name']
        keep_building = True
        while keep_building:
            available = available_cities_to_build(game, p)

            if len(available) == 0:
                print "No available cities"
                keep_building = False
                break

            print "Available cities: "
            for i, a in enumerate(available):
                print "  %d: %s" % (i, a['name'])

            build_choice = raw_input(p['name'] + ', build a city or pass: ')

            if build_choice == 'pass' or build_choice == '':
                keep_building = False
                break

            try:
                build_choice = int(build_choice)
            except:
                print "Could not parse selection.  Passing instead."
                keep_building = False
                break

            if build_choice < 0 or build_choice >= len(available):
                print "Selection was not in valid range.  Passing instead."
                keep_building = False
                break

            cost = 10
            # TODO: fix the cost calculation to incorporate the cheapest possible connection

            if cost > p['money']:
                print "Not enough money.  Passing instead."
                keep_building = False
                break

            # occupy the city
            city = available[build_choice]
            city['occupants'][10] = p['id']

            # pay for construction
            p['money'] -= cost

            print "Built a city at %s for a price of %d" % (city['name'], cost)


def available_cities_to_build(game, p):
    cities_occupied = cities_occupied_by(p['id'], game)

    # a player's first city can be in any unoccupied spot
    if len(cities_occupied) == 0:
        return [city for city in game['cities'] if len(city['occupants']) == 0 ]

    # for later cities...
    # find the connected component (there can only be one) to which the player's cities belong
    #   NOTE: "connected" in the sense of having a path via player's own cities or opponents' cities
    first_city_id = cities_occupied[0]['id']
    component = connected_component_starting_at( first_city_id, game )

    # then, find all unoccupied cities one step away from the connected component
    available = []
    for c in component:
        row = game['city_connection_matrix'][c]
        for i, conn in enumerate(row):
            city = game['cities'][i]
            if conn != -1 and len(city['occupants']) == 0 and not(i in available):
                #TODO: update this condition for later stages
                available.append(i)

    return [game['cities'][i] for i in available]

def burn_resources(game):
    print "Resource-burning phase (player order reversed)"

    # NOTE: this phase is played in reverse order
    reverse_order = [game['players'][i] for i in reversed( game['player_order'] ) ]

    winner_candidates = []

    for p in reverse_order:
        print "%s's turn to burn resources" % p['name']

        ready = plants_ready_to_burn(p)

        if len(ready) == 0:
            print "No plants ready to burn"
            continue

        print "Plants ready to burn:"
        for i, (plant, options) in enumerate(ready):
            print "  %d: %s" % (i, str(plant))
            for j, resource_name in enumerate(options):
                if resource_name == None:
                    print "    %d: free burn to power up to %d cities" % (j, plant['cities_powered'])
                else:
                    print "    %d: burn %d %s to power up to %d cities" % (j, plant['inputs'][resource_name], resource_name, plant['cities_powered'])

        raw_input(p['name'] + ', press Enter to burn resources. ')

        # TODO: allow player to choose to burn a subset of resources, and to choose between multiple options (when available) for hybrid plants

        powered_cities = 0
        unpowered_cities = len(cities_occupied_by(p['id'], game)) 
        for plant, options in ready:
            chosen_option = options[0]
            cities_to_power = min(unpowered_cities, plant['cities_powered'])
            powered_cities += cities_to_power
            unpowered_cities -= cities_to_power

            if chosen_option == None:
                print "Free burn to power %d cities" % cities_to_power
            else:
                amount = plant['inputs'][chosen_option]
                print "Burning %d %s to power %d cities" % (amount, chosen_option, cities_to_power)
                plant['resources'][chosen_option] -= amount
                if plant['resources'][chosen_option] == 0:
                    del plant['resources'][chosen_option]

        income = get_income_for(powered_cities)
        p['money'] += income

        print "Total of %d cities powered, for an income of %d" % (powered_cities, income)

        if powered_cities > 20:
            winner_candidates.append(p)

    # TODO: decide a unique winner
    if len(winner_candidates) > 0:
        game['winner'] = winner_candidates[0]['id']

def get_income_for(powered_cities):
    max_income = 100
    income_map = {0: 10, 1: 20, 2: 30, 3: 39, 4: 48, 5: 56, 6: 63, 7: 70, 8: 76, 9: 82, 10: 87, 11: 92, 12: 96, 13: 100}
    return income_map.get(powered_cities, max_income)

def plants_ready_to_burn(p):
    ready = []
    for plant in p['plants']:
        if len(plant['inputs']) == 0:
            ready.append( (plant, [None]) )
        else:
            options = []
            for resource_name, resource_needed in plant['inputs'].items():
                if plant['resources'].get(resource_name, 0) >= resource_needed:
                    options.append( resource_name )
            if len(options) > 0:
                ready.append( (plant, options) )
    return ready

def replenish_resources(game):
    print "Replenish resources phase"
    raw_input("Press Enter to continue. ")
    # TODO: implement this phase

def update_power_plants(game):
    print "Plant update phase"
    raw_input("Press Enter to continue. ")
    # TODO: implement this phase

def connected_component_starting_at(city_index, game):
    def helper(game, found_so_far):
        extras = []
        
        for f in found_so_far:
            row = game['city_connection_matrix'][f]
            for i, conn in enumerate(row):
                city = game['cities'][i]
                if conn != -1 and len(city['occupants']) > 0 and not(i in found_so_far) and not(i in extras):
                    extras.append(i)
        
        if len(extras) == 0:
            return found_so_far
        else:
            return helper(game, found_so_far + extras)

    return helper(game, [city_index])

def cities_occupied_by(player_index, game):
    result = []
    for city in game['cities']:
        for value, occupant in city['occupants'].items():
            if occupant == player_index:
                result.append(city)
    return result

def highest_plant_owned_by(player):
    if len(player['plants']) == 0:
        return -1
    else:
        return max( [plant['initial_bid'] for plant in player['plants']] )

def test():
    test_game = make_blank_game()

    setup_deck(test_game)
    setup_resources(test_game)
    setup_cities(test_game)

    add_player(test_game, "player A", "FF0000", 200),
    add_player(test_game, "player B", "00FF00", 200),
    add_player(test_game, "player C", "0000FF", 200)

    show_all_neighbors(test_game)

    try:
        game_loop( test_game )
    except Exception, e:
        print_game(test_game)
        traceback.print_exc()

if __name__ == '__main__':
    test()





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
