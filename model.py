# Code by Chidozie J. Nnaji
# Licensed under Attribution-NonCommercial 4.0 International (CC BY_NC 4.0)
from nltk.tokenize import word_tokenize  # used to split up the word and tokenize it

"""
    The class below used to read the emotions data and count the times an emotion appears in a text
    it also used to give a emotions a percent value, which is useful to figure out the most likely emotion.
"""


class words:
    def __init__(self, word, dfile, syfile):
        file1 = open(bytes('emo_Data/definitions/' + dfile, 'utf-8'), 'r')
        file2 = open(bytes('emo_Data/emotions_Data/' + syfile, 'utf-8'), 'r')
        self.word = word
        self.definition = file1.read()
        self.synonyms = file2.read()
        self.times = 0
        self.total = len(word_tokenize(self.synonyms))
        self.percent = 0.0
        self.words = word_tokenize(self.synonyms)
        file1.close()
        file2.close()

    def count(self, Words):
        for w in Words:
            if w in self.words:
                self.times += 1

    def pt(self):
        print(self.word, self.times)

    def pall(self):
        print(self.word)
        print(self.word, 'definitions', self.definition)
        print(self.word, 'times', self.times)
        print(self.word, 'total', self.total)

    def calp(self, number):
        self.percent = number


# Making instance of the class and saving to a list called emotions
emotions = [words('acceptance', 'acceptance.text', 'acceptance.text'),
            words('admiration', 'admiration.text', 'admiration.text'),
            words('adoration', 'adoration.text', 'adoration.text'),
            words('affection', 'affection.text', 'affection.text'),
            words('affirmation', 'affirmation.text', 'affirmation.text'),
            words('aggravation', 'aggravation.text', 'aggravation.text'),
            words('aggressive', 'aggressive.text', 'aggressive.text'),
            words('agitation', 'agitation.text', 'agitation.text'), words('agony', 'agony.text', 'agony.text'),
            words('alarm', 'alarm.text', 'alarm.text'), words('alienation', 'alienation.text', 'alienation.text'),
            words('amazement', 'amazement.text', 'amazement.text'),
            words('ambivalence', 'ambivalence.text', 'ambivalence.text'),
            words('amusement', 'amusement.text', 'amusement.text'), words('anger', 'anger.text', 'anger.text'),
            words('anguish', 'anguish.text', 'anguish.text'), words('annoyance', 'annoyance.text', 'annoyance.text'),
            words('anticipation', 'anticipation.text', 'anticipation.text'),
            words('anticipatory', 'anticipatory.text', 'anticipatory.text'),
            words('anxiety', 'anxiety.text', 'anxiety.text'), words('anxious', 'anxious.text', 'anxious.text'),
            words('apathy', 'apathy.text', 'apathy.text'),
            words('appreciation', 'appreciation.text', 'appreciation.text'),
            words('apprehension', 'apprehension.text', 'apprehension.text'),
            words('arrogance', 'arrogance.text', 'arrogance.text'),
            words('astonishment', 'astonishment.text', 'astonishment.text'),
            words('attentiveness', 'attentiveness.text', 'attentiveness.text'),
            words('attraction', 'attraction.text', 'attraction.text'), words('avarice', 'avarice.text', 'avarice.text'),
            words('aversion', 'aversion.text', 'aversion.text'), words('awe', 'awe.text', 'awe.text'),
            words('awkwardness', 'awkwardness.text', 'awkwardness.text'), words('baffle', 'baffle.text', 'baffle.text'),
            words('bewilderment', 'bewilderment.text', 'bewilderment.text'),
            words('bitter', 'bitter.text', 'bitter.text'), words('bitterness', 'bitterness.text', 'bitterness.text'),
            words('bliss', 'bliss.text', 'bliss.text'), words('blushing', 'blushing.text', 'blushing.text'),
            words('boredom', 'boredom.text', 'boredom.text'), words('brooding', 'brooding.text', 'brooding.text'),
            words('calm', 'calm.text', 'calm.text'), words('calmness', 'calmness.text', 'calmness.text'),
            words('carefree', 'carefree.text', 'carefree.text'), words('caring', 'caring.text', 'caring.text'),
            words('charity', 'charity.text', 'charity.text'), words('cheated', 'cheated.text', 'cheated.text'),
            words('cheerful', 'cheerful.text', 'cheerful.text'), words('cheesed', 'cheesed.text', 'cheesed.text'),
            words('claustrophobia', 'claustrophobia.text', 'claustrophobia.text'),
            words('coercion', 'coercion.text', 'coercion.text'),
            words('collywobbles', 'collywobbles.text', 'collywobbles.text'),
            words('comfort', 'comfort.text', 'comfort.text'), words('compassion', 'compassion.text', 'compassion.text'),
            words('confidence', 'confidence.text', 'confidence.text'),
            words('confident', 'confident.text', 'confident.text'), words('confused', 'confused.text', 'confused.text'),
            words('confusion', 'confusion.text', 'confusion.text'), words('contempt', 'contempt.text', 'contempt.text'),
            words('contentment', 'contentment.text', 'contentment.text'),
            words('contrary', 'contrary.text', 'contrary.text'), words('courage', 'courage.text', 'courage.text'),
            words('craving', 'craving.text', 'craving.text'),
            words('crosspatch', 'crosspatch.text', 'crosspatch.text'), words('cruelty', 'cruelty.text', 'cruelty.text'),
            words('curiosity', 'curiosity.text', 'curiosity.text'), words('cynicism', 'cynicism.text', 'cynicism.text'),
            words('decisiveness', 'decisiveness.text', 'decisiveness.text'),
            words('defeatism', 'defeatism.text', 'defeatism.text'),
            words('dejection', 'dejection.text', 'dejection.text'),
            words('delight', 'delight.text', 'delight.text'), words('depression', 'depression.text', 'depression.text'),
            words('desire', 'desire.text', 'desire.text'), words('despair', 'despair.text', 'despair.text'),
            words('desperate', 'desperate.text', 'desperate.text'),
            words('determination', 'determination.text', 'determination.text'),
            words('devotion', 'devotion.text', 'devotion.text'),
            words('disappear', 'disappear.text', 'disappear.text'),
            words('disappointed', 'disappointed.text', 'disappointed.text'),
            words('disappointment', 'disappointment.text', 'disappointment.text'),
            words('disapproval', 'disapproval.text', 'disapproval.text'),
            words('disapproving', 'disapproving.text', 'disapproving.text'),
            words('discard', 'discard.text', 'discard.text'),
            words('discomfort', 'discomfort.text', 'discomfort.text'),
            words('discontentment', 'discontentment.text', 'discontentment.text'),
            words('disdain', 'disdain.text', 'disdain.text'),
            words('disgruntlement', 'disgruntlement.text', 'disgruntlement.text'),
            words('disgust', 'disgust.text', 'disgust.text'), words('dislike', 'dislike.text', 'dislike.text'),
            words('dismay', 'dismay.text', 'dismay.text'), words('dispirited', 'dispirited.text', 'dispirited.text'),
            words('displeasure', 'displeasure.text', 'displeasure.text'),
            words('distraction', 'distraction.text', 'distraction.text'),
            words('distress', 'distress.text', 'distress.text'), words('disturbed', 'disturbed.text', 'disturbed.text'),
            words('dominance', 'dominance.text', 'dominance.text'), words('doom', 'doom.text', 'doom.text'),
            words('doubt', 'doubt.text', 'doubt.text'), words('doubtful', 'doubtful.text', 'doubtful.text'),
            words('dread', 'dread.text', 'dread.text'), words('eagerness', 'eagerness.text', 'eagerness.text'),
            words('ecstasy', 'ecstasy.text', 'ecstasy.text'), words('elation', 'elation.text', 'elation.text'),
            words('embarrass', 'embarrass.text', 'embarrass.text'),
            words('embarrassment', 'embarrassment.text', 'embarrassment.text'),
            words('empathic', 'empathic.text', 'empathic.text'), words('empathy', 'empathy.text', 'empathy.text'),
            words('enchantment', 'enchantment.text', 'enchantment.text'),
            words('enjoyment', 'enjoyment.text', 'enjoyment.text'),
            words('enlightenment', 'enlightenment.text', 'enlightenment.text'),
            words('ennui', 'ennui.text', 'ennui.text'), words('enthrallment', 'enthrallment.text', 'enthrallment.text'),
            words('enthusiasm', 'enthusiasm.text', 'enthusiasm.text'),
            words('enthusiastic', 'enthusiastic.text', 'enthusiastic.text'),
            words('entrancement', 'entrancement.text', 'entrancement.text'), words('envy', 'envy.text', 'envy.text'),
            words('epiphany', 'epiphany.text', 'epiphany.text'), words('euphoria', 'euphoria.text', 'euphoria.text'),
            words('exasperation', 'exasperation.text', 'exasperation.text'),
            words('excited', 'excited.text', 'excited.text'), words('excitement', 'excitement.text', 'excitement.text'),
            words('exhilaration', 'exhilaration.text', 'exhilaration.text'),
            words('expectancy', 'expectancy.text', 'expectancy.text'),
            words('fascination', 'fascination.text', 'fascination.text'),
            words('fatalism', 'fatalism.text', 'fatalism.text'), words('fear', 'fear.text', 'fear.text'),
            words('feeling good', 'feeling good.text', 'feeling good.text'),
            words('ferocity', 'ferocity.text', 'ferocity.text'), words('flee', 'flee.text', 'flee.text'),
            words('fondness', 'fondness.text', 'fondness.text'),
            words('fraud', 'fraud.text', 'fraud.text'), words('friendliness', 'friendliness.text', 'friendliness.text'),
            words('friendship', 'friendship.text', 'friendship.text'), words('fright', 'fright.text', 'fright.text'),
            words('frivolity', 'frivolity.text', 'frivolity.text'),
            words('frozenness', 'frozenness.text', 'frozenness.text'),
            words('frustrated', 'frustrated.text', 'frustrated.text'),
            words('frustration', 'frustration.text', 'frustration.text'),
            words('fury', 'fury.text', 'fury.text'), words('gaiety', 'gaiety.text', 'gaiety.text'),
            words('gladness', 'gladness.text', 'gladness.text'), words('glee', 'glee.text', 'glee.text'),
            words('gloat', 'gloat.text', 'gloat.text'),
            words('gloom', 'gloom.text', 'gloom.text'), words('gloominess', 'gloominess.text', 'gloominess.text'),
            words('glumness', 'glumness.text', 'glumness.text'), words('gratitude', 'gratitude.text', 'gratitude.text'),
            words('greed', 'greed.text', 'greed.text'), words('grief', 'grief.text', 'grief.text'),
            words('grieved', 'grieved.text', 'grieved.text'), words('grouchy', 'grouchy.text', 'grouchy.text'),
            words('grumpy', 'grumpy.text', 'grumpy.text'), words('guilt', 'guilt.text', 'guilt.text'),
            words('habituation', 'habituation.text', 'habituation.text'),
            words('happiness', 'happiness.text', 'happiness.text'),
            words('hate', 'hate.text', 'hate.text'), words('hatred', 'hatred.text', 'hatred.text'),
            words('heartbroken', 'heartbroken.text', 'heartbroken.text'),
            words('heebie jeebies', 'heebie jeebies.text', 'heebie jeebies.text'),
            words('helpless', 'helpless.text', 'helpless.text'),
            words('helplessness', 'helplessness.text', 'helplessness.text'),
            words('high spirits', 'high spirits.text', 'high spirits.text'),
            words('hoard', 'hoard.text', 'hoard.text'), words('holiness', 'holiness.text', 'holiness.text'),
            words('homesickness', 'homesickness.text', 'homesickness.text'), words('hope', 'hope.text', 'hope.text'),
            words('hopeful', 'hopeful.text', 'hopeful.text'),
            words('hopefulness', 'hopefulness.text', 'hopefulness.text'),
            words('hopeless', 'hopeless.text', 'hopeless.text'), words('horny', 'horny.text', 'horny.text'),
            words('horrified', 'horrified.text', 'horrified.text'), words('horror', 'horror.text', 'horror.text'),
            words('hostility', 'hostility.text', 'hostility.text'), words('huff', 'huff.text', 'huff.text'),
            words('humble', 'humble.text', 'humble.text'), words('humiliate', 'humiliate.text', 'humiliate.text'),
            words('humiliation', 'humiliation.text', 'humiliation.text'),
            words('humility', 'humility.text', 'humility.text'),
            words('hunger', 'hunger.text', 'hunger.text'), words('hurt', 'hurt.text', 'hurt.text'),
            words('hysteria', 'hysteria.text', 'hysteria.text'),
            words('impatience', 'impatience.text', 'impatience.text'),
            words('indifference', 'indifference.text', 'indifference.text'),
            words('indignation', 'indignation.text', 'indignation.text'),
            words('infatuation', 'infatuation.text', 'infatuation.text'),
            words('infuriated', 'infuriated.text', 'infuriated.text'),
            words('insecurity', 'insecurity.text', 'insecurity.text'), words('insight', 'insight.text', 'insight.text'),
            words('insult', 'insult.text', 'insult.text'),
            words('insulted', 'insulted.text', 'insulted.text'), words('interest', 'interest.text', 'interest.text'),
            words('intrigue', 'intrigue.text', 'intrigue.text'),
            words('irritability', 'irritability.text', 'irritability.text'),
            words('irritated', 'irritated.text', 'irritated.text'),
            words('irritation', 'irritation.text', 'irritation.text'),
            words('isolation', 'isolation.text', 'isolation.text'), words('jealousy', 'jealousy.text', 'jealousy.text'),
            words('joviality', 'joviality.text', 'joviality.text'), words('joy', 'joy.text', 'joy.text'),
            words('jubilation', 'jubilation.text', 'jubilation.text'),
            words('kindness', 'kindness.text', 'kindness.text'),
            words('liking', 'liking.text', 'liking.text'), words('loathing', 'loathing.text', 'loathing.text'),
            words('loneliness', 'loneliness.text', 'loneliness.text'), words('lonely', 'lonely.text', 'lonely.text'),
            words('longing', 'longing.text', 'longing.text'), words('lost', 'lost.text', 'lost.text'),
            words('love', 'love.text', 'love.text'), words('low-spirited', 'low-spirited.text', 'low-spirited.text'),
            words('lust', 'lust.text', 'lust.text'), words('mad', 'mad.text', 'mad.text'),
            words('meditation', 'meditation.text', 'meditation.text'),
            words('melancholy', 'melancholy.text', 'melancholy.text'),
            words('miffed', 'miffed.text', 'miffed.text'),
            words('misconceptions', 'misconceptions.text', 'misconceptions.text'),
            words('miserable', 'miserable.text', 'miserable.text'), words('miserly', 'miserly.text', 'miserly.text'),
            words('misery', 'misery.text', 'misery.text'), words('modesty', 'modesty.text', 'modesty.text'),
            words('morbid', 'morbid.text', 'morbid.text'),
            words('mortification', 'mortification.text', 'mortification.text'),
            words('nauseated', 'nauseated.text', 'nauseated.text'), words('negation', 'negation.text', 'negation.text'),
            words('neglect', 'neglect.text', 'neglect.text'), words('nervous', 'nervous.text', 'nervous.text'),
            words('nervousness', 'nervousness.text', 'nervousness.text'),
            words('nostalgia', 'nostalgia.text', 'nostalgia.text'), words('offended', 'offended.text', 'offended.text'),
            words('optimism', 'optimism.text', 'optimism.text'),
            words('outrage', 'outrage.text', 'outrage.text'),
            words('overwhelmed', 'overwhelmed.text', 'overwhelmed.text'), words('pain', 'pain.text', 'pain.text'),
            words('panic', 'panic.text', 'panic.text'),
            words('panicked', 'panicked.text', 'panicked.text'), words('paranoia', 'paranoia.text', 'paranoia.text'),
            words('passion', 'passion.text', 'passion.text'), words('patience', 'patience.text', 'patience.text'),
            words('peeved', 'peeved.text', 'peeved.text'), words('pensiveness', 'pensiveness.text', 'pensiveness.text'),
            words('pessimism', 'pessimism.text', 'pessimism.text'), words('pique', 'pique.text', 'pique.text'),
            words('pity', 'pity.text', 'pity.text'), words('pleased', 'pleased.text', 'pleased.text'),
            words('pleasure', 'pleasure.text', 'pleasure.text'),
            words('politeness', 'politeness.text', 'politeness.text'),
            words('powerlessness', 'powerlessness.text', 'powerlessness.text'),
            words('pride', 'pride.text', 'pride.text'), words('proud', 'proud.text', 'proud.text'),
            words('prudishness', 'prudishness.text', 'prudishness.text'),
            words('puzzlement', 'puzzlement.text', 'puzzlement.text'), words('rage', 'rage.text', 'rage.text'),
            words('rapture', 'rapture.text', 'rapture.text'), words('reflection', 'reflection.text', 'reflection.text'),
            words('regret', 'regret.text', 'regret.text'), words('rejection', 'rejection.text', 'rejection.text'),
            words('relaxation', 'relaxation.text', 'relaxation.text'), words('relief', 'relief.text', 'relief.text'),
            words('reluctance', 'reluctance.text', 'reluctance.text'), words('remorse', 'remorse.text', 'remorse.text'),
            words('reproach', 'reproach.text', 'reproach.text'),
            words('resentment', 'resentment.text', 'resentment.text'),
            words('resignation', 'resignation.text', 'resignation.text'),
            words('resigned', 'resigned.text', 'resigned.text'),
            words('restlessness', 'restlessness.text', 'restlessness.text'),
            words('revulsion', 'revulsion.text', 'revulsion.text'),
            words('rivalry', 'rivalry.text', 'rivalry.text'), words('road rage', 'road rage.text', 'road rage.text'),
            words('romance', 'romance.text', 'romance.text'), words('sadness', 'sadness.text', 'sadness.text'),
            words('satisfaction', 'satisfaction.text', 'satisfaction.text'),
            words('satisfied', 'satisfied.text', 'satisfied.text'), words('saudade', 'saudade.text', 'saudade.text'),
            words('scorn', 'scorn.text', 'scorn.text'),
            words('self-conscious', 'self-conscious.text', 'self-conscious.text'),
            words('sentimentality', 'sentimentality.text', 'sentimentality.text'),
            words('serenity', 'serenity.text', 'serenity.text'),
            words('shame', 'shame.text', 'shame.text'), words('shock', 'shock.text', 'shock.text'),
            words('shyness', 'shyness.text', 'shyness.text'), words('smugness', 'smugness.text', 'smugness.text'),
            words('song', 'song.text', 'song.text'), words('sorrow', 'sorrow.text', 'sorrow.text'),
            words('stress', 'stress.text', 'stress.text'), words('stressed', 'stressed.text', 'stressed.text'),
            words('submission', 'submission.text', 'submission.text'),
            words('suffering', 'suffering.text', 'suffering.text'),
            words('sulkiness', 'sulkiness.text', 'sulkiness.text'), words('surprise', 'surprise.text', 'surprise.text'),
            words('suspense', 'suspense.text', 'suspense.text'), words('suspicion', 'suspicion.text', 'suspicion.text'),
            words('sympathy', 'sympathy.text', 'sympathy.text'),
            words('tenderness', 'tenderness.text', 'tenderness.text'),
            words('terrified', 'terrified.text', 'terrified.text'), words('terror', 'terror.text', 'terror.text'),
            words('thankfulness', 'thankfulness.text', 'thankfulness.text'),
            words('thrill', 'thrill.text', 'thrill.text'),
            words('thrilled', 'thrilled.text', 'thrilled.text'), words('tolerance', 'tolerance.text', 'tolerance.text'),
            words('torment', 'torment.text', 'torment.text'), words('triumph', 'triumph.text', 'triumph.text'),
            words('troubled', 'troubled.text', 'troubled.text'), words('trust', 'trust.text', 'trust.text'),
            words('unbelief', 'unbelief.text', 'unbelief.text'),
            words('uncertainty', 'uncertainty.text', 'uncertainty.text'),
            words('uncomfortable', 'uncomfortable.text', 'uncomfortable.text'),
            words('uneasiness', 'uneasiness.text', 'uneasiness.text'),
            words('unhappiness', 'unhappiness.text', 'unhappiness.text'),
            words('unhappy', 'unhappy.text', 'unhappy.text'), words('vengeance', 'vengeance.text', 'vengeance.text'),
            words('vengeful', 'vengeful.text', 'vengeful.text'),
            words('vengefulness', 'vengefulness.text', 'vengefulness.text'),
            words('victory', 'victory.text', 'victory.text'), words('vigilance', 'vigilance.text', 'vigilance.text'),
            words('vulnerability', 'vulnerability.text', 'vulnerability.text'),
            words('wanderlust', 'wanderlust.text', 'wanderlust.text'), words('weeping', 'weeping.text', 'weeping.text'),
            words('withdrawal', 'withdrawal.text', 'withdrawal.text'), words('woe', 'woe.text', 'woe.text'),
            words('wonder', 'wonder.text', 'wonder.text'), words('worried', 'worried.text', 'worried.text'),
            words('worry', 'worry.text', 'worry.text'), words('wrath', 'wrath.text', 'wrath.text'),
            words('zeal', 'zeal.text', 'zeal.text'), words('zest', 'zest.text', 'zest.text')]


