import sublime, sublime_plugin

class FindFramilyCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, "Hello, World!")

class LanguagePreferences:
    languageName = ""
    bread = []

    def setBread (brd):
        self.bread = brd

    #Take a filepath and find the indexes that match finding the first in the lists
    def matchToBread (thing):
        return true

    #Take a filepath and find the indexes that match finding all in the lists
    def matchAllBread (thing):
        return true

class FileChecker:

    # checks if the given name and path if an actual file
    @staticmethod
    def isValidFile(fileNameAndPath):
        return true

    # Returns a new list of file names and paths that are actual files
    @staticmethod
    def returnOnlyValid(listOfFileNamesAndPaths):
        return true





class TestingStuffCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print "testing"






        line = "/Users/Thomas/Projects/Redspot/app/controllers/api/par_levels_controller.rb"

        matchObj = re.search('(.+?)' + re.escape('api/') + '(.+?)', line) #api(.+?)rb
        if matchObj:
           print "match --> matchObj.group(1) : ", matchObj.group(2)
        else:
           print "No match!!"

        fileNameSpecials = ['_finder.rb', '_controller.rb', 's_controller.rb', '_oracle.rb', '_type.rb', '_saver.rb']
        railsFolders = ["models/", "controllers/", "views/", "finders/", "oracles/", "savers/"]

        for fns in fileNameSpecials:
            print fns
            matchObj = re.search(re.escape('api/') + '(.+?)' + re.escape(fns), line) #api(.+?)rb
            if matchObj:
               print "match --> matchObj.group(1) : ", matchObj.group(1)
            else:
               print "No match!!"


