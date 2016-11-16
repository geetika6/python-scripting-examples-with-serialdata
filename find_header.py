import sys
def find_header(stream_data):
    header_start="a5"
    num_times_to_check=5
    times_to_check=0
    offset=4
    print stream_data[0]
    next_match=None
    first_match=None
    for index,val in enumerate(stream_data):
        if stream_data[index]==header_start :
             print index
             if first_match==None :
                 first_match=index
                 print "first_match1",first_match  
                 print "next_match1",next_match  
             elif first_match :
                 next_match=index
                 print "first_match",first_match  
                 print "next_match",next_match  
                 if (next_match-first_match)==offset:
                     times_to_check= times_to_check +1 
                     print "times",times_to_check  
             if times_to_check ==num_times_to_check :
                 print "first_index",next_match-(offset*times_to_check)  
                 break
             else :
                 if next_match :
                    first_match=next_match
list_data=['b3','b1','a5','b1','a5','23','23','24','a5','34','35','36','a5','45','46','47','a5','23','23','24','a5','34','35','36','a5','45','46','47','a5']
print list_data[0]    
find_header(list_data)
 
