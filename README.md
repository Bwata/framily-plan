# Sublime Text 2 Plugin: FramilyPlan

This is a sublime plug in to find similar files based on your predefined standard naming structures.

##How To use it:

I set the standard key binding to ctrl + F and a list of similar files will show up.

But you may ask what are the similar files? Well, kind lady (or sir) it is up to you and you OCD naming structure.

All of the dirty framily secrets happen in the framily-plan.sublime-settings file. You will see a (probably confusing) structure defining how this plug in finds the similar files. So lets walk through it to configure it for yourself.

What is the Framily (in this plugin):
  Your Framily:
    Files in a project that are similar to the one that you have open and focus now.
  Your Family:
    Files that have the same base name like 'user' but are different files. Like a rails application has user.rb and users_controller.rb. These files are in the same family.
  Your Friends:
    This is a future feature but when it gets made they will be files that have different base names but have similar "purposes". Again, to use a rails application you may have a users_controller.rb and a items_controller.rb and these files would be friends.


The "base": 
  the name of a folder or file that will always be in the root folder of all your projects you want to use this plugin for, I set the default to ".git" because well, it's git.

The "family":
  These are setting for files that are family members as described above.

  The language or project:
    In the friends or family you specify a language or project that the family belongs to. The language is base on the way Sublime performs the syntax on the current visibal file. 

The "friends":
  Again not built yet but will be similar to family.




