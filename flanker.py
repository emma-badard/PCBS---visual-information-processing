# Packages 
import pandas
import expyriment
import random

# Initializing experiment
exp = expyriment.design.Experiment(name="Experiment")
expyriment.control.set_develop_mode()
expyriment.control.initialize(exp)
expyriment.control.defaults.window_mode = True

# Displayed stuff
fixation_cross = expyriment.stimuli.FixCross(position = (0,30))
blankscreen = expyriment.stimuli.BlankScreen()
general_instructions_screen = expyriment.stimuli.TextScreen("General instructions",
	"You will be presented a white screen with a fixation cross in the middle." 
	"Above the fixation cross, strings of letters will appear." 
	"The letter just above the fixation cross is your target letter."
	"If the target letter that appears is a H or a K, you must press the right arrow on your keyboard as fast as possible."
	"If the target letter is a S or a C, you must press the left arrow of your keyboard as fast as possible."
	"You must ignore the letters which surround your target letter, if there are any."
	"There will be one training set, to make sure the task is clear, and one test sets, where your reaction time and accuracy will be recorded."
	"Have a nice experiment !")
training_set_instructions =  expyriment.stimuli.TextScreen("Training set instructions",
	"""This is the training set : don't worry, your reaction time and accuracy will not be recorded.""")
first_test_set_instructions =  expyriment.stimuli.TextScreen("First training set instructions",
	"""This is the test set : good luck !""")
final_instructions =  expyriment.stimuli.TextScreen("Final instructions", 
	"""This is the end of the experiment. Well done, and thanks for your participation !""")


# Stimuli
CS_set = ["C", "S"]
HK_set = ["H", "K"]
NWZ_set = ["N","W","Z"]
GJQ_set = ["G","J","Q"]

control_set_no_flanker = CS_set + HK_set

flanker_is_the_same_letter_set = ["HHHHHHH","KKKKKKK","SSSSSSS","CCCCCCC"]

flanker_is_in_the_same_response_set_set = ["KKKHKKK","HHHKHHH","CCCSCCC","SSSCSSS"]

flanker_is_in_the_different_response_set_set = [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in CS_set for d2 in CS_set for d3 in CS_set for t in HK_set for d4 in CS_set for d5 in CS_set for d6 in CS_set] + [d1 + d2 + d3 + t + d4 + d5 + d6  for d1 in HK_set for d2 in HK_set for d3 in HK_set for t in CS_set for d4 in HK_set for d5 in HK_set for d6 in HK_set]

flanker_has_similar_features_set = [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in NWZ_set for d2 in NWZ_set for d3 in NWZ_set for t in HK_set for d4 in NWZ_set for d5 in NWZ_set for d6 in NWZ_set] + [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in GJQ_set for d2 in GJQ_set for d3 in GJQ_set for t in CS_set for d4 in GJQ_set for d5 in GJQ_set for d6 in GJQ_set]

flanker_has_dissimilar_features_set = [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in GJQ_set for d2 in GJQ_set for d3 in GJQ_set for t in HK_set for d4 in GJQ_set for d5 in GJQ_set for d6 in GJQ_set] + [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in NWZ_set for d2 in NWZ_set for d3 in NWZ_set for t in CS_set for d4 in NWZ_set for d5 in NWZ_set for d6 in NWZ_set]

dict_of_conditions = {"control" : control_set_no_flanker, 
					  "same letter" : flanker_is_the_same_letter_set,
					  "same response set" : flanker_is_in_the_same_response_set_set, 
					  "different response set" : flanker_is_in_the_different_response_set_set,
					  "similar features" : flanker_has_similar_features_set,
					  "dissimilar features" : flanker_has_dissimilar_features_set}

# Experiment structure
block_training = expyriment.design.Block(name = "Training set")
for cond, stimuli in dict_of_conditions.items() : 
	for _ in range(2) : 
		t = expyriment.design.Trial()
		t.set_factor("Condition", cond)
		chosen_stim = "".join(random.sample(stimuli, 1))
		t.set_factor("Stimulus", chosen_stim)
		t.add_stimulus(expyriment.stimuli.TextLine(chosen_stim, text_size=25, text_font="lucidasanstypewriterregular"))
		block_training.add_trial(t)


block_test = expyriment.design.Block(name = "Test set 1")
for cond, stimuli in dict_of_conditions.items() : 
	if cond != "control" : 
		for _ in range(4) : 
			t = expyriment.design.Trial()
			t.set_factor("Condition", cond)
			chosen_stim = "".join(random.sample(stimuli, 1))
			t.set_factor("Stimulus", chosen_stim)
			t.add_stimulus(expyriment.stimuli.TextLine(chosen_stim, text_size=25, text_font="lucidasanstypewriterregular"))
			block_test.add_trial(t)


exp.add_block(block_training)
exp.add_block(block_test)
exp.data_variable_names = ["Block", "Condition", "Stimulus", "Accuracy", "RT"]


# Experiment execution
expyriment.control.start()

general_instructions_screen.present()
exp.clock.wait(waiting_time = 10)
exp.keyboard.wait(keys = [expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])

for i, block in enumerate(exp.blocks):
	if i == 0 :
		training_set_instructions.present()
		exp.clock.wait(waiting_time = 10)
		exp.keyboard.wait(keys = [expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
		n_trials = 6
	else : 
		first_test_set_instructions.present()
		exp.clock.wait(waiting_time = 10)
		exp.keyboard.wait(keys = [expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
		n_trials = 30

	for t in block.trials :

		fixation_cross.present(clear = True, update = False)
		t.stimuli[0].present(clear = False, update = True) 

		
		stim = t.get_factor("Stimulus")
		condition = t.get_factor("Condition")
		key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT, expyriment.misc.constants.K_RIGHT])

		if condition != "control" : 
			right_trial = stim[3] in HK_set
			left_trial = stim[3] in CS_set
			accuracy = (((key == expyriment.misc.constants.K_RIGHT) and right_trial) or ((key == expyriment.misc.constants.K_LEFT) and left_trial))
	
		else :
			accuracy = "NaN"
		
		exp.data.add([block.name, condition, stim, accuracy, rt])
		
final_instructions.present()
exp.clock.wait(waiting_time = 10)
exp.keyboard.wait(keys = [expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])

expyriment.control.end()

