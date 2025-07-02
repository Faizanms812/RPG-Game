import random
def dragon():
    dragon_miss_messages = [
"🐉 The dragon rears back and breathes fire — but you roll clear of the inferno just in time!",
"🔥 The beast’s claw crashes down, but strikes only shattered stone.",
"💨 A mighty tail sweep whooshes past as you duck beneath it.",
"🌫️ The dragon’s flames erupt wildly, but you vanish into the smoke.",
"🛡️ You raise your shield as its fangs snap — metal meets nothing.",
]

    dragon_miss_message = random.choice(dragon_miss_messages)
    return dragon_miss_message

def goblin_messages__miss():
    goblin_miss_messages = [
"👺 The goblin shrieks and lunges — but trips over its own feet!\n\n",
"🗡️ It slashes wildly, missing you by a mile.\n\n",
"💨 You duck low as its jagged blade whistles overhead.\n\n",
"🤡 The goblin leaps to strike — but you sidestep and it tumbles past.\n\n",
"🪓 Its crude axe embeds in a nearby tree as you dance out of reach.\n\n",]
    miss = random.choice(goblin_miss_messages)
    return miss
    
def skeleton_messages_miss():
    skeleton_miss_messages = [
"💀 The skeleton swings its rusted blade — but it clatters against your armor harmlessly.\n\n",
"🦴 Its brittle bones creak as it lunges and misses entirely.\n\n",
"⚔️ The skeleton slashes, but your swift sidestep leaves it swinging at shadows.\n\n",
"🕸️ A hollow hiss escapes as its weapon passes through empty space.\n\n",
"💢 Its ancient limbs falter mid-swing, and you easily dodge the blow.\n\n",
]
    miss = random.choice(skeleton_miss_messages)
    return miss

def knight_messages_miss():
    knight_miss_messages = ["🗡️ You charge with valor, but your blade glances off the enemy’s armor. No damage dealt!\n\n",
"⚔️ You swing hard, but the foe sidesteps with uncanny speed.\n\n",
"🛡️ Your strike crashes down—but only meets dirt and dust.\n\n",
"🔨 You raise your weapon high, but the enemy parries just in time.\n\n",
"💨 You lunge forward, but the foe’s nimble footwork leaves you striking empty air.\n\n",]
    knight_miss_message = random.choice(knight_miss_messages)
    return knight_miss_message

def archer_messages_miss():
    archer_miss_messages = [
"🏹 You loose an arrow, swift and sharp—but it whistles past as the enemy ducks low.\n\n",
"🎯 Your shot was true—but a sudden gust throws it off course.\n\n",
"🪶 The arrow sails into the mist—your target already vanished.\n\n",
"🔦 You take aim, but your fingers slip, and the arrow falls harmlessly.\n\n",
"🕊️ Your arrow grazes a cloak—close, but not close enough.\n\n",
    ]
    archer_miss_message = random.choice(archer_miss_messages)
    return archer_miss_message

def wizard_messages_miss():
    wizard_miss_messages = [
"🔮 You conjure a bolt of fire, but the foe vanishes behind a shimmer of magical resistance.\n\n",
"💨 You unleash arcane energy, but it fizzles out before reaching the target.\n\n",
"📜 You chant the incantation—but a moment's distraction warps the spell.\n\n",
"🌩️ Lightning surges forth, but the enemy leaps clear just in time.\n\n",
"🕯️ Shadows twist around your magic, absorbing the spell before it can land.\n\n",
]
    wizard_miss = random.choice(wizard_miss_messages)
    return wizard_miss
    
def strength_buff_msgs_knight():
    knight_buff_messages = [
    "🗡️ You raise your blade to the sky — the gods of war answer with sacred power.\n\n",
    "🏇 You steel your body and charge — your next strike will be unstoppable.\n\n",
    "🛡️ With a roar, your armor glows faintly — strength and honor guide your hand.\n\n",
]
    knight_message = random.choice(knight_buff_messages)
    return knight_message

def strength_buff_msgs_wizard():
    wizard_buff_messages = [
    "🔮 You whisper ancient words — your magic now crackles with enhanced fury.\n\n",
    "📖 The arcane runes pulse — your spells grow more destructive with each beat.\n\n",
    "🌩️ You draw power from the aether — even your enemies can feel the air shift.\n\n",
]
    wizard_msg = random.choice(wizard_buff_messages)
    return wizard_msg

def strength_buff_msgs_archer():
    archer_buff_messages = [
    "🏹 You steady your breath — each shot now carries the force of a thunderclap.\n\n",
    "🎯 Your focus sharpens, your muscles coil — the next arrow will strike like a spear.\n\n",
    "🌲 Nature’s blessing fills your arms — your bow hums with lethal energy.\n\n",
]
    archer_msg = random.choice(archer_buff_messages)
    return archer_msg