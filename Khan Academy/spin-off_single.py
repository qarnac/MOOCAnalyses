import urllib
import re

# you can change this total_num to adjust the number of follower you want to analyze 
total_num = 50
# link
url = "https://www.khanacademy.org/api/labs/scratchpads/848372201/top-forks?casing=camel&sort=1&limit="+str(total_num)+"&page=0&lang=en&_=1366703615516"
# regular expression:
regex_lists_index= ["Title", "Nick_name", "Sum_votes", "Link"]
regex_lists = ['"title": "(.+?)", "translatedTitle"','"authorNickname": (.+?)}','"sumVotesIncremented": (.+?), "thumb"','{"url": "(.+?)", "sumVotesIncremented"']
# open the website and read content into buffer 
htmltext = urllib.urlopen(url).read()

def scrape_result(index):
    regex = regex_lists[index]
    pattern = re.compile(regex)
    links = re.findall(pattern, htmltext)
    return links

def main():
    # get result one by one, save into result1, result2....
    for j in range(len(regex_lists_index)):
        locals()['result'+str(j)] = scrape_result(j)

    # create a new file result.txt. result will be saved
    new_file = open('result.txt', 'w')
    for i in range(total_num):
        print_out = str("["+str(i+1)+"] Title:"+str(locals()['result'+str(0)][i])+"; Nick Name:"+str(locals()['result'+str(1)][i])+"; Sum Votes:"+str(locals()['result'+str(2)][i])+"; Link:"+str(locals()['result'+str(3)][i]))
        print print_out
        new_file.write(print_out+"\n")
    # close the file
    new_file.close()

if __name__ == "__main__":
    main()
