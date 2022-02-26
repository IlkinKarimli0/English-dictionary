import mysql.connector
from difflib import get_close_matches

#connection to database

connection = mysql.connector.connect(
    user= "Username", 
    password= "Password"   ,
    host=  "Host"  , 
    database=  "DB"   ,
)
#-------------------------------------------------

word =  str(input("Enter the word: ")).lower()

#-------------------------------------------------


#getting data from database

def connect_to_words(query):
    """connect to data from Php server 
    param query : mySQL code for finding the data from php server
    ex: SERVER *FROM Dictionary getting all server 
    ex: SERVER *FROM Dictionary WHERE Expression = word(changagbe) 
    as a result it return the tuples what is consists of the word and definition of it
    """
    
    cursor = connection.cursor()

    cursor.execute(query) 

    results = cursor.fetchall()

    return results

#-----------------------------------------------------------
lst_of_keys = list(result[0] for result in connect_to_words("SELECT *FROM Dictionary"))
#------------------------------------------------------------------------------------------
def translate(word):
    query = " SELECT *FROM Dictionary WHERE Expression = '%s' " %word
    results = connect_to_words(query)
    lst_of_keys = list(result[0] for result in connect_to_words("SELECT *FROM Dictionary"))
    best_matched_list = get_close_matches(word,lst_of_keys)
    if results:
        result = list(result[1] for result in results)
        return result  
    elif best_matched_list: 
        correction_of_word = str(input("Did you mean '%s'instead( ANSWER with [Y]   [N] "%best_matched_list[0]))
        if correction_of_word.lower() == "y":
            return translate(best_matched_list[0])
        elif correction_of_word.lower() == "n":
            out_list = list(frozenset(best_matched_list))
            g_c_m = best_matched_list[0] 
            while g_c_m in out_list:    
                out_list.remove(g_c_m)
            print("\n The word '"+ word +"' does not exist")
            print("\n You can check instead :")  
            count = 0 #making a count variabla in order to make option for choosing word among the best matched words
            if len(out_list) > 1:
                for c in range(0,len(out_list)):
                    count += 1
                    print(count,end=" ")
                    print(out_list[c])
                answer = int(input("Write number of the words that you wanna  : "))
                if out_list[answer-1]:
                    return translate(out_list[answer-1])
                else:
                    pass
            elif len(out_list) == 1 :
                print("1" , out_list[0])
                answer = input("do you wanna to search this word?   [Y]    [N]   : ")
                if answer.lower() == "y":
                    return translate(out_list[0])
                else:
                    pass
            else:
                return "there no statement like that"
            return " "  
        else:
            return "there no statement like that"
    elif word.upper() in lst_of_keys:
        return translate(word.upper())
    elif word.title() in lst_of_keys:#cheking for some special nouns
        return translate(word.title())
    else:
        return "This word is not exist"


def output(word):
    output = translate(word)
    if not isinstance(output,str):
        for i in output:
            print("\n" , i)
    else:
        print("\n" , output)


if __name__ == "__main__":
    output(word)
