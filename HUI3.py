

#implement HUI Multi-Attribute Utility Function"Formula (Dead - Perfect Health scale)
# u* = 1.371 (b1 * b2 * b3 * b4 * b5 * b6 * b7 * b8) - 0.371

Constant = 0.371
dictCoefficients = {'Vision':       [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':      [1, 0.95, 0.89, 0.80, 0.74, 0.61],
                    'Speech':       [1, 0.94, 0.89, 0.81, 0.68, 0],
                    'Ambulation':   [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':    [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':      [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Cognition':    [1, 0.92, 0.95, 0.83, 0.60, 0.42],
                    'Pain':         [1, 0.96, 0.90, 0.77, 0.55, 0]};

def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1, 2, 3, 4, 5, 6')
    if not(hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1, 2, 3, 4, 5, 6')
    if not(speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1, 2, 3, 4, 5')
    if not(ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1, 2, 3, 4, 5, 6')
    if not(dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1, 2, 3, 4, 5, 6')
    if not(emotion in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Emotion level can take only 1, 2, 3, 4, 5, 6')
    if not(cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1, 2, 3, 4, 5, 6')
    if not(pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1, 2, 3, 4, 5')

    score = 1.371
    score *= dictCoefficients['Vision'][vision - 1]
    score *= dictCoefficients['Hearing'][hearing - 1]
    score *= dictCoefficients['Speech'][speech - 1]
    score *= dictCoefficients['Ambulation'][ambulation - 1]
    score *= dictCoefficients['Dexterity'][dexterity - 1]
    score *= dictCoefficients['Emotion'][emotion - 1]
    score *= dictCoefficients['Cognition'][cognition - 1]
    score *= dictCoefficients['Pain'][pain - 1]
    score -= 0.371

    return score
