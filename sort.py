import re
import os

f  = open('input.txt', 'r')
#print('test')


def readBlock(file):
    p_empty = re.compile('^[\s]+$')
    p_tag = re.compile('^\s*###[\s]*(.+)\s$')

    new_person = ''
    new_person_check = 0

    person = ''
    block = ''
    tags = []

    i = 0

    blocks = {}

    for line in file:
        #if(i < 20):
        #    i += 1
        #else:
        #    break
        
        #print ('1. zeile')
        if(p_empty.match(line)):

            if(new_person_check == 1):
                person = '' + new_person
                print ('Neue Person: ' + person)
            new_person_check = 0
            new_person = ''
            
            
            
            #print ('2.    leere Zeile')
            if(len(tags) > 0):
                block = person + block
            for tag in tags:
                try:
                    blocks[tag].append(block)
                except:
                    blocks[tag] = []
                    blocks[tag].append(block)
                    
            #End the last Block
            block = ''
            tags = []
        elif(p_tag.match(line)):
            m = p_tag.match(line)
            tags.append(m.group(1).strip())
            #print ('2.    Tag: ' + m.group(1))

            if(new_person_check > 0):
                new_person_check += 1
        else:
            block += line
            #print ('2.    Text')

            new_person = line
            new_person_check += 1

    return blocks



def writeBlocksToFile(blocks):
    if not os.path.exists('output/'):
        os.makedirs('output/')
    
    for tag in blocks:
        s = 'output/' + tag + '.txt'
        w  = open(s, 'w')

        w.write(tag)
        w.write('\n')
        w.write('\n')

        for block in blocks[tag]:
            w.write(block)
            w.write('(' + tag + ')')
            w.write('\n')

        w.write('\n')
        w.write('\n')
        w.close()
        

blocks = readBlock(f)
writeBlocksToFile(blocks)
