from pygal_maps_world.maps import World

wm = World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 3412600, 'us': 30934900, 'mx': 113423000})

wm.render_to_file('na_populations.svg')