# Set all the times back to zero
def reset():
    for i in emotions:
        i.times = 0


# Arrange all the percent in descending order, then saving it to an array and lastly returning that array.
def arrange(array):
    new = sorted(array, reverse=True)
    return new


""""
 The preprocess function uses probability to find the most likely emotions
First it count the amount of a emotion is in a text. Then assigns a percents
to each emotion. and then find the required amount a emotion needs to be to be considered
most likely.
"""


def preprocess(line):
    reset()
    most_likely = []
    potential = []
    not_likely = []
    token = word_tokenize(line)
    length = len(word_tokenize(line))
    percentages = []
    # counting the amount of emotion in a the given text: token
    for i in emotions:
        i.count(token)
    # giving each emotion a percent value
    for p in emotions:
        p.calp((p.times / length) * 100)
    # saving all the percent of a emotion into an array
    for pe in emotions:
        percentages.append(pe.percent)
    percentages = arrange(percentages)
    # gets the highest percentage
    highest_p = percentages[0]
    # gets the second highest percentage
    second_highest_p = percentages[1]
    # adds highest and second highest percentage, to find the requirement for an emotion to be considered most likely,
    # or potential or not likely
    require = (float(highest_p + second_highest_p)) / 2
    for last in emotions:
        if last.percent >= require:
            array = 'Emotion:', last.word, 'Percent:', last.percent, 'Definitions:', last.definition
            most_likely.append(array)
        elif require - 20 <= last.percent <= require + 20:
            # this is if statement if in case the percent is 0.0, for what ever reason. We don't want potentials to be
            # full of 0's
            if last.percent != 0.0:
                array = 'Emotion:', last.word, 'Percent:', last.percent, 'Definitions:', last.definition
                potential.append(array)
            else:
                array = 'Emotion:', last.word, 'Percent:', last.percent, 'Definition:', last.definition
                not_likely.append(array)
        else:
            array = 'Emotion:', last.word, 'Percent:', last.percent, 'Definitions:', last.definition
            not_likely.append(array)
    if require > 0.2:
        return True, require, most_likely, potential, not_likely
    else:
        return False, require, potential


