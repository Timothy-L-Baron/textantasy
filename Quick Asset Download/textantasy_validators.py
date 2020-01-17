#validators

#universal validator
def universal_validator_1(answer, lst):
    #it will check to see if the answer provided is  in a specified list
    while True:
        if answer in lst:
            #print(answer)
            return answer
        else:
            answer = input('\nPlease choose a valid response: ')
