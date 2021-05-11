# Project PCBS : visual information processing

Background

The project will be a replication of Eriksen and Eriksen's 1974 article : "Effects of noise letters upon the identification of a target letter in a nonsearch task". 
The paper draws on some previous experiments, which aimed at assessing the impact of noise (in the form of distractor letters) upon RT and accuracy in visual search experiments (where a target letter, which can appear at different places on the screen, had to be detected). This is, more generally, a replication of the flanker task paradigm. 
The authors argue that, in order to distinguish the effects of noise on the visual search and on the identification of the target, one must create a baseline condition. That is, there must be an experiment which asseses the impact of noise on identification of the target only : this is what this experimental design is about. 
Some previous findings seemed to indicate that noise increased RT and decreased accuracy even in identification-only tasks. This could be interpreted as evidence that "there is a minimal channel size in terms of capacity for simultaneous processing with a capacity exceeding that required for identifying a single letter. Further, the unutilized capacity cannot be shut off and, if there are other letters or stimuli present, they will be processed simultaneously along with the target". There should then be a selectively inhibitory process, which allows the subject to respond only according to the target letter (even if more letters were processed) 
This experiment is meant to test this hypothesis. 


Experimental design

The subject is presented a white screen, on which strings of letter appear at each trial. He is told that the target letter will always appear at one given location (1/2 degree above the fixation point) and that he should ignore letters appearing at any other position. In all but two control trial where the target letter appears alone, the target letter appears flanked by 3 other letters on either side. 
The subject is asked to press the right key if the target letter is a H or a K, and the left key if the target letter is a S or a C. 
There are five conditions, where the target letter is flanked on either side by :
* three repetitions of itself
* three repetitions of the letter that was the other member of that response set (Hs are flanked by Ks and vice versa, Cs and flanked by Ss and vice versa)
*  three occurrences of one of the letters of the opposite response set (Hs and Ks were flanked by either Cs or Ss and vice versa)
* three letters having features similar to the target set as determined by the Gibson system but excluding the two letters that were members of the target
set (Hs and Ks are flanked by Ns or Ws or Zs, S and Cs are flanked by Gs or Js or Qs)
* three letters having features dissimilar to target set as determined by the Gibson system and excluding the target set (Hs and Ks are flanked by Gs or Js or Qs and Cs and Ss are flanked by Ns or Ws or Zs)

![](https://github.com/emma-badard/PCBS---visual-information-processing/blob/master/images/image.git.1.pdf)

RT and accuracy is collected for all conditions, and the mean RT across conditions and percentage accuracy across conditions are presented below. 

Implementation

The flanker.py file contains the main code, and the read_data.py file contains the code to read and analyse data. 

Results

TO BE DONE

To do
* In the original paper, another variable was spacing between the letters. It would have constituted a second training set. I did not have time to implement this other variable, since I already had quite a lot of conditions to treat, but I would have liked to implement it.
* Parts of the code could have been cleaner. For example, some lines of code were copy pasted and slightly modified (lines 44, 46 and 48 ; lines 58 to 66 and 69 to 78)
* The "analyse_data" file could be clearer, since there are many variable names. 

