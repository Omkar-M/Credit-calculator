hero_damage = 100


def double_damage():
    global hero_damage
    hero_damage = 200
    return


def disarmed():
    global hero_damage
    hero_damage *= .9
    return hero_damage


def power_potion():
    global hero_damage
    hero_damage += 100
    return hero_damage
