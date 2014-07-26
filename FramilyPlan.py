import sublime, sublime_plugin, os, glob, re

class FindFamilyCommand(sublime_plugin.WindowCommand):
    def run(self):
        FramilyFileFinder(sublime.active_window(), 'family').run()

# next on the list to implament
# class FindFriendsCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         FramilyFileFinder(sublime.active_window(), 'friends').run()


class FramilyMember:
    def __init__(self, title, path):
        self.title = title
        self.path = path

    def __hash__(self):
        return hash(self.path)

    def __contains__(self):
        return self.path

    def __cmp__(self, other):
        return cmp(self.path, other.path)

    def to_array(self):
        return [self.title, self.path]


class FramilyFileFinder:

    def __init__(self, window, framily_type):
        # current window
        self.window = window

        # an array of FramilyMembers
        self.framily_members = []

        # all the settings in the settings file
        self.all_settings = sublime.load_settings("framily_language.sublime-settings")

        # current files file path
        self.opened_file = self.window.active_view().file_name()

        # base path for search
        self.base_path = self.find_base_path()

        # settings for all framily members
        self.framily = self.get_framily_settings(framily_type, self.window.active_view().settings().get('syntax').split("/")[1])
        if self.framily:
            # get the base name to perform search
            self.base_name = self.determine_base_name()
            if (self.base_name):
                self.get_framily()
        self.framily_array = self.get_framily_array()

    def run(self):
        if self.valid_framily:
            sublime.active_window().show_quick_panel(self.get_framily_array(), self.whenDone)


    # Called to open the file in the list that was selected
    def whenDone(self, index):
        try:
            if index > -1:
                print self.framily_array[index][1]
                self.window.open_file(self.base_path + self.framily_array[index][1])
        except:
            print "not opening file"   


    def valid_base_name(self):
        return not not (self.framily and self.base_name)

    def valid_framily(self):
        return not not self.framily_members

    def convertFileNameToTitle(self, filePath):
        splitPath = filePath.split("/")
        new_title = splitPath[-1].replace(self.base_name, "")
        return " ".join((" ".join(new_title.split("_"))).split(".")).title()

    def get_glob_framily(self, member):
        real_glob_return = []
        glob_return =  glob.glob(self.base_path + "/" + member['prepend'] + self.base_name + member['append'])
        for glober in glob_return:
            title = member['title'].replace('*', self.convertFileNameToTitle(glober))
            new_member = FramilyMember(title, glober)
            if new_member not in self.framily_members:
                real_glob_return.append(FramilyMember(title, glober.replace(self.base_path, "")))
        return real_glob_return


    def get_framily(self):
        for member in self.framily:
            glob_return =  self.get_glob_framily(member)
            if glob_return:
                self.framily_members += glob_return
            else:
                exists_return = os.path.exists(self.base_path + "/" + member['prepend'] + self.base_name + member['append'])
                if exists_return:
                    self.framily_members.append(FramilyMember(member['title'], exists_return.replace(self.base_path, "")))


    def get_framily_array(self):
        framily_array = []
        for member in self.framily_members:
            framily_array.append([member.title, member.path])
        return framily_array


    def get_framily_settings(self, framily_type, language):
        settings = self.all_settings.get(framily_type)
        if settings:
            settings = settings.get(self.base_path)
            if not settings:
                settings = self.all_settings.get(language)
            if settings:
                return settings['members']
            else:
                return False


    def find_base_path(self):
        folders = sublime.active_window().folders()

        for folder in folders:
          if folder in self.opened_file and os.path.exists(os.path.join(folder, self.all_settings.get('base'))):
            return os.path.abspath(folder)


    def determine_base_name(self):
        found_member = "this_is_an_abserdly_long_text_field_so_that_the_algorithm_works"

        for member in self.framily:
            match_member = re.search('.+' + re.escape(member['prepend']) + '(.+?)' + re.escape(member['append']), self.opened_file)
            if match_member:
                if (len(found_member) > len(match_member.group(1))):
                    found_member = match_member.group(1)

        if (found_member != "this_is_an_abserdly_long_text_field_so_that_the_algorithm_works"):
            return found_member
        else:
            return False