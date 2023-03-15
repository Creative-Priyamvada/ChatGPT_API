import openai
import os
from dotenv import load_dotenv
import re
import json

load_dotenv()


# Set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY") 

def extract_int(string_val):
    try:
        int_val = int(re.search(r'\d+', string_val).group())
        return int_val
    except (ValueError,AttributeError):
        print("The value passed is not a valid number")
        return None

def chatGPT_output(question, answer):
    #print('question : ',question)
    #print('answer :',answer)

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": "Please act as evaluator, question: {question}, answer: {answer}, Please rate this answer between 0 and 10 and respond in format 'rating : ' and 'comment : ' in json format".format(question = question, answer= answer)}]
    )

    message= dict(completion.choices[0].message)
    print('--message-- ',message)
    content=message['content']

    response_chatGPT_dict = {}
    #response_chatGPT_dict["content"] = content

    try:
        print('--1st try block----')
        try:
            response = json.loads(content)
        except json.decoder.JSONDecodeError:
            raise Exception('Error: JSONDecodeError occurred')
        else:
            rating = response.get('rating')
            comment = response.get('comment')
            response_chatGPT_dict["rating"] = rating
            response_chatGPT_dict["comment"] = comment
    except:
        print('--1st except block----')
        # Extract rating from the response
        rating_match = re.findall(r"rating\s*:\s*(\d+)", content)
        if rating_match:
            rating = extract_int(rating_match[0])
            response_chatGPT_dict["rating"] = rating
        
        # Extract comment from the response
        comment_match = re.findall(r"comment\s*:\s*(.*)", content)
        if comment_match:
            comment = comment_match[0].strip()
            response_chatGPT_dict["comment"] = comment








    '''try:
        print('--1st try block----')
        # Extract rating from the response
        rating_match = re.findall(r"rating\s*:\s*(\d+)", content)
        if rating_match:
            rating = extract_int(rating_match[0])
            response_chatGPT_dict["rating"] = rating
        
        # Extract comment from the response
        comment_match = re.findall(r"comment\s*:\s*(.*)", content)
        if comment_match:
            comment = comment_match[0].strip()
            response_chatGPT_dict["comment"] = comment
    except:
        print('--1st except block----')
        try:
            response = json.loads(content)
        except json.decoder.JSONDecodeError:
            pass
        else:
            rating = response.get('rating')
            comment = response.get('comment')
            response_chatGPT_dict["rating"] = rating
            response_chatGPT_dict["comment"] = comment'''




    '''try:
        print('--- in try block ---')
        response = json.loads(content)
        rating = response.get('rating')
        comment = response.get('comment')
    except json.decoder.JSONDecodeError:
        print(' -- in except block --')
        #rating = extract_int(re.findall(r"rating: (\d+)", content)[0])
        rating = extract_int(content)
        comment = re.findall(r"comment: (.+)", content)[0]

    #print('---rating,comment from chatGPT---',rating,comment)


    try:
        response_chatGPT_dict = {'rating': rating, 'comments': comment}
    except Exception as e:
        print(f"Exception occurred: {e}")
        response_chatGPT_dict = {'rating': 0, 'comments': content}'''


    if not response_chatGPT_dict:
        response_chatGPT_dict["rating"] = 0
        response_chatGPT_dict["comment"] = content
    #print('--response_chatGPT_dict-- :', response_chatGPT_dict)
    return response_chatGPT_dict


    '''try:
        print('---- in try block ----')
        text = json.loads(content)
        rating = text['rating']
        comment = text['comment']
        print('--rating,comment-- ',rating,comment)

    except(KeyError, ValueError, json.JSONDecodeError):
        # if the 'content' is not a valid JSON string
        print('---- in except block ----')
        lines = content.strip().split('\n')
        print('--lines--',lines,type(lines))
        for i in lines:
            print('---i---- from func:',i)
            split_item = i.split(':')
            print('(split_item[0]).lower()) :-----',(split_item[0]).lower())
            if 'rating' in ((split_item[0]).lower()):
                rating=extract_int(split_item[1])
                print('*** rating from func***',rating)
            elif 'comment' in ((split_item[0]).lower()):
                comments=(split_item[1])
                print('*** comments from func***',comments)
        print('--rating,comment-- ',rating,comment)'''

    
                


            

    print('***************************************************************************')
    print('***************************************************************************')


        #print('--rating,comment-- ',rating,comment)


    '''try:
        text = json.loads(completion.choices[0].message.content)
        response_chatGPT_dict = {'rating': text['rating'], 'comments': text['comment']}
    except Exception as e:
        print(f"Exception occurred: {e}")
        text = completion.choices[0].message.content
        response_chatGPT_dict = {'rating': 0, 'comments': text}

    print('--response_chatGPT_dict-- :', response_chatGPT_dict)
    return response_chatGPT_dict'''




#chatGPT_output("what is apple","apple is a fruit")
