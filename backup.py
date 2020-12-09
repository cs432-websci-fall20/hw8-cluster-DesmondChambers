import fnmatch
import os
import re

all_tweets_dict = {}

for file in os.listdir('./tweets/'):
    try:
        #if fnmatch.fnmatch(file, '*.txt'):
        print(file)
        my_file = open(f"./tweets/{file}", "r")
        content = my_file.read()
        globals()['{}'.format(file)] = content.split()
        my_file.close()
        #print(content_list)
        #for word in globals()[file]:
        all_tweets_dict['{}'.format(file)] = globals()['{}'.format(file)]
    except:
        continue
        
print(len(all_tweets_dict))

import re

clean_tweets_dict = {}
temp_list = []  

def clean_up(title, list): 
    for word in list:
        try:
            result = re.sub(r"http\S+", "", "{}".format(word.strip()))
            result = re.sub(r"@\S+", "", "{}".format(result.strip()))
            result = result.replace('"','')
            test = ''.join(letter for letter in result.lower() if 'a' <= letter <= 'z')
            #print(test)
            if not len(test)<3 and not len(test) > 15:
                item = str(test)
                #print(test)
                temp_list.append(item)
        except:
            continue
    #globals()['{}'.format(word)]
    #all_clean_tweets['{}' .format(title)] = temp_list
    return temp_list

    #while("" in globals()['{}'.format(word)]) : 
        #globals()['{}'.format(word)].remove("") 
    #print(word)
    #print(len(globals()['{}'.format(word)]))
    #print(newlist)
    #all_clean_tweets.append(globals()['{}'.format(word)])

if __name__ == '__main__':
    for key, val in all_tweets_dict.items():   
        clean_tweets_dict['{}'.format(key)] = clean_up(key, val)
        #clean_up(key, val)"