""" 
emotions_test is use to find the accuracy of the emotion. Feel free to add more emotions to test, as long as they are
part of the word class instance, if it is not an instance, the computer will not be able to detect it. Feel free to 
change, delete, and add emotions or word that signify emotions, in the emotions_test dictionary. In case the one I 
added was not accurate, which might explain the low score of the AI
"""
emotions_test = {'low-spirited': ['sad and fed up.', "It makes me sad to see all those animals in cages at the zoo.",
                                  "He's so down in the dumps these days.", 'ill or tired', "I've got a blinding "
                                                                                           "headache and I feel",
                                  'unhappy'],

                 'disappointed': ['She was disappointed by her son\'s poor results at school.', "When you didn't turn "
                                                                                                "up to the meeting, "
                                                                                                "I felt really let "
                                                                                                "down."],
                 'thrilled': ['When he asked her to marry him she was ecstatic.', "She was over the moon with her new "
                                                                                  "bicycle and rode it every day for "
                                                                                  "a whole year."
                                                                                  "I'm keen to see your new house. "
                                                                                  "I've heard lots about it."],
                 'excited': 'I\'m excited by the new opportunities that the internet brings.',
                 'astonishment': 'When he heard the news, he became quite emotional.',
                 'envy': ["I'm very envious of her happiness. I wish I was happy too.", 'envious.', "She was jealous "
                                                                                                    "of her sister's "
                                                                                                    "new toy."],
                 'embarrass': ['slightly ashamed.', 'I felt so embarrassed that I went bright red.'],
                 'blushing': 'I felt so embarrassed that I went bright red.',
                 'anger': ['very angry.', "I was unhappy to hear that I hadn't got the job.",
                           'extremely angry, but hiding it.',
                           "She was seething after her boss "
                           "criticised her.", 'I was furious with '
                                              'him for breaking my'' favourite vase.'],
                 'fear': ["She's terrified of spiders and screams whenever she sees one.", 'As a child '
                                                                                           'she was '
                                                                                           'frightened '
                                                                                           'of the '
                                                                                           'dark.'],
                 'glee': ['very good.', 'I feel great today.', "I feel terrific today!"],
                 'feel good': 'She was happy to hear the good news.',
                 'horrified': ['very shocked.', "I'm horrified by the amount of violence on television today.",
                               'frightened', "very scared"],
                 'irritated': ['annoyed.', 'angry', "I get so irritated when he changes TV channels without asking me "
                                                    "first."],
                 'intrigue': ['being so interested in something you have to find out more.', "I'm intrigue to hear "
                                                                                             "about your safari in "
                                                                                             "Kenya."],
                 'pity': ['tired and having no interest.', 'After 10 years at this company, I just feel jaded.'],
                 'stress': ["You look a bit tense", "I'm "
                                                    "keen "
                                                    "on "
                                                    "keeping "
                                                    "fit. ",
                            "I am "
                            "worried",
                            "I am anxious",
                            "I feel really stressed at work. I need a brake.", "He "
                                                                               "was "
                                                                               "stressed out by all the traveling in "
                                                                               "his job"],
                 'calm': ["I can't be bothered to do anything today. I feel really lazy!", "I'm going to play the "
                                                                                           "lottery. I feel lucky "
                                                                                           "today!"],
                 'pleased': ["Looking at my sister's new baby made me feel really maternal.", "I felt wonderful after "
                                                                                              "such a relaxing "
                                                                                              "weekend"],
                 'surprised': "I was so nonplussed by his announcement that I couldn't say anything.",
                 'pessimism': ["When you can only see the disadvantages.", "I feel very negative about my job. The "
                                                                           "pay is awful."],
                 'overwhelmed': ["So much emotion that you don't know what to say or do.", "I was overwhelmed by the "
                                                                                           "offer of promotion at "
                                                                                           "work."],
                 'scorn': ["When you don't want to do something.", "I'm reluctant to buy a new car. The one we have "
                                                                   "is fine."],
                 'carefree': 'I was completely relaxed after I came back from holiday.',
                 'nauseated': 'ill or tired'
                 }
