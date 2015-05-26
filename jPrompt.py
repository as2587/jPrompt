import time
import random
import os
#commands:
#qq -> immediate quit. Append all previous answers to Journal file
#Ask all questions

promptQ = []
promptQ.append('What is your favorite song now?')
promptQ.append('What are you currently doing?')
promptQ.append('Most interesting things on reddit?')
promptQ.append('Latest Jimmy Fallon or John Oliver video?')
promptQ.append('What\'s the weather like?')
promptQ.append('What is the main thin on your mind?')
promptQ.append('What (and when) is the main thing you\'re looking forward to?')
promptQ.append('How\'s the gym/fitness been going?')


def runPrompts(filename):
    #TODO: start timer and print result
    startT = time.time()
    resp = ''
    allresp = ''
    completedID = []
    while not (resp == 'qq'):
        allresp = allresp+resp + '\n\n'
        
        if len(completedID)<len(promptQ): 
            promptID = random.randint(0, len(promptQ)-1)
            while (promptID in completedID):
                 promptID = random.randint(0, len(promptQ)-1)
                 
            currPrompt = promptQ[promptID] + "\n"
            completedID.append(promptID)
        else:
            currPrompt = "I'm all out of questions... type away: \n"
            
    
        
        resp = raw_input(currPrompt)
        print ''
    allresp = allresp + '\n\n'
    
    #Save everything
    currentTime = time.strftime('%c')
    f = open(filename, 'a')
    f.write(currentTime)
    f.write('\n')
    f.write(allresp)
    f.write('\n')
    f.close()
    totTime = time.time() - startT
    print 'Journal saved! That took: ' + str(int(totTime)) + ' sec'



if __name__ == "__main__":
    #Get filename 
    #TODO: arguments to get file name
    jName = 'main.txt'
    fullName =  os.path.dirname(os.path.abspath(__file__)) + '/' + jName
    runPrompts(fullName)
    