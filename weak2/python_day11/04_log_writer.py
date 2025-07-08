def log(message):
    with open('log.txt', 'a') as file:
        file.write(message + '\n')

log("program started" )
log("User Logged in")
log("User performed an action")
log("program ended")
