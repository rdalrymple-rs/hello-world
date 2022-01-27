#------------ GIT COMMANDS USED TO CREATE NEW BRANCH AND ADD THIS FILE ------------#

# cd hello-world                            ## Move to directory of the git repo.
# git checkout -b richard                   ## Create new branch of name "richard"
                                            #   and switch to this new branch.
# git add richards_script.py                ## After creating this file (called
                                            #   richards_script.py) add it to the
                                            #   git upstream to be commited.
# git commit -m "Added file"                ## Commit any changes that were added
                                            #   with the "git add" command and
                                            #   give a brief message of what these
                                            #   changes are.
# git push --set-upstream origin richard    ## Push the committed changes, while
                                            #   setting the upstream to be "origin"
                                            #   within "richard" branch.
#----------------------------------------------------------------------------------#

if __name__ == "__main__":
    print("This is Richard's branch to make changes in")