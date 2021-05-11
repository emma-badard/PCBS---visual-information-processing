# Packages 
import pandas
import expyriment
import random

# Initializing experiment
exp = expyriment.design.Experiment(name="Experiment")
expyriment.control.initialize(exp)
expyriment.control.defaults.window_mode = True

# Displayed stuff
#expyriment.control.defaults.window_mode(True)
fixation_cross = expyriment.stimuli.FixCross(position = (20,50))
blankscreen = expyriment.stimuli.BlankScreen()
general_instructions_screen = expyriment.stimuli.TextScreen("General instructions","You will be presented a white screen with a fixation cross in the middle. \n Above the fixation cross, strings of letters will appear. \n The letter just above the fixation cross is your target letter. \n If the target letter that appears is a H or a K, you must press the left arrow on your keyboard as fast as possible. \n If the target letter is a S or a C, you must press the right arrow of your keyboard as fast as possible. \n You must ignore the letters which surround your target letter, if there are any. \n There will be one training set, to make sure the task is clear, and one test sets, where your reaction time and accuracy will be recorded.\n Have a nice experiment !")
training_set_instructions =  expyriment.stimuli.TextScreen("Training set instructions","This is the training set : don't worry, your reaction time and accuracy will not be recorded.")
first_test_set_instructions =  expyriment.stimuli.TextScreen("First training set instructions","This is the test set : good luck !")
final_instructions =  expyriment.stimuli.TextScreen("Final instructions", "This is the end of the experiment. Well done, and thanks for your participation !")


# Stimuli
CS_set = ["C", "S"]
HK_set = ["H", "K"]
NWZ_set = ["N","W","Z"]
GJQ_set = ["G","J","Q"]
control_set_no_flanker = CS_set + HK_set
flanker_is_the_same_letter_set = ["HHHHHHH","KKKKKKK","SSSSSSS","CCCCCCC"]
flanker_is_in_the_same_response_set_set = ["KKKHKKK","HHHKHHH","CCCSCCC","SSSCSSS"]
flanker_is_in_the_different_response_set_set = [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in CS_set for d2 in CS_set for d3 in CS_set for t in HK_set for d4 in CS_set for d5 in CS_set for d6 in CS_set] + [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in HK_set for d2 in HK_set for d3 in HK_set for t in CS_set for d4 in HK_set for d5 in HK_set for d6 in HK_set]
flanker_has_similar_features_set = [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in NWZ_set for d2 in NWZ_set for d3 in NWZ_set for t in HK_set for d4 in NWZ_set for d5 in NWZ_set for d6 in NWZ_set] + [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in GJQ_set for d2 in GJQ_set for d3 in GJQ_set for t in CS_set for d4 in GJQ_set for d5 in GJQ_set for d6 in GJQ_set]
flanker_has_dissimilar_features_set = [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in GJQ_set for d2 in GJQ_set for d3 in GJQ_set for t in HK_set for d4 in GJQ_set for d5 in GJQ_set for d6 in GJQ_set] + [d1 + d2 + d3 + t + d4 + d5 + d6 for d1 in NWZ_set for d2 in NWZ_set for d3 in NWZ_set for t in CS_set for d4 in NWZ_set for d5 in NWZ_set for d6 in NWZ_set]
#list_of_conditions = [control_set_no_flanker,flanker_is_the_same_letter_set,flanker_is_in_the_same_response_set_set, flanker_is_in_the_different_response_set_set,flanker_has_similar_features_set,flanker_has_dissimilar_features_set]
dict_of_conditions = {"control" : control_set_no_flanker, 
					  "same letter" : flanker_is_the_same_letter_set,
					  "same response set" : flanker_is_in_the_same_response_set_set, 
					  "different response set" : flanker_is_in_the_different_response_set_set,
					  "similar features" : flanker_has_similar_features_set,
					  "dissimilar features" : flanker_has_dissimilar_features_set}

training_dataset = random.sample(control_set_no_flanker,2) + random.sample(flanker_is_the_same_letter_set,2) + random.sample (flanker_is_in_the_same_response_set_set,2) + random.sample(flanker_is_in_the_different_response_set_set,2) + random.sample (flanker_has_similar_features_set,2) + random.sample(flanker_has_dissimilar_features_set,2)
test_1_dataset = random.sample(flanker_is_the_same_letter_set,4) + random.sample (flanker_is_in_the_same_response_set_set, 4) + random.sample(flanker_is_in_the_different_response_set_set, 4) + random.sample (flanker_has_similar_features_set,4) + random.sample(flanker_has_dissimilar_features_set,4)


# Experiment structure

block_one = expyriment.design.Block(name = "Training set")
block_two = expyriment.design.Block(name = "Test set 1")
exp.add_block(block_one)
exp.add_block(block_two)

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
		used_dataset = training_dataset
		n_trials = 6
	else : 
		first_test_set_instructions.present()
		exp.clock.wait(waiting_time = 10)
		exp.keyboard.wait(keys = [expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])
		used_dataset = test_1_dataset
		n_trials = 20


	for j in range(n_trials) :
		#presents the stimulus
		fixation_cross.present(clear = True, update = False)
		chosen_stim = random.sample(used_dataset,1)
		presented_stim = expyriment.stimuli.TextLine("".join(chosen_stim), position = (20,20))
		presented_stim.present(clear = False, update = True) 

		#computes the variables of interest
		trial = expyriment.design.Trial()
		trial.add_stimulus(presented_stim)
		block.add_trial(trial)

		chosen_stim_as_string = chosen_stim[0]
		left_trial = (chosen_stim_as_string[len(chosen_stim_as_string)//2] in HK_set)
		key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT, expyriment.misc.constants.K_RIGHT])
		accuracy = ((key == 275) and left_trial)

		condition = -1
		for key, value in dict_of_conditions.items() :
			if chosen_stim_as_string in value :
				condition = key


		#stocks the variables of interest in the data file
		exp.data.add([block.name, j, condition, accuracy, rt])
		exp.data_variable_names = ["Block", "Trial","Condition","Accuracy", "RT"]

final_instructions.present()
exp.clock.wait(waiting_time = 10)
exp.keyboard.wait(keys = [expyriment.misc.constants.K_LEFT,expyriment.misc.constants.K_RIGHT])

expyriment.control.end()

