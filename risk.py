# Python file for calculating the odds of winning a game of Risk

from dataclasses import dataclass, field


@dataclass
class AttackRoll:
    rolls: list = field(default_factory=list)
    probability_of_roll: float = 0.0
    probability_of_defender_loses_0: float = 0.0
    probability_of_defender_loses_1: float = 0.0
    probability_of_defender_loses_2: float = 0.0
    probability_of_defender_loses_against_one_dice: float = 0.0


attack_rolls = {(1, 1): AttackRoll(),
                (1, 2): AttackRoll(),
                (1, 3): AttackRoll(),
                (1, 4): AttackRoll(),
                (1, 5): AttackRoll(),
                (1, 6): AttackRoll(),
                (2, 2): AttackRoll(),
                (2, 3): AttackRoll(),
                (3, 3): AttackRoll(),
                (2, 4): AttackRoll(),
                (2, 5): AttackRoll(),
                (3, 4): AttackRoll(),
                (2, 6): AttackRoll(),
                (4, 4): AttackRoll(),
                (3, 5): AttackRoll(),
                (3, 6): AttackRoll(),
                (4, 5): AttackRoll(),
                (5, 5): AttackRoll(),
                (4, 6): AttackRoll(),
                (5, 6): AttackRoll(),
                (6, 6): AttackRoll(),
                }

# Define all possible rolls
defense_rolls = [[i, j] for i in range(1, 7) for j in range(1, 7)]
attack_rolls_all = [[i, j, k] for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]

for i, roll in enumerate(defense_rolls):
    roll.sort(reverse=True)

for i, roll in enumerate(attack_rolls_all):
    roll.sort(reverse=True)

# Count attack rolls and calculate probabilities
for i, roll in enumerate(attack_rolls_all):
    attack_dice_high = roll[0]
    attack_dice_low = roll[1]
    attack_rolls[(attack_dice_low, attack_dice_high)].rolls.append(roll)

for i, roll in enumerate(attack_rolls):
    probability = len(attack_rolls[roll].rolls) / len(attack_rolls_all) * 100
    attack_rolls[roll].probability_of_roll = probability


# Calculate defender loses based on 1 dice

def calculate_change_one_dice(attack_high):
    count = 0
    for i in range(1, 7):
        if i >= attack_high:
            count += 1
    return 100 - (count / 6 * 100)


for roll, val in attack_rolls.items():
    attack_dice_high = roll[1]
    attack_rolls[roll].probability_of_defender_loses_against_one_dice = calculate_change_one_dice(attack_dice_high)

# Calculate defender loses based on 2 dice


def calculate_defender_losses(attack_high, attack_low, defense_high, defense_low):
    loses = 0
    if attack_high > defense_high:
        loses += 1
    if attack_low > defense_low:
        loses += 1
    return loses


for roll, val in attack_rolls.items():
    probability_count = [0, 0, 0]
    attack_dice_high = roll[1]
    attack_dice_low = roll[0]

    for defense_roll in defense_rolls:
        defense_dice_high = defense_roll[0]
        defense_dice_low = defense_roll[1]
        defender_loses = calculate_defender_losses(attack_dice_high, attack_dice_low, defense_dice_high, defense_dice_low)
        probability_count[defender_loses] += 1

    attack_rolls[roll].probability_of_defender_loses_0 = probability_count[0] / len(defense_rolls) * 100
    attack_rolls[roll].probability_of_defender_loses_1 = probability_count[1] / len(defense_rolls) * 100
    attack_rolls[roll].probability_of_defender_loses_2 = probability_count[2] / len(defense_rolls) * 100

# Print data
accumulated_probability = 0
print("Data as losses for defender")
print("attack_roll | n_rolls | probability of roll | accumulated_probability | lose against i dice | 0 loses | 1 loses | 2 loses v | rolls ")
print("----------- | ------- | ------------------- | ----------------------- | ------------------- | ------- | ------- | --------- | ------")

for k, v in attack_rolls.items():
    # print(key, val)
    accumulated_probability += v.probability_of_roll
    print("{}      | {:7d} | {:19.1f} | {:23.1f} | {:19.1f} | {:7.1f} | {:7.1f} | {:9.1f} |".format(k,
                                                                                                    len(v.rolls),
                                                                                                    v.probability_of_roll,
                                                                                                    accumulated_probability,
                                                                                                    v.probability_of_defender_loses_against_one_dice,
                                                                                                    v.probability_of_defender_loses_0,
                                                                                                    v.probability_of_defender_loses_1,
                                                                                                    v.probability_of_defender_loses_2,
                                                                                                    ))
