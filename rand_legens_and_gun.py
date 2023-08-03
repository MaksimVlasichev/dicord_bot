import os
import random

def rand_gun():
    gun = {
        'Havoc': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/b/b8/Obsidian_Night_Havoc.png/revision/latest/scale-to-width-down/1000?cb=20221102074056',
        'Flatline': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/49/Heat_Sink_Flatline.png/revision/latest/scale-to-width-down/1000?cb=20220528170903',
        'Red_Hemlok': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/e7/Scream_Machine_Hemlok.png/revision/latest/scale-to-width-down/1000?cb=20220411134333',
        'R-301': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/3e/Exposed_Wiring_R-301.png/revision/latest/scale-to-width-down/1000?cb=20211122012732',
        'Nemesis': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/b/b9/The_Cleaner_Nemesis.png/revision/latest/scale-to-width-down/1000?cb=20230621125315',
        'Alternator': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/3c/Amped_Up_Alternator_SMG.png/revision/latest/scale-to-width-down/1000?cb=20220519205608',
        'Prowler': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/cf/Wrath_Bringer_Prowler.png/revision/latest/scale-to-width-down/1000?cb=20210805052609',
        'R-99': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/37/Cutting_Edge_R-99.png/revision/latest/scale-to-width-down/1000?cb=20220519212617',
        'Volt': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/e3/Fatal_Injection_Volt.png/revision/latest/scale-to-width-down/1000?cb=20211012112245',
        'CAR': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/6/6a/Wyrmborn_CAR.png/revision/latest/scale-to-width-down/1000?cb=20220514100542',
        'Devotion': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/41/Arctic_Calibration_Devotion.png/revision/latest/scale-to-width-down/1000?cb=20220920215657',
        'Red_L-STAR': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/c6/Road_Rash_L-STAR.png/revision/latest/scale-to-width-down/1000?cb=20220525191347',
        'M600_Spitfire': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/3b/Molten_Soul_Spitfire.png/revision/latest/scale-to-width-down/1000?cb=20220512143555',
        'Rampage': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/1/11/Secondary_Jaw_Rampage.png/revision/latest/scale-to-width-down/1000?cb=20220920215703',
        'G7_Scout': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/6/6f/The_Blue_Dragon_G7_Scout.png/revision/latest/scale-to-width-down/1000?cb=20220320030806',
        'Triple_Take': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/3d/Prime_Precision_Triple_Take.png/revision/latest/scale-to-width-down/1000?cb=20210928114220',
        '30-30_Repeater': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/e6/Dose_of_Madness_30-30_Repeater.png/revision/latest/scale-to-width-down/1000?cb=20220403153953',
        'Red_Bocek': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/0/08/Aurora_Arrow_Bocek.png/revision/latest?cb=20220317180744',
        'Charge_Rifle': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/3f/Cosmic_Cannon_Charge_Rifle.png/revision/latest/scale-to-width-down/1000?cb=20221102074235',
        'Longbow': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/b/ba/Runic_Ritual_Longbow.png/revision/latest/scale-to-width-down/1000?cb=20230114120846',
        'Red_Kraber': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/d/d6/Wasteland_Finery_Kraber.png/revision/latest/scale-to-width-down/1000?cb=20210805110359',
        'Sentinel': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/5c/Ethereal_Expectations_Sentinel.png/revision/latest/scale-to-width-down/1000?cb=20211002152704',
        'EVA': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/c7/Soul_Ripper_EVA-8.png/revision/latest/scale-to-width-down/1000?cb=20230126111452',
        'Mastiff': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/b/b6/Afterparty_Mastiff.png/revision/latest/scale-to-width-down/1000?cb=20230215185456',
        'Mozambique': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/9/98/Norse_Code_Mozambique.png/revision/latest/scale-to-width-down/1000?cb=20210805073557',
        'Peacekeeper': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/8f/Frostbite_Peacekeeper.png/revision/latest/scale-to-width-down/1000?cb=20220517153918',
        'RE-45': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/c2/The_Blue_Beast_RE-45.png/revision/latest?cb=20220320034751',
        'P2020': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/ff/Pit_Viper_P2020.png/revision/latest/scale-to-width-down/1000?cb=20210701000434',
        'Wingman': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/f/fa/Cardinal_Force_Wingman.png/revision/latest/scale-to-width-down/1000?cb=20220621213010'
    }
    
    name_gun1, url_gun1 = random.choice(list(gun.items()))
    name_gun2, url_gun2 = random.choice(list(gun.items()))
    name_gun3, url_gun3 = random.choice(list(gun.items()))
    guns = [name_gun1,name_gun2,name_gun3]
    k = 0
    for i in range(len(guns)):
        if "Red" in guns[i]:
            k+=1
            if k == 3:
                k = "Ахахахаха, сходи лотерейный билетик купи"
     

    ArrGun = [name_gun1, url_gun1, name_gun2, url_gun2, name_gun3, url_gun3, k]
    return ArrGun

def rand_leg():
    legend = {
        'Bangalore': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/1/10/Radical_Action_Bangalore.png/revision/latest?cb=20211125212812',
        'Revenant': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/1/1c/Predatory_Instinct_Revenant.png/revision/latest?cb=20210817191539',
        'Fuse': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/2/2a/Cybernetic_Payload_Fuse.png/revision/latest?cb=20211002143501',
        'Ash': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/7/79/Chain_of_Command_Ash.png/revision/latest?cb=20211110153714',
        'Maggie': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/7/76/Necro-Smasher_Maggie.png/revision/latest?cb=20230110214707',
        'Ballistic': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/9/9a/Vice_Grip_Ballistic.png/revision/latest?cb=20230512185006',
        'Pathfinder': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/44/Full_Throttle_Pathfinder.png/revision/latest?cb=20220120213138',
        'Wrath': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/58/Apex_Voidshifter_Wraith_Tier_3.png/revision/latest?cb=20221207035917',
        'Octane': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/4/4d/Biohazard_Octane.png/revision/latest?cb=20230215185842',
        'Horizon': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/a/a2/Lethal_Lass_Horizon.png/revision/latest?cb=20230621125309',
        'Valkyrie': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/6/69/Sky_Sentinel_Valkyrie.png/revision/latest?cb=20230503202102',
        'Bloodhound': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/9/91/Apex_Hunter_Bloodhound_Tier_3.png/revision/latest?cb=20220310114750',
        'Crypto': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/82/Machine_Language_Crypto.png/revision/latest?cb=20220504002811',
        'Seer': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/32/Aces_High_Seer.png/revision/latest?cb=20220222192737',
        'Vantage': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/3f/Nocturnal_Tactics_Vantage.png/revision/latest?cb=20220809215816',
        'Gibraltar': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/1/1f/Golden_Guardian_Gibraltar.png/revision/latest?cb=20220220144854',
        'Lifeline': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/e/e8/Hell_Raiser_Lifeline.png/revision/latest?cb=20210710011158',
        'Mirage': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/5/50/Marked_Man_Mirage.png/revision/latest?cb=20220621212729',
        'Loba': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/a/af/Trouble_in_Paradise_Loba.png/revision/latest?cb=20230401171245',
        'Newcastle': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/7/71/Mane_Event_Newcastle.png/revision/latest?cb=20221107064107',
        'Caustic': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/8/86/Apex_Contagion_Caustic_Tier_3%282%29.png/revision/latest/scale-to-width-down/1000?cb=20230425203800',
        'Wattson': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/3/34/Thunder_Kitty_Wattson.png/revision/latest?cb=20220221173756',
        'Rampart': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/1/1f/Sly_Fox_Rampart.png/revision/latest?cb=20220330000902',
        'Catalyst': 'https://static.wikia.nocookie.net/apexlegends_gamepedia_en/images/c/c0/Celestial_Protector_Catalyst.png/revision/latest?cb=20221101203306'
    }
    name_leg1, url_leg1 = random.choice(list(legend.items()))
    heroes = []
    heroes.append(name_leg1 + "," + url_leg1)
    while len(heroes)< 3:
        name_leg1, url_leg1 = random.choice(list(legend.items()))
        for i in range(len(heroes)):
            if name_leg1 in heroes[i]:
                
                break
            else:
                heroes.append(name_leg1 + "," + url_leg1)
        continue
    return [heroes[0].split(",")[0],heroes[0].split(",")[1],heroes[1].split(",")[0],heroes[1].split(",")[1],heroes[2].split(",")[0], heroes[2].split(",")[1]]
