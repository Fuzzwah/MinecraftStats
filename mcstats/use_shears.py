from mcstats import __mcstats__

__mcstats__.registry.append(
    __mcstats__.MinecraftStat(
        'use_shears',
        {
            'title': 'Cutter',
            'desc': 'Shear uses',
            'unit': 'int',
        },
        __mcstats__.StatReader(['minecraft:used','minecraft:shears'])
    ))
