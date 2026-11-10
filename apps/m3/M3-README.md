# Milestone-3
Sample program of this version is stored in apps/m3

# REFACTOR
Soup Replacer now uses event hooks on_start() and on_end() to apply changes to a tag inside of handle_starttag and handle_endtag

# FEATURES
- Added name_xformer as a new optinal parameter of SoupReplacer, which takes in an user-defined function to return the new name for a tag.
- Added attrs_xformer as a new optional parameter of SoupReplacer, which similarly takes in an user-defined function to return the new attributes for a tag.
- Added xformer as a new optional parameter of SoupReplacer, which takes an user-defined logic and make transformation to the tag in place.

# BRIEF
Compared to M2, M3 exercises more on the understanding of how Beautiful Soup handles the tags before they are passed into the builders and also on how each different parsers treat a document (for example, html_parser only reports what it sees, igonoring any misbehaviors, but lxml parser will repair a document if it has any mismatched or stray tags hanging). The tasks in the milestone also tests developer's ability to design a system and imagine how a piece of API should live in a project, what should be stored for the new class object and what should be hidden, using abstraction and encapasulation. The new library should ultimately match the behaviors of the original code base that it works on, in the case of SoupReplacer, start and end event hooks are made to match handle_starttag and handle_endtag by saving the state of the tags at start hook and releasing them at end hook to preserve their data, and all transformation are hidden and done in SoupReplacer class to maintain cleaner code and make the API easy to use.