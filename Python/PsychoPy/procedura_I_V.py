#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on maj 10, 2019, at 11:08
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = 'with_training'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\pcisl\\Desktop\\statystyka\\pilotaż\\procedura_I_V.py',
    
    #'C:\\Users\\pcisl\\Desktop\\psychopy\\procedura\\with_training.py'
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[255,255,255], colorSpace='rgb',
    blendMode='avg', useFBO=False,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "begining"
beginingClock = core.Clock()
start = visual.TextStim(win=win, name='start',
    text='''Witamy na badaniach rozpoznania kategorii bodźców wzrokowych. Podczas zadania, na ekranie w pierwszej kolejności zostanie wyświetlony tekst lub obrazek.\n
    W przypadku tekstu, spróbuj wyobrazić sobie obiekt, którego nazwa została wyświetlona. W przypadku obrazka, po prostu skup się na tym co jest na nim prezentowane.\n
    Po prezentacji obrazka lub tekstu, po krótkiej przerwie na ekranie pojawi się sześć obrazków. Twoim zadaniem, jest sprawdzenie czy te sześć obrazków należą do jednej kategorii. Na przykład, czy prezentowane jest sześć obrazków ubrań.
    \n(wciśnij spację, aby przejść do dalszej części instrukcji)
    ''',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=True, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

start_img = visual.ImageStim(
    win=win,
    name='start_img', 
    image='instrukcje/wstep.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.3, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "training_instruction"
training_instructionClock = core.Clock()
instr = visual.TextStim(win=win, name='instr',
    text='''Jeśli prezentowane obrazki <b_Red>NIE NALEŻĄ</b> do tej samej kategorii, naciśnij <b_Red>LEWY ALT</b> \n
	Jeśli prezentowane sześć obrazków <b_Green>NALEŻY</b> do tej samej kategorii, naciśnij <b_Green>PRAWY ALT</b> \n
    Postaraj się nacisnąć przycisk, tak szybko jak zdecydujesz czy obrazki należą do tej samej kategorii, czy nie.\n
    Teraz czas na krótką sesję treningową.\n
    
    (Naciśnij spację aby przejść do sesji treningowej)''',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=True, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_img = visual.ImageStim(
    win=win,
    name='instr_img', 
    image='instrukcje/trening.jpg', mask=None,
    ori=0, pos=(0, 0), size=(1.3, 0.55),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "routine_4_sec_training"
routine_4_sec_trainingClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='trening wyobrażenie/obrazek/nic?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
priming_3 = visual.ImageStim(
    win=win,
    name='priming_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)



# Initialize components for Routine "nothing_0_5s_training"
nothing_0_5s_trainingClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "cross_training"
cross_trainingClock = core.Clock()
fixat = visual.ShapeStim(
    win=win, name='fixat', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "routine_1"
routine_1Clock = core.Clock()
target_tr = visual.ImageStim(
    win=win,
    name='target_tr', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
filament_1_tr = visual.ImageStim(
    win=win,
    name='filament_1_tr', 
    image=None, mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
filament_2_tr = visual.ImageStim(
    win=win,
    name='filament_2_tr', 
    image=None, mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
filament_3_tr = visual.ImageStim(
    win=win,
    name='filament_3_tr', 
    image=None, mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
filament_4_tr = visual.ImageStim(
    win=win,
    name='filament_4_tr', 
    image=None, mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
filament_5_tr = visual.ImageStim(
    win=win,
    name='filament_5_tr', 
    image=None, mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "break_2s"
break_2sClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
instrukcja = visual.TextStim(win=win, name='instrukcja',
    text='''To już koniec sesji treningowej.
    Teraz zacznie się właściwe badanie, które będzie wyglądało dokładnie tak samo, jak w sesji treningowej.\n
    Jeśli prezentowane obrazki <b_Red>NIE NALEŻĄ</b> do tej samej kategorii, naciśnij <b_Red>LEWY ALT</b> \n
	Jeśli prezentowane sześć obrazków <b_Green>NALEŻY</b> do tej samej kategorii, naciśnij <b_Green>PRAWY ALT</b> \n
    \n(Naciśnij spację aby przejść do sesji właściwej)''',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrukcja_img = visual.ImageStim(
    win=win,
    name='instrukcja_img', 
    image='instrukcje/imagined_priming_2_1.jpg', mask=None,
    ori=0, pos=[0,0], size=(1.4, 0.9),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
    
    
Instruction_2Clock = core.Clock()
instrukcja_2 = visual.TextStim(win=win, name='instrukcja_2',
    text='''
    Teraz czas na drugą część eksperymentu. \n
    Jeśli prezentowane obrazki <b_Red>NIE NALEŻĄ</b> do tej samej kategorii, naciśnij <b_Red>LEWY ALT</b> \n
	Jeśli prezentowane sześć obrazków <b_Green>NALEŻY</b> do tej samej kategorii, naciśnij <b_Green>PRAWY ALT</b> \n
    \n(Naciśnij spację aby przejść do sesji właściwej)''',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instrukcja_2_img = visual.ImageStim(
    win=win,
    name='instrukcja_2_img', 
    image='instrukcje/visual_priming_2_1.jpg', mask=None,
    ori=0, pos=[0,0], size=(1.3, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
    
#Blok 1 -----------------------------------------------------------------------
# Initialize components for Routine "routine_4_sec"
routine_4_secClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
priming = visual.ImageStim(
    win=win,
    name='priming', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "nothing_0_5s"
nothing_0_5sClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "img_2"
img_2Clock = core.Clock()
target = visual.ImageStim(
    win=win,
    name='target', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
filament_1 = visual.ImageStim(
    win=win,
    name='filament_1', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
filament_2 = visual.ImageStim(
    win=win,
    name='filament_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
filament_3 = visual.ImageStim(
    win=win,
    name='filament_3', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
filament_4 = visual.ImageStim(
    win=win,
    name='filament_4', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
filament_5 = visual.ImageStim(
    win=win,
    name='filament_5', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
    
    
    
    # Initialize components for Routine "break_2s"
break_2sClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Teraz czas na krótką przerwę. \n\n(Naciśnij spację gdy będziesz gotowy by kontynuować)\n\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
# BlOK 2 ------------------------------------------------------------------

# Initialize components for Routine "routine_4_sec"
routine_4_sec_2Clock = core.Clock()
text_4_2 = visual.TextStim(win=win, name='text_4_2',
    text='moze teraz',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb255', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
priming_2 = visual.ImageStim(
    win=win,
    name='priming_2', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "nothing_0_5s"
nothing_0_5s_2Clock = core.Clock()
text_2_2 = visual.TextStim(win=win, name='text_2_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_cross"
fixation_cross_2Clock = core.Clock()
cross_2 = visual.ShapeStim(
    win=win, name='cross_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[0,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

img_2_2Clock = core.Clock()
target_2 = visual.ImageStim(
    win=win,
    name='target_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
filament_1_2 = visual.ImageStim(
    win=win,
    name='filament_1_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
filament_2_2 = visual.ImageStim(
    win=win,
    name='filament_2_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
filament_3_2 = visual.ImageStim(
    win=win,
    name='filament_3_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
filament_4_2 = visual.ImageStim(
    win=win,
    name='filament_4_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
filament_5_2 = visual.ImageStim(
    win=win,
    name='filament_5_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)


trial_11Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Teraz czas na krótką przerwę. \n\n (Naciśnij spację aby kontynuować badanie)' ,
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
trial_12Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Teraz czas na krótką przerwę. \n\n (Naciśnij spację aby kontynuować badanie)',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "break_2s"
break_2s_2Clock = core.Clock()
text_3_2 = visual.TextStim(win=win, name='text_3_2',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
#
## Initialize components for Routine "trial"
#trial_2Clock = core.Clock()
#text_7_2 = visual.TextStim(win=win, name='text_7_2',
#    text='Teraz czas na krótką (60 sekund) przerwę. \n\n',
#    font='Arial',
#    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
#    color='black', colorSpace='rgb', opacity=1, 
#    languageStyle='LTR',
#    depth=0.0);


# Initialize components for Routine "END"
ENDClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='To już koniec.\n\n Dziękujemy za udział w badaniu!',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "begining"-------
t = 0
beginingClock.reset()  # clock
frameN = -1
continueRoutine = True
#routineTimer.add(1.000000)

key_resp_7 = event.BuilderKeyResponse()

# update component parameters for each repeat
# keep track of which components have finished
beginingComponents = [start_img,key_resp_7]
for thisComponent in beginingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED



# -------Start Routine "begining"-------
while continueRoutine:
    # get current time
    t = beginingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start* updates
    if t >= 0.0 and start_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_img.tStart = t
        start_img.frameNStart = frameN  # exact frame index
        start_img.setAutoDraw(True)
#    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
#    if start.status == STARTED and t >= frameRemains:
#        start.setAutoDraw(False)
    
    
      # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
#    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
#    if key_resp_7.status == STARTED and t >= frameRemains:
#        key_resp_7.status = FINISHED
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
#            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
#            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begining"-------
for thisComponent in beginingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "training_instruction"-------
t = 0
training_instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
training_instructionComponents = [instr_img, key_resp_3]
for thisComponent in training_instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "training_instruction"-------
while continueRoutine:
    # get current time
    t = training_instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    if t >= 0.0 and instr_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_img.tStart = t
        instr_img.frameNStart = frameN  # exact frame index
        instr_img.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in training_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "training_instruction"-------
for thisComponent in training_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "training_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('training.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_4_sec_training"-------
    t = 0
    routine_4_sec_trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    
#    snakes=['snake1.jpg','snake2.jpg','snake3.jpg','snake4.jpg','snake5.jpg','snake6.jpg']
#    things=['tr1','tr2','tr3','tr4','tr5','tr6','tr7']
    
    if img == 13:
        text_5.text="Wąż"
        priming_3.setImage(None)
    elif img == 14:
        text_5.text="Warzywo"
        priming_3.setImage(None)
    elif img == 33:
        text_5.text="Wąż"
        priming_3.setImage(None)
    elif img == 34:
        text_5.text="Warzywo"
        priming_3.setImage(None)
    elif img == 11:
        priming_3.setImage("snake1.jpg")
        text_5.text=""
    elif img == 12:
        priming_3.setImage("priming_tr.jpg")
        text_5.text=""
    elif img == 31:
        priming_3.setImage("snake1.jpg")
        text_5.text=""
    elif img == 32:
        priming_3.setImage("priming_tr.jpg")
        text_5.text=""

    
    
    
    
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_4_sec_trainingComponents = [text_5, priming_3]
    for thisComponent in routine_4_sec_trainingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_4_sec_training"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_4_sec_trainingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_5.status == STARTED and t >= frameRemains:
            text_5.setAutoDraw(False)
        
        # *priming* updates
        if t >= 0.0 and priming_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            priming_3.tStart = t
            priming_3.frameNStart = frameN  # exact frame index
            priming_3.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if priming_3.status == STARTED and t >= frameRemains:
            priming_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_4_sec_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_4_sec_training"-------
    for thisComponent in routine_4_sec_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "nothing_0_5s_training"-------
    t = 0
    nothing_0_5s_trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    nothing_0_5s_trainingComponents = [text_6]
    for thisComponent in nothing_0_5s_trainingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "nothing_0_5s_training"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = nothing_0_5s_trainingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_6.status == STARTED and t >= frameRemains:
            text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nothing_0_5s_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nothing_0_5s_training"-------
    for thisComponent in nothing_0_5s_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "cross_training"-------
    t = 0
    cross_trainingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    cross_trainingComponents = [fixat]
    for thisComponent in cross_trainingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cross_training"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cross_trainingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixat* updates
        if t >= 0.0 and fixat.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixat.tStart = t
            fixat.frameNStart = frameN  # exact frame index
            fixat.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixat.status == STARTED and t >= frameRemains:
            fixat.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cross_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cross_training"-------
    for thisComponent in cross_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "routine_1"-------
    t = 0
    routine_1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    target_tr.setPos(pos)
    
    
    filaments_tr= [filament_1_tr, filament_2_tr, filament_3_tr, filament_4_tr, filament_5_tr]
    Positions_list_tr=[[-0.3,0],[0.3,0],[-0.15, 0.3],[-0.15, -0.3] ,[0.15, 0.3], [0.15,-0.3]]
    Positions_list_tr.remove(pos)
    filaments_positions_tr=Positions_list_tr
    
    for i in range(len(filaments_positions_tr)):
        selected_pos_tr=random.choice(filaments_positions_tr)
        filaments_positions_tr.remove(selected_pos_tr)
        filaments_tr[i].setPos(selected_pos_tr)


    snakes=['snake1.jpg','snake2.jpg','snake3.jpg','snake4.jpg','snake5.jpg','snake6.jpg']
    things=['tr1.jpg','tr2.jpg','tr3.jpg','tr4.jpg','tr5.jpg','tr6.jpg','tr7.jpg']
    

    if (img==11) or (img==12) or img==13 or img==14:
        target_image_tr=random.choice(snakes)
        target_tr.setImage(target_image_tr)
        snakes.remove(target_image_tr)
        for i in range(5):
            filament_img_tr = random.choice(things)
            things.remove(filament_img_tr)
            filaments_tr[i].setImage(filament_img_tr)
    elif img==31 or img==32 or img==33 or img==34:
        target_image_tr=random.choice(things)
        target_tr.setImage(target_image_tr)
        things.remove(target_image_tr)
        for i in range(5):
            filament_img_tr = random.choice(things)
            things.remove(filament_img_tr)
            print(filaments_tr[i])
            filaments_tr[i].setImage(filament_img_tr)

    
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    routine_1Components = [target_tr, filament_1_tr, filament_2_tr, filament_3_tr, filament_4_tr, filament_5_tr, key_resp_2]
    for thisComponent in routine_1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_1"-------
    while continueRoutine:
        # get current time
        t = routine_1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target_tr* updates
        if t >= 0.0 and target_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_tr.tStart = t
            target_tr.frameNStart = frameN  # exact frame index
            target_tr.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target_tr.status == STARTED and t >= frameRemains:
            target_tr.setAutoDraw(False)
        
        # *filament_1_tr* updates
        if t >= 0.0 and filament_1_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_1_tr.tStart = t
            filament_1_tr.frameNStart = frameN  # exact frame index
            filament_1_tr.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_1_tr.status == STARTED and t >= frameRemains:
            filament_1_tr.setAutoDraw(False)
        
        # *filament_2_tr* updates
        if t >= 0.0 and filament_2_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_2_tr.tStart = t
            filament_2_tr.frameNStart = frameN  # exact frame index
            filament_2_tr.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_2_tr.status == STARTED and t >= frameRemains:
            filament_2_tr.setAutoDraw(False)
        
        # *filament_3_tr* updates
        if t >= 0.0 and filament_3_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_3_tr.tStart = t
            filament_3_tr.frameNStart = frameN  # exact frame index
            filament_3_tr.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_3_tr.status == STARTED and t >= frameRemains:
            filament_3_tr.setAutoDraw(False)
        
        # *filament_4_tr* updates
        if t >= 0.0 and filament_4_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_4_tr.tStart = t
            filament_4_tr.frameNStart = frameN  # exact frame index
            filament_4_tr.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_4_tr.status == STARTED and t >= frameRemains:
            filament_4_tr.setAutoDraw(False)
        
        # *filament_5_tr* updates
        if t >= 0.0 and filament_5_tr.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_5_tr.tStart = t
            filament_5_tr.frameNStart = frameN  # exact frame index
            filament_5_tr.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_5_tr.status == STARTED and t >= frameRemains:
            filament_5_tr.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
#            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED and t >= frameRemains:
            key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['loption', 'roption'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
#                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
#                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_1"-------
    for thisComponent in routine_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
#    # check responses
#    if key_resp_2.keys in ['', [], None]:  # No response was made
#        key_resp_2.keys=None
#    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
#    if key_resp_2.keys != None:  # we had a response
#        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "routine_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "break_2s"-------
    t = 0
    break_2sClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2sComponents = [text_3]
    for thisComponent in break_2sComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "break_2s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2sClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2s"-------
    for thisComponent in break_2sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Instruction"-------
t = 0
InstructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionComponents = [instrukcja_img, key_resp_4]
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = InstructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrukcja* updates
    if t >= 0.0 and instrukcja_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrukcja_img.tStart = t
        instrukcja_img.frameNStart = frameN  # exact frame index
        instrukcja_img.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#Blok 2-------------------------------------------------------------------------------------------------------------------------------



# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('imagined_priming.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_4_sec"-------
    t = 0
    routine_4_sec_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    
    
    if img == 13:
        priming_2.setImage(None)
        text_4_2.text="Pająk"
        
    elif img == 14:
        priming_2.setImage(None)
        text_4_2.text="Grzyb"
        
    elif img == 23:
        priming_2.setImage(None)
        text_4_2.text="Grzyb"
        
    elif img == 24:
        priming_2.setImage(None)
        text_4_2.text="Pająk"
        
    elif img == 33:
        priming_2.setImage(None)
        text_4_2.text="Pająk"
        
    elif img == 34:
        priming_2.setImage(None)
        text_4_2.text="Grzyb"
        
    

    
    # update component parameters for each repeat
    
    # keep track of which components have finished
    routine_4_sec_2Components = [text_4_2, priming_2]
    for thisComponent in routine_4_sec_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_4_sec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_4_sec_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4_2.tStart = t
            text_4_2.frameNStart = frameN  # exact frame index
            text_4_2.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4_2.status == STARTED and t >= frameRemains:
            text_4_2.setAutoDraw(False)
        
        # *priming* updates
        if t >= 0.0 and priming_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            priming_2.tStart = t
            priming_2.frameNStart = frameN  # exact frame index
            priming_2.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if priming_2.status == STARTED and t >= frameRemains:
            priming_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_4_sec_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_4_sec"-------
    for thisComponent in routine_4_sec_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "nothing_0_5s"-------
    t = 0
    nothing_0_5s_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    nothing_0_5s_2Components = [text_2_2]
    for thisComponent in nothing_0_5s_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "nothing_0_5s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = nothing_0_5s_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2_2.tStart = t
            text_2_2.frameNStart = frameN  # exact frame index
            text_2_2.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2_2.status == STARTED and t >= frameRemains:
            text_2_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nothing_0_5s_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nothing_0_5s"-------
    for thisComponent in nothing_0_5s_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_cross"-------
    t = 0
    fixation_cross_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_cross_2Components = [cross_2]
    for thisComponent in fixation_cross_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_cross_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if t >= 0.0 and cross_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross_2.tStart = t
            cross_2.frameNStart = frameN  # exact frame index
            cross_2.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross_2.status == STARTED and t >= frameRemains:
            cross_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_cross_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross"-------
    for thisComponent in fixation_cross_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "img_2"-------
    t = 0
    img_2_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    target_2.setPos(pos)
   
    filaments_2= [filament_1_2, filament_2_2, filament_3_2, filament_4_2, filament_5_2]
    Positions_list_2=[[-0.3,0],[0.3,0],[-0.15, 0.3],[-0.15, -0.3] ,[0.15, 0.3], [0.15,-0.3]]
    Positions_list_2.remove(pos)
    filaments_positions_2=Positions_list_2
    
    for i in range(len(filaments_positions_2)):
        selected_pos_2=random.choice(filaments_positions_2)
        filaments_positions_2.remove(selected_pos_2)
        filaments_2[i].setPos(selected_pos_2)
    
   
    flowers_2=['f1.jpg','f2.jpg','f3.jpg','f4.jpg','f5.jpg','f6.jpg','f7.jpg','f8.jpg','f9.jpg','f10.jpg','f11.jpg','f12.jpg']
    spiders_2=['s1.jpg','s2.jpg','s3.jpg','s4.jpg','s5.jpg','s6.jpg','s7.jpg']
    mushrooms_2=['m1.jpg','m2.jpg','m3.jpg','m4.jpg','m5.jpg','m6.jpg']
    
    
    if   img==13 or img==14:
        target_image_2=random.choice(spiders_2)
        target_2.setImage(target_image_2)
        spiders_2.remove(target_image_2)
        for i in range(5):
            filament_img_2 = random.choice(flowers_2)
            flowers_2.remove(filament_img_2)
            filaments_2[i].setImage(filament_img_2)
    elif  img==23 or img==24:
        target_image_2=random.choice(mushrooms_2)
        target_2.setImage(target_image_2)
        mushrooms_2.remove(target_image_2)
        for i in range(5):
            filament_img_2 = random.choice(flowers_2)
            flowers_2.remove(filament_img_2)
            print(filaments_2[i])
            filaments_2[i].setImage(filament_img_2)
    elif img==33 or img==34:
        target_image_2=random.choice(flowers_2)
        target_2.setImage(target_image_2)
        flowers_2.remove(target_image_2)
        for i in range(5):
            filament_img_2 = random.choice(flowers_2)
            flowers_2.remove(filament_img_2)
            print(filaments_2[i])
            filaments_2[i].setImage(filament_img_2)

   
   
    key_resp_6_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    img_2_2Components = [target_2, filament_1_2, filament_2_2, filament_3_2, filament_4_2, filament_5_2, key_resp_6_2]
    for thisComponent in img_2_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "img_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = img_2_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if t >= 0.0 and target_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            target_2.tStart = t
            target_2.frameNStart = frameN  # exact frame index
            target_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target_2.status == STARTED and t >= frameRemains:
            target_2.setAutoDraw(False)
        
        # *filament_1* updates
        if t >= 0.0 and filament_1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_1_2.tStart = t
            filament_1_2.frameNStart = frameN  # exact frame index
            filament_1_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_1_2.status == STARTED and t >= frameRemains:
            filament_1_2.setAutoDraw(False)
        
        # *filament_2* updates
        if t >= 0.0 and filament_2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_2_2.tStart = t
            filament_2_2.frameNStart = frameN  # exact frame index
            filament_2_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_2_2.status == STARTED and t >= frameRemains:
            filament_2_2.setAutoDraw(False)
        
        # *filament_3* updates
        if t >= 0.0 and filament_3_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_3_2.tStart = t
            filament_3_2.frameNStart = frameN  # exact frame index
            filament_3_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_3_2.status == STARTED and t >= frameRemains:
            filament_3_2.setAutoDraw(False)
        
        # *filament_4* updates
        if t >= 0.0 and filament_4_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_4_2.tStart = t
            filament_4_2.frameNStart = frameN  # exact frame index
            filament_4_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_4_2.status == STARTED and t >= frameRemains:
            filament_4_2.setAutoDraw(False)
        
        # *filament_5* updates
        if t >= 0.0 and filament_5_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_5_2.tStart = t
            filament_5_2.frameNStart = frameN  # exact frame index
            filament_5_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_5_2.status == STARTED and t >= frameRemains:
            filament_5_2.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6_2.tStart = t
            key_resp_6_2.frameNStart = frameN  # exact frame index
            key_resp_6_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_6_2.status == STARTED and t >= frameRemains:
            key_resp_6_2.status = FINISHED
        if key_resp_6_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['loption', 'roption'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6_2.rt = key_resp_6_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in img_2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "img_2"-------
    for thisComponent in img_2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6_2.keys in ['', [], None]:  # No response was made
        key_resp_6_2.keys=None
    trials_3.addData('key_resp_6_2.keys',key_resp_6_2.keys)
    if key_resp_6_2.keys != None:  # we had a response
        trials_3.addData('key_resp_6_2.rt', key_resp_6_2.rt)
    
    # ------Prepare to start Routine "break_2s"-------
    t = 0
    break_2s_2Clock.reset()  # clock
    frameN = -1
    
    continueRoutine = True
    
    
    routineTimer.add(2.000000)
    
    
    
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2s_2Components = [text_3_2]
    for thisComponent in break_2s_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "break_2s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2s_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3_2.tStart = t
            text_3_2.frameNStart = frameN  # exact frame index
            text_3_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3_2.status == STARTED and t >= frameRemains:
            text_3_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2s_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2s"-------
    for thisComponent in break_2s_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
     # ------Prepare to start Routine "trial"-------
    t = 0
    trial_11Clock.reset()  # clock
    frameN = -1
    if trials_3.thisN != 47:
        continueRoutine = False
    else:
        continueRoutine = True
    
    # update component parameters for each repeat
    key_resp_11 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial_11Components = [text_11, key_resp_11]
    for thisComponent in trial_11Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trial_11Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        
      
            
        
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_11.clock.reset)
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 0.0- win.monitorFramePeriod * 0.75
        if t >= frameRemains:
            if key_resp_11.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
            
    
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if t>=frameRemains:
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_11.rt = key_resp_11.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trial_11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    

    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#Koniec Bloku 2-----------------------------------------------------------

# ------Prepare to start Routine "trial"-------
t = 0
trialClock.reset()  # clock
frameN = -1

continueRoutine = True

# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
trialComponents = [text_7, key_resp_5]
for thisComponent in trialComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
  
        
    
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)
        event.clearEvents(eventType='keyboard')
    frameRemains = 0.0 + 10.0- win.monitorFramePeriod * 0.75
    if t >= frameRemains:
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
        

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if t>=frameRemains:
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#pownowna instrukcja

# ------Prepare to start Routine "Instruction"-------
t = 0
Instruction_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Instruction_2Components = [instrukcja_2_img, key_resp_8]
for thisComponent in Instruction_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
while continueRoutine:
    # get current time
    t = Instruction_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrukcja* updates
    if t >= 0.0 and instrukcja_2_img.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrukcja_2_img.tStart = t
        instrukcja_2_img.frameNStart = frameN  # exact frame index
        instrukcja_2_img.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in Instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



#Blok 1 --------------------------------------------------------------------------------------------------------------------------

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Visual_prime.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_4_sec"-------
    t = 0
    routine_4_secClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    
    
    if img == 11:
        priming.setImage("mushroom_priming1.jpg")
        text_4.text=""
    elif img == 12:
        priming.setImage("spider_priming1.jpg")
        text_4.text=""
    elif img == 21:
        priming.setImage("mushroom_priming1.jpg")
        text_4.text=""
    elif img == 22:
        priming.setImage("spider_priming1.jpg")
        text_4.text=""
    elif img == 31:
        priming.setImage("spider_priming1.jpg")
        text_4.text=""
    elif img == 32:
        priming.setImage("mushroom_priming1.jpg")
        text_4.text=""

    
    # update component parameters for each repeat
    
    # keep track of which components have finished
    routine_4_secComponents = [text_4, priming]
    for thisComponent in routine_4_secComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "routine_4_sec"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = routine_4_secClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)
        
        # *priming* updates
        if t >= 0.0 and priming.status == NOT_STARTED:
            # keep track of start time/frame for later
            priming.tStart = t
            priming.frameNStart = frameN  # exact frame index
            priming.setAutoDraw(True)
        frameRemains = 0.0 + 4.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if priming.status == STARTED and t >= frameRemains:
            priming.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_4_secComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_4_sec"-------
    for thisComponent in routine_4_secComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "nothing_0_5s"-------
    t = 0
    nothing_0_5sClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    nothing_0_5sComponents = [text_2]
    for thisComponent in nothing_0_5sComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "nothing_0_5s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = nothing_0_5sClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_2.status == STARTED and t >= frameRemains:
            text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nothing_0_5sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "nothing_0_5s"-------
    for thisComponent in nothing_0_5sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "fixation_cross"-------
    t = 0
    fixation_crossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.800000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_crossComponents = [cross]
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_crossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        if t >= 0.0 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.setAutoDraw(True)
        frameRemains = 0.0 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross"-------
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "img_2"-------
    t = 0
    img_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    target.setPos(pos)
   
    filaments= [filament_1, filament_2, filament_3, filament_4, filament_5]
    Positions_list=[[-0.3,0],[0.3,0],[-0.15, 0.3],[-0.15, -0.3] ,[0.15, 0.3], [0.15,-0.3]]
    Positions_list.remove(pos)
    filaments_positions=Positions_list
    
    for i in range(len(filaments_positions)):
        selected_pos=random.choice(filaments_positions)
        filaments_positions.remove(selected_pos)
        filaments[i].setPos(selected_pos)
    
   
    flowers=['f1.jpg','f2.jpg','f3.jpg','f4.jpg','f5.jpg','f6.jpg','f7.jpg','f8.jpg','f9.jpg','f10.jpg','f11.jpg','f12.jpg']
    spiders=['s1.jpg','s2.jpg','s3.jpg','s4.jpg','s5.jpg','s6.jpg','s7.jpg']
    mushrooms=['m1.jpg','m2.jpg','m3.jpg','m4.jpg','m5.jpg','m6.jpg']
    
    
    if (img==11) or (img==12):
        target_image=random.choice(spiders)
        target.setImage(target_image)
        spiders.remove(target_image)
        for i in range(5):
            filament_img = random.choice(flowers)
            flowers.remove(filament_img)
            filaments[i].setImage(filament_img)
    elif (img==21) or (img==22):
        target_image=random.choice(mushrooms)
        target.setImage(target_image)
        mushrooms.remove(target_image)
        for i in range(5):
            filament_img = random.choice(flowers)
            flowers.remove(filament_img)
            print(filaments[i])
            filaments[i].setImage(filament_img)
    elif img==31 or img==32:
        target_image=random.choice(flowers)
        target.setImage(target_image)
        flowers.remove(target_image)
        for i in range(5):
            filament_img = random.choice(flowers)
            flowers.remove(filament_img)
            print(filaments[i])
            filaments[i].setImage(filament_img)

   
   
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    img_2Components = [target, filament_1, filament_2, filament_3, filament_4, filament_5, key_resp_6]
    for thisComponent in img_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "img_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = img_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if t >= 0.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t
            target.frameNStart = frameN  # exact frame index
            target.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target.status == STARTED and t >= frameRemains:
            target.setAutoDraw(False)
        
        # *filament_1* updates
        if t >= 0.0 and filament_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_1.tStart = t
            filament_1.frameNStart = frameN  # exact frame index
            filament_1.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_1.status == STARTED and t >= frameRemains:
            filament_1.setAutoDraw(False)
        
        # *filament_2* updates
        if t >= 0.0 and filament_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_2.tStart = t
            filament_2.frameNStart = frameN  # exact frame index
            filament_2.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_2.status == STARTED and t >= frameRemains:
            filament_2.setAutoDraw(False)
        
        # *filament_3* updates
        if t >= 0.0 and filament_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_3.tStart = t
            filament_3.frameNStart = frameN  # exact frame index
            filament_3.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_3.status == STARTED and t >= frameRemains:
            filament_3.setAutoDraw(False)
        
        # *filament_4* updates
        if t >= 0.0 and filament_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_4.tStart = t
            filament_4.frameNStart = frameN  # exact frame index
            filament_4.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_4.status == STARTED and t >= frameRemains:
            filament_4.setAutoDraw(False)
        
        # *filament_5* updates
        if t >= 0.0 and filament_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            filament_5.tStart = t
            filament_5.frameNStart = frameN  # exact frame index
            filament_5.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if filament_5.status == STARTED and t >= frameRemains:
            filament_5.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_6.status == STARTED and t >= frameRemains:
            key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['loption', 'roption'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in img_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "img_2"-------
    for thisComponent in img_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    
    # ------Prepare to start Routine "break_2s"-------
    t = 0
    break_2sClock.reset()  # clock
    frameN = -1
    
    continueRoutine = True
    
    
    routineTimer.add(2.000000)
    
    
    
    # update component parameters for each repeat
    # keep track of which components have finished
    break_2sComponents = [text_3]
    for thisComponent in break_2sComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "break_2s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = break_2sClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2s"-------
    for thisComponent in break_2sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            
    
     # ------Prepare to start Routine "trial"-------
    t = 0
    trial_12Clock.reset()  # clock
    frameN = -1
    if trials.thisN != 47:
        continueRoutine = False
    else:
        continueRoutine = True
    
    # update component parameters for each repeat
    key_resp_12 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial_12Components = [text_12, key_resp_12]
    for thisComponent in trial_12Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trial_12Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        
      
            
        
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_12.tStart = t
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_12.clock.reset)
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 0.0- win.monitorFramePeriod * 0.75
        if t >= frameRemains:
            if key_resp_12.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
            
    
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if t>=frameRemains:
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_12.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_12.rt = key_resp_12.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trial_12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    

    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

#Koniec Blok 1 ---------------------------------------------------------------------------------------------------------------------


# ------Prepare to start Routine "END"-------
t = 0
ENDClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [text]
for thisComponent in ENDComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "END"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ENDClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
