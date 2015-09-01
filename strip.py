import re, sys, os

def main(argv):

    # input validation
    if len(argv) != 2:
        print "Usage: python linkstrip.py <filename>"
        sys.exit(1)

    FOLDER = 'links' # folder to place links in - Created if doesn't exist.
	
    # input file
    emailfname = argv[1]
    email = open(emailfname, 'r')
    text = email.read()

    # extract urls
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    # create directory
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

    # output file
    linksfname = './' + FOLDER + '/' + os.path.splitext(emailfname)[0] + '_links.txt'
    links = open(linksfname, 'w+')

    # loop thru urls
    for url in urls:
        links.write(url)
        links.write('\n')

    # close files
    email.close()
    links.close()

if __name__ == '__main__':
    main(sys.argv)