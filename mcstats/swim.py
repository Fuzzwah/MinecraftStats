from mcstats import __mcstats__

__mcstats__.registry.append(
    __mcstats__.MinecraftStat(
        'swim',
        {
            'title': 'Swimmer',
            'desc': 'Distance swum',
            'unit': 'cm',
        },
        __mcstats__.StatReader(['minecraft:custom','minecraft:swim_one_cm'])
    ))
