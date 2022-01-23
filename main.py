import re
import long_responses as long
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    percentage = float(message_certainty) / float(len(recognised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #sample responses
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!, Have a nice day!', ['bye', 'goodbye'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Vasavi College Of Engineering is located in Ibrahimbagh ,Hyderabad',['where', 'is','vasavi', 'college','located'],required_words=['vasavi','where'])
    response('A++ GRADING', ['what', 'is', 'the', 'naac', 'grading', 'of', 'vasavi'], required_words=['what', 'naac'])
    response('201', ['what', 'is', 'nirf', 'ranking'], required_words=['what', 'nirf'])
    response('486', ['how', 'many', 'net', 'selections', 'in', 'placements'],required_words=['how', 'selections', 'placements'])
    response('82.65', ['what', 'is', 'the', 'percentage', 'of', 'selected', 'in', 'placement'],required_words=['what', 'percentege', 'selected'])
    response('Osmania University', ['vasavi', 'is', 'affiliated', 'to'], required_words=['vasavi', 'affiliated'])
    response('1981', ['vasavi', 'founded', 'in', 'which', 'year'], required_words=['founded', 'year'])
    response('private institute', ['which', 'type', 'of', 'institute'], required_words=['type', 'institute'])
    response('Dr.S.V.Ramana is the principal of vasavi college of engineering', ['who', 'is', 'the', 'principal', 'of', 'vasavi','vce'], required_words=['principal'])
    response('Dr.K.Ram Mohan rao is the HOD of IT Department', ['who', 'is', 'the', 'HOD', 'of', 'IT', 'department'], required_words=['hod', 'it'])
    response('Dr.B.Sridhar is the HOD of civil Department', ['who', 'is', 'the', 'HOD', 'of', 'civil', 'department'], required_words=['hod', 'civil'])
    response('Dr.E.Sreenivasa is the HOD of ECE Department', ['who', 'is', 'the', 'HOD', 'of', 'ECE', 'department'],required_words=['hod', 'ece'])
    response('Dr.M.Chakravarthy is the HOD of EEE Department', ['who', 'is', 'the', 'HOD', 'of', 'EEE', 'department'],required_words=['hod', 'eee'])
    response('Dr.T.Ram Mohan rao is the HOD of Mechanical Department', ['who', 'is', 'the', 'HOD', 'of', 'mech', 'department'], required_words=['hod', 'mech'])
    response('There are 8 departments in vce', ['how', 'many', 'departments', 'are', 'there', 'in', 'vasavi'],required_words=['how', 'departments'])
    response('OOP and DS', ['what', 'are', 'different', 'core','subjects', 'in', 'IT and CSE'], required_words=['what','subjects', 'IT and CSE'])
    response('Networks analysis and Electronic devices', ['what','are', 'different', 'core', 'subjects', 'in', 'ECE'],required_words=['what', 'subjects', 'ECE'])
    response('Electrical Network Analysis and Electromagnetic FielTheory', ['what','are', 'different', 'core', 'subjects', ' in ','EEE'], required_words = ['what', 'subjects', 'EEE'])
    response('Geology and Surveying', ['what', 'are', 'different','core', 'subjects', 'in', 'Civil'], required_words=['what','subjects', 'Civil'])
    response('Mechanics of Materials and Materials Engineering',['what', 'are', 'different', 'core', 'subjects', 'in','Mechanics'], required_words = ['what', 'subjects', 'Mechanics'])
    response('+914023146003', ['what', 'is', 'the','college', 'landline number', '?'], required_words=['landline'])
    response('Vasavi college gives admissions through EAMCET and JEE mains', ['what ', 'are', 'different', 'categories', 'of', 'admissions', 'available', 'in', 'vasavi college'], required_words = ['what', 'join' ])
    response('https://vce.ac.in',['what','is','the','college','website'],required_words = ['website'])
    response('https://maps.app.goo.gl/GuDFXL4HpyQkic8m6',['what','is','the','route','map','for','vasavi','college'],required_words = ['map'])
    response('VCE conducts online exams on moodle platform',['where','do','you','counduct','online','exams'],required_words = ['online','exams'])
    response('https://moodle.vce.ac.in',['what','is','the','link','for','moodle','platform'],required_words = ['link','moodle'])
    response('Mr. M. Ravi Kumar is the librarian of vce',['who', 'is', 'the', 'librarian', 'of', 'vasavi','vce'], required_words=['librarian'])
    response('+914023146095',['what', 'is', 'the','college', 'library', 'number'], required_words=['library','number'])
    response('library@staff.vce.ac.in',['what', 'is', 'the', 'college', 'library', 'email'], required_words = ['library', 'email'])
    response('500089 is the pincode of vce',['what','is','the','pincode','of','vasavi','college'],required_words = ['pincode'])
    response('https://www.vce.ac.in/Facilities/Library/Working_Hours', ['what', 'are', 'the', 'library', 'timings'], required_words=['library','timings'])
    response('https://www.vce.ac.in/Facilities/Library/Rare_Books',['what', 'are', 'the', 'rare','books','in', 'library'], required_words = ['rare','books'])
    response('https://www.vce.ac.in/Facilities/Library/Library_Rules',['what', 'are', 'the', 'rules', 'of', 'vce', 'library'], required_words=['rules', 'library'])
    response('https://www.vce.ac.in/Staff_List.cshtml?Department=Civil',['civil','faculty'],required_words=['civil','faculty'])
    response('https://www.vce.ac.in/Staff_List.cshtml?Department=CSE', ['CSE', 'faculty'],required_words=['cse', 'faculty'])
    response('https://www.vce.ac.in/Staff_List.cshtml?Department=ECE', ['ECE', 'faculty'],required_words=['ece', 'faculty'])
    response('https://www.vce.ac.in/Staff_List.cshtml?Department=EEE', ['EEE', 'faculty'],required_words=['eee', 'faculty'])
    response('https://www.vce.ac.in/Staff_List.cshtml?Department=Mech.', ['mechanical', 'faculty'],required_words=['mech', 'faculty'])
    response('https://www.vce.ac.in/Staff_List.cshtml?Department=IT', ['IT', 'faculty'],required_words=['it', 'faculty'])
    response('https://www.vce.ac.in/Facilities/GamesnSports/Facilities_Games',['facility','of','games'],required_words=['games'])
    response('Sri Pendekanti Venkatasubbaiah is the founder of vce',['vce','founder'],required_words=['vce','founder'])
    response('No in vasavi college we don\'t have hostel facility',['Is', 'there', 'any', 'hostel', 'facility', 'available', 'in', 'vasavi', 'college', 'vce'],required_words=['hostel', 'facility'])
    response('Yes we have transportation facility in vasavi college',['what', 'are', 'transportation', 'facilities', 'in', 'vasavi', 'college', 'vce'],required_words=['transportation'])
    response('https://www.vce.ac.in/Facilities/Transport.cshtml',['what', 'are', 'different', 'routes', 'of', 'transportation'],required_words=['routes'])



    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 0.5 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

print("********WELCOME TO THE VASAVI CHAT ASSISTANT********")

while True:
    s = get_response(input('You: '))
    print('Bot: ' + s)
    if s == 'See you!, Have a nice day!':
        